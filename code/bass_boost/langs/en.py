class Lang(object):
    lang = "en"
    format_unsupported = "Unsupported audio format."
    start_message = "This bot can boost the bass in audio files you send. Just send me an audio."
    help_message = start_message + "\n\nPart of the @luckydonaldsbots network.\n\nTHIS BOT IS SO CRAPPY\nYO!!! M8!!! WHY U USE IT?!?"
    caption = "@{bot} just boosted your bass!"
    caption_shit = lambda times: "!!!!111111!!112111!"[:times] + ("" if times < 20 else ("ONE" if times < 21 else "ELEVEN") + "!11!1!111!1!!"[:times-21] + "".join(str(i-33) for i in range(34, times)))
    progress0 = "downloading file"
    progress1 = "loading audio"
    progress2 = "parsing track"
    progress3 = "calculating average bass boost needed"
    progress4 = "calculating bass boost"
    progress5 = "calculating bigger bass boost"
    progress6 = "extracting regions to boost"
    progress7 = "applying boosted bass to original track"
    generic_error = "An error occurred. Please retry when bug is fixed."
# end class
