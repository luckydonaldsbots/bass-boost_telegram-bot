from .en import Lang as LBase

class Lang(LBase):
    """ Thanks @luckydonald """
    lang = "de"
    format_unsupported = "Nicht unterstüztes Audio Format."
    start_message = "Dieser Bot verstärkt den Bass in Musik die du schickst. Probier's mal mit 'ner Audiodatei."
    help_message = start_message + "\n\nTeil des @luckydonaldsbots Netzwerkes.\n\nDIESER BOT IST SO EIN MÜLL\nJO!!! DIGGR!!! WARUM NUTZT DU DAS?"
    caption = "@{bot} verstärkte grade den Bass!"
    capslock_number_1 = "EINS"
    capslock_number_11 = "ELF"
    capslock_number_111 = "EINHUNDERTUNDELF"
    progress0 = "Läd Datei herunter"
    progress1 = "Lädt Audio"
    progress2 = "Zerteilung des Tracks"
    progress3 = "Berechnung des durchschnittlich benötigten Basses"
    progress4 = "Berechne Bassverstärkung"
    progress5 = "Berechne stärkere Bassverstärkung"
    progress6 = "Extrahiere zu verstärkende Bereiche"
    progress7 = "Wende den besseren Bass auf die Orginalspur an"
    generic_error = "Ein Fehler trat auf. Bitte versuche es erneut, sobald dieser behoben ist."
    task_scheduled = "Deine Datei wurde zur Bassverstärkung eingereiht."
# end class
