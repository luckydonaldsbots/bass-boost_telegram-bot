from .en import Lang as LBase

class Lang(LBase):
    lang = "de"
    format_unsupported = "Nicht unterstüztes Audio Format."
    start_message = "Dieser Bot verstärkt den Bass in Musik die du schickst. Probier's mal mit 'ner Audiodatei."
    help_message = start_message + "\n\nTeil des @luckydonaldsbots Netzwerkes.\n\nDIESER BOT IST SO EIN MÜLL\nJO!!! DIGGR!!! WARUM NUTZT DU DAS?"
    caption = "@{bot} verstärkte grade den Bass!"
    caption_shit = lambda times: "!!!!111111!!112111!"[:times] + ("" if times < 20 else ("ONE" if times < 21 else "ELEVEN") + "!11!1!111!1!!"[:times-21] + "".join(str(i-33) for i in range(34, times)))
# end class
