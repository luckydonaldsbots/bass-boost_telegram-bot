class Lang(object):
    lang = "en"
    format_unsupported = "Unsupported audio format."
    start_message = "This bot can boost the bass in audio files you send. Just send me an audio."
    help_message = start_message + "\n\nPart of the @luckydonaldsbots network.\n\nTHIS BOT IS SO CRAPPY\nYO!!! M8!!! WHY U USE IT?!?"
    caption = "@{bot} just boosted your bass!"
    caption_shit = lambda times: "!!!!111111!!112111!"[:times] + ("" if times < 20 else ("ONE" if times < 21 else "ELEVEN") + "!11!1!111!1!!"[:times-21] + "".join(str(i-33) for i in range(34, times)))
# end class
