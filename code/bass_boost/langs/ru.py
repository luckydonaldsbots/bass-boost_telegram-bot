from .en import Lang as LBase

class Lang(LBase):
    """ Thanks @ekazak48 """
    lang = "ru"
    format_unsupported = "Неподдерживаемый формат файла."
    start_message = "Этот бот может прокачать бас в отправленных вами аудиофайлах. Просто отправьте мне аудио."
    help_message = start_message + "\n\nЭтот бот является частью сети @luckydonaldsbots.\n\nЭТОТ БОТ ОЧЕНЬ ХЕРОВЫЙ\n ЙО, ЧУВАК!!!! ЗАЧЕМ ТЫ ЕГО ИСПОЛЬЗУЕШЬ?!?"
    caption = "@{bot} прокачал ваш бас!"
    progress0 = "скачивание аудио"
    progress1 = "загрузка аудио"
    progress2 = "анализ дорожки"
    progress3 = "расчёт средней необходимой прокачки басов"
    progress4 = "расчёт прокачки басов"
    progress5 = "расчёт максимальной прокачки басов"
    progress6 = "распаковка частей дорожки для прокачки"
    progress7 = "применение прокачанного баса к оригинальному треку"
