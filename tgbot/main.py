import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from peewee import SqliteDatabase

from infrastructure.database.setup import setup_database
from tgbot.config import load_config
from tgbot.handlers import routers
from tgbot.middlewares.database import DatabaseMiddleware
from tgbot.services import broadcaster


async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "Bot has been started")


def register_global_middlewares(dp: Dispatcher, db: SqliteDatabase):
    middleware_types = [
        DatabaseMiddleware(db)
    ]

    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


async def main():
    setup_logging()
    db = setup_database()

    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_routers(*routers)

    register_global_middlewares(dp, db)

    await on_startup(bot, config.tg_bot.admin_ids)
    await dp.start_polling(bot, config=config)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot has been stopped")
