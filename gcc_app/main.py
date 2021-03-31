from aiogram.utils import executor

from gcc_app.app import dp
from gcc_app import controllers


if __name__ == '__main__':
    executor.start_polling(dp)