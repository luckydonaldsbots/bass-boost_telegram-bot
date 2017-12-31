# -*- coding: utf-8 -*-
import requests
from flask import Flask, url_for
from luckydonaldUtils.logger import logging
from pydub import AudioSegment
from pytgbot import Bot
from pytgbot.api_types.receivable.media import Audio
from pytgbot.api_types.receivable.peer import Chat, User
from pytgbot.api_types.receivable.updates import Message, Update
from pytgbot.api_types.sendable.files import InputFile
from teleflask.messages import HTMLMessage

from bass_boost.boost import boost
from .langs import l
from .secrets import API_KEY, URL_HOSTNAME, URL_PATH
from luckydonaldUtils.exceptions import assert_type_or_raise
import re
from html import escape
from io import BytesIO

POSSIBLE_CHAT_TYPES = ("supergroup", "group", "channel")
SEND_BACKOFF = 5

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)
logging.add_colored_handler(level=logging.DEBUG)

from teleflask import Teleflask
app = Flask(__name__)

# sentry = add_error_reporting(app)
bot = Teleflask(API_KEY, hostname=URL_HOSTNAME, hostpath=URL_PATH, hookpath="/income/{API_KEY}")
bot.init_app(app)

assert_type_or_raise(bot.bot, Bot)
AT_ADMIN_REGEX = re.compile(".*([^\\w]|^)@(admins?|{bot})(\\W|$).*".format(bot=bot.username))


@app.errorhandler(404)
def url_404(error):
    return "Nope.", 404
# end def


@app.route("/", methods=["GET","POST"])
def url_root():
    return "Yep."
# end def


@app.route("/test", methods=["GET","POST"])
def url_test():
    return "Success", 200
# end def

@app.route("/healthcheck")
def url_healthcheck():
    return '[ OK ]', 200
    #return '[FAIL]', 500
# end def



@bot.command("start")
def cmd_start(update, text):
    return HTMLMessage(l(update.message.from_peer.language_code).help_message)
# end def


@bot.command("help")
def cmd_start(update, text):
    return HTMLMessage(l(update.message.from_peer.language_code).help_message)
# end def


AUDIO_FORMATS = {
    "audio/mpeg3": "mp3",
    "audio/x-mpeg-3": "mp3",
    "audio/mpeg": "mp3",
}

from .langs import l
@bot.on_message("audio")
def msg_audio(update, msg):
    assert isinstance(msg, Message)
    assert isinstance(msg.audio, Audio)
    assert isinstance(msg.from_peer, User)
    process_audio(
        audio=msg.audio,
        chat_id=msg.chat.id,
        message_id=msg.message_id,
        file_id=msg.audio.file_id,
        language_code=msg.from_peer.language_code
    )
# end def

def process_audio(audio, chat_id, message_id, file_id, language_code):
    assert isinstance(audio, Audio)
    assert isinstance(bot.bot, Bot)
    ln = l(language_code)
    progress = bot.bot.send_message(
        chat_id=chat_id, text="downloading audio", disable_web_page_preview=True,
        disable_notification=False, reply_to_message_id=message_id
    )
    file_in = bot.bot.get_file(file_id)
    url = bot.bot.get_download_url(file_in)
    r = requests.get(url, stream=True)
    fake_file_in = BytesIO(r.content)
    fake_file_out = BytesIO()
    if audio.mime_type not in AUDIO_FORMATS:
        return ln.format_unsupported
    # end if
    audio_format = AUDIO_FORMATS[audio.mime_type]
    audio_in = AudioSegment.from_file(fake_file_in, format=audio_format)
    audio_out = None
    for step in boost(audio_in):
        if isinstance(step, str):
            bot.bot.edit_message_text(
                step, chat_id, progress.message_id, disable_web_page_preview=True
            )
            bot.bot.send_chat_action(chat_id, "record_audio")
        # end if
        else:
            audio_out = step
            break
        # end for
    # end def
    bot.bot.send_chat_action(chat_id, "upload_audio")
    audio_out.export(fake_file_out, format="mp3", tags={"comment": "TEST°!!!", "title":"test title"})
    file_out = InputFile(fake_file_out.getvalue(), file_name="moar bass.mp3", file_mime="audio/mpeg")
    bot.bot.send_chat_action(chat_id, "upload_audio")
    caption = ln.caption.format(bot=bot.username)
    bot.bot.send_audio(
        chat_id, file_out,
        caption=caption, duration=audio.duration,
        performer=audio.performer, title=audio.title,
        disable_notification=False, reply_to_message_id=message_id
    )
    bot.bot.delete_message(chat_id, progress.message_id)
# end def


@app.route("/boobs/" + API_KEY + "/<path:url>")
def bass_booooooost_bitches(tg_file_url):
    url = "https://api.telegram.org/file/bot" + API_KEY + "/" + tg_file_url
    r = requests.get(url, stream=True)
    input = AudioSegment.from_file(r)

    def stream():
        for chunk in r.iter_content(chunk_size=1024):
            yield chunk
            # end for

    # end def
    from flask import Response
    return Response(stream(), mimetype="image/jpg")
# end def



def format_user(peer):
    assert isinstance(peer, User)
    name = (str(peer.first_name) if peer.first_name else "" + " " + str(peer.last_name)).strip() if peer.last_name else ""
    if name:
        name = '<b>{name}</b> '.format(name=escape(name))
    else:
        name = ''
    # end if
    username = ('<a href="t.me/{username}">@{username}</a> '.format(username=str(peer.username).strip())) if peer.username else ""
    return '{name}{username}(<a href="tg://user?id={id}">{id}</a>)'.format(name=name, username=username, id=peer.id)
# end if


def format_chat(message):
    chat, msg_id = message.chat, message.message_id
    assert isinstance(chat, Chat)
    assert isinstance(bot.bot, Bot)
    logger.info(repr(message))
    if chat.title:
        title = "<b>{title}</b>".format(title=escape(chat.title))
    else:
        title = "<i>{untitled_chat}</i>".format(untitled_chat=LangEN.untitled_chat)
    # end if
    if chat.username:
        return '{title} <a href="t.me/{username}/{msg_id}">@{username}</a>'.format(
            username=chat.username, msg_id=msg_id, title=title, chat_id=chat.id
        )
    # end if

    # try getting an invite link.
    invite_link = chat.invite_link
    if chat.type in ("supergroup", "channel") and not invite_link:
        try:
            invite_link = bot.bot.export_chat_invite_link(chat.id)
        except:
            logger.exception("export_chat_invite_link Exception.")
        # end try
    try:
        chat = bot.bot.get_chat(chat.id)
        invite_link = chat.invite_link
    except:
        pass
        # end if
    if invite_link:
        return '{title} (<a href="{invite_link}">{chat_id}</a>)'.format(
            title=title, invite_link=invite_link, chat_id=chat.id
        )
    else:
        return '{title} (<code>{chat_id}</code>)'.format(title=title, chat_id=chat.id)
    # end if
# end def


@bot.on_message("new_chat_members")
def on_join(update, message):
    assert_type_or_raise(message.new_chat_members, list)
    if bot.user_id not in [user.id for user in message.new_chat_members if isinstance(user, User)]:
        # not we were added
        return
    # end if

    return HTMLMessage(LangEN.join_message.format(bot=bot.username, chat_id=message.chat.id) + (LangEN.unstable_text if bot.username == "hey_admin_bot" else ""))
#end def


