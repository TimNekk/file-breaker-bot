from dataclasses import dataclass

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов


@dataclass
class DB:
    user = env.str('db_user')
    password = env.str('db_password')
    database = env.str('db_database')
    ip = env.str('db_ip')
    uri = f"postgres://{user}:{password}@{ip}/{database}"
