# -*- coding: utf-8 -*-
from flask import Flask, url_for, jsonify
from pytgbot import Bot
from pytgbot.api_types.receivable.media import Audio
from pytgbot.api_types.receivable.peer import User
from pytgbot.api_types.receivable.updates import Message
from teleflask.messages import HTMLMessage
from luckydonaldUtils.logger import logging

from .langs import l
from .secrets import API_KEY, URL_HOSTNAME, URL_PATH
from .celery.process_audio import process_audio
from luckydonaldUtils.exceptions import assert_type_or_raise
import re

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)
logging.add_colored_handler(level=logging.DEBUG)

from teleflask import Teleflask
app = Flask(__name__)

# sentry = add_error_reporting(app)
bot = Teleflask(API_KEY, hostname=URL_HOSTNAME, hostpath=URL_PATH, hookpath="/income/{API_KEY}")
bot.init_app(app)

assert_type_or_raise(bot.bot, Bot)

@app.errorhandler(404)
def url_404(error):
    return "Nope.", 404
# end def


@app.route("/", methods=["GET","POST"])
def url_root():
    return "Yep."
# end def


@app.route("/healthcheck")
def url_healthcheck():
    """
    Checks if telegram api works.
    :return:
    """
    status = {}

    try:
        me = bot.bot.get_me()
        assert isinstance(me, User)
        logger.info(me)
        status['telegram api'] = True
    except Exception as e:
        logger.exception("Telegram API failed.")
        status['telegram api'] = False
    # end try

    success = all(x for x in status.values())
    return jsonify(status), 200 if success else 500
# end def



@bot.command("start")
def cmd_start(update, text):
    return HTMLMessage(l(update.message.from_peer.language_code).start_message)
# end def


@bot.command("help")
def cmd_start(update, text):
    return HTMLMessage(l(update.message.from_peer.language_code).help_message)
# end def


@bot.on_message("audio")
def msg_audio(update, msg):
    assert isinstance(msg, Message)
    assert isinstance(msg.audio, Audio)
    assert isinstance(msg.from_peer, User)
    ln = l(msg.from_peer.language_code)
    progress = bot.bot.send_message(
        chat_id=msg.chat.id, text=ln.task_scheduled, disable_web_page_preview=True,
        disable_notification=False, reply_to_message_id=msg.message_id,
    )
    process_audio.delay(
        api_key=API_KEY,
        progress_msg_id=progress.message_id,
        chat_id=msg.chat.id,
        message_id=msg.message_id,
        audio=msg.audio.to_array(),
        language_code=msg.from_peer.language_code
    )
# end def
