import uvloop

from bot.bot import dp
from bot.handlers.event_handlers import on_shutdown, base_on_startup
from settings import BOT_MODE, BotMode


uvloop.install()


def run_polling() -> None:
    from aiogram.utils import executor
    executor.start_polling(
        dp, skip_updates=True, on_startup=base_on_startup, on_shutdown=on_shutdown
    )


def run_webhook() -> None:
    from aiogram.dispatcher.webhook import DEFAULT_ROUTE_NAME
    from aiogram.utils.executor import set_webhook

    from bot.handlers.event_handlers import on_startup
    from server.application import init_app
    from settings import WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_PATH


    web_app = init_app()
    print(f"Start bot on {WEBHOOK_PATH}")
    executor = set_webhook(
        web_app=web_app,
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        loop=None,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        check_ip=False,
        retry_after=False,
        route_name=DEFAULT_ROUTE_NAME,
    )
    executor.run_app(
        host=WEBAPP_HOST, port=WEBAPP_PORT,
    )


def main() -> None:
    if BOT_MODE == BotMode.polling:
        run_polling()
    elif BOT_MODE == BotMode.webhooks:
        run_webhook()
    else:
        raise ValueError(f"Unknown bot mode: {BOT_MODE}")


if __name__ == "__main__":
    main()
