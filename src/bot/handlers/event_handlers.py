import logging

from aiogram import Dispatcher

from settings import WEBHOOK_URL
from bot.bot import bot


async def base_on_startup(dp: Dispatcher) -> None:
    pass


async def on_startup(dp: Dispatcher) -> None:
    await base_on_startup(dp)
    logging.info(f"Set webhook {WEBHOOK_URL}")
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp: Dispatcher) -> None:
    logging.warning("Shutting down..")

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning("Bye!")
