from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

    @staticmethod
    def from_env(env: Env):
        mode: str = env.str('MODE')
        admin_ids = list(map(int, env.list('ADMINS')))

        if mode == 'dev':
            token: str = env.str('DEV_BOT_TOKEN')
        else:
            token: str = env.str('PROD_BOT_TOKEN')

        return TgBot(
            token=token,
            admin_ids=admin_ids
        )


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot.from_env(env),
    )
