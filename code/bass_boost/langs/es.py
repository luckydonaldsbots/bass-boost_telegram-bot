from .en import Lang as LBase

class Lang(LBase):
    """ Thanks Pigeon """
    lang = "es"
    format_unsupported = "Formato de audio no soportado."
    start_message = "Este bot puede potenciar los graves en archivos de audio. Simplemente envíame un audio."
    help_message = start_message + "\n\nParte de la red de bots de @luckydonaldsbots .\n\nESTE BOT ES TAN MALO\n¡¡¡OYE!!! ¡¡¡TU!!! ¡¡¡POR QUÉ LO USAS?!?"
    caption = "¡ @{bot} acaba de potenciar los graves!"
    progress1 = "cargando audio"
    progress0 = progress1
    progress2 = "analizando pista de audio"
    progress3 = "calculando el aumento medio de los graves que será necesario"
    progress4 = "calculando potenciación de graves"
    progress5 = "calculando una mayor potenciación de los graves"
    progress6 = "extrayendo regiones para potenciar"
    progress7 = "aplicando potenciación de graves a la pista de audio original"