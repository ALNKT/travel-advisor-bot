from aiogram.utils import executor

from database.CRUD import init_db, close_db
from telegram_API.handlers.restaurants import *

init_db()

executor.start_polling(dp, skip_updates=True)
close_db()
