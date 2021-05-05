from aiogram.utils import executor

from gcc_app.app import dp, shutdown

# todo skip_updates=True ?
if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)