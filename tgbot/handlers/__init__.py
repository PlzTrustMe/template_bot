from aiogram import Router

from tgbot.handlers.bot.start import router as start_router

routers: list[Router] = [start_router]

__all__ = ['routers']
