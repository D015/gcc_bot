from aiogram.utils import executor

from app import dp, shutdown, startup
import controllers

controllers = controllers
# todo skip_updates=True ?
if __name__ == "__main__":
    executor.start_polling(dp, on_shutdown=shutdown, on_startup=startup)
