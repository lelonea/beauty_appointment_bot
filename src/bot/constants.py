from aiogram.utils.text_decorations import markdown_decoration


link = markdown_decoration.link
bold = markdown_decoration.bold

HELP_MESSAGE = (
    f"{bold('Привет!')}\nЭто бот для мастеров.\n"
    "Нашёл ошибку или есть предложения по улучшению? Напиши нам: @leloneya @devexc\n"
    "Если хочешь поддержать разработку обновлений: "
    f"{link('Кошелёк для доната', 'https://paypal.me/devexc?locale.x=en_US')}"
)

START_MESSAGE = (
    f"{bold('Привет!')}\nЭто бот для мастеров.\n"
    "Здесь ты можешь управлять своими окошками и клиентами.\n"
    "Кликни на кнопку ниже, чтобы начать."
)
