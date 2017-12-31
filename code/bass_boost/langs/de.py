from .en import Lang as LBase

class Lang(LBase):
    """ Thanks @luckydonald """
    lang = "de"
    format_unsupported = "Nicht unterstüztes Audio Format."
    start_message = "Dieser Bot verstärkt den Bass in Musik die du schickst. Probier's mal mit 'ner Audiodatei."
    help_message = start_message + "\n\nTeil des @luckydonaldsbots Netzwerkes.\n\nDIESER BOT IST SO EIN MÜLL\nJO!!! DIGGR!!! WARUM NUTZT DU DAS?"
    caption = "@{bot} verstärkte grade den Bass!"
    caption_shit = lambda times: "!!!!111111!!112111!"[:times] + ("" if times < 20 else ("ONE" if times < 21 else "ELEVEN") + "!11!1!111!1!!"[:times-21] + "".join(str(i-33) for i in range(34, times)))
    progress1 = "Lädt Audio"
    progress2 = "Zerteilung track"
    progress3 = "calculating average bass boost needed"
    progress4 = "calculating bass boost"
    progress5 = "calculating bigger bass boost"
    progress6 = "extracting regions to boost"
    progress7 = "applying boosted bass to original track"
# end class
