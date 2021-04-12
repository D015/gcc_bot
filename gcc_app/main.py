from aiogram.utils import executor

from gcc_app.app import dp, shutdown
from gcc_app import controllers

# todo skip_updates=True ?
if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)