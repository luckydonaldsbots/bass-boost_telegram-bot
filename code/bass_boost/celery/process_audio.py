# -*- coding: utf-8 -*-
from io import BytesIO

import requests
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.logger import logging
from pydub import AudioSegment
from pytgbot.bot import Bot
from pytgbot.api_types.receivable.media import Audio
from pytgbot.api_types.sendable.files import InputFile
from pytgbot.exceptions import TgApiServerException

from . import celery
from ..boost import boost
from ..langs import l

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)

AUDIO_FORMATS = {
    "audio/mp3": "mp3",
    "audio/mpeg3": "mp3",
    "audio/x-mpeg-3": "mp3",
    "audio/mpeg": "mp3",
}


@celery.task(ignore_result=True)
def process_audio(api_key, audio, chat_id, message_id, file_id, language_code):
    assert isinstance(audio, dict)
    audio = Audio.from_array(audio)
    assert isinstance(audio, Audio)
    bot = Bot(api_key)
    bot.username = bot.get_me().username
    assert isinstance(bot, Bot)
    ln = l(language_code)
    progress = bot.send_message(
        chat_id=chat_id, text=ln.progress0, disable_web_page_preview=True,
        disable_notification=False, reply_to_message_id=message_id
    )

    #if audio.duration > 210 or audio.file_size > 7000000:  # 3.5 minutes
    #    bot.edit_message_text(
    #        ln.file_too_big, chat_id, progress.message_id, disable_web_page_preview=True
    #    )
    #    return
    ## end if

    try:
        logger.debug("Mime is {mime}".format(mime=audio.mime_type))
        if audio.mime_type not in AUDIO_FORMATS:
            logger.debug("Mime is wrong")
            bot.edit_message_text(
                ln.format_unsupported, chat_id, progress.message_id, disable_web_page_preview=True
            )
            return
        # end if

        logger.debug("Downloading file: {id}".format(id=file_id))
        file_in = bot.get_file(file_id)
        url = bot.get_download_url(file_in)
        logger.debug("Downloading file: {url}".format(url=url))
        r = requests.get(url, stream=True)
        logger.debug("Downloaded file.")
        fake_file_in = BytesIO(r.content)
        fake_file_out = BytesIO()
        audio_format = AUDIO_FORMATS[audio.mime_type]
        logger.debug("Format is {format}".format(format=audio_format))
        audio_in = AudioSegment.from_file(fake_file_in, format=audio_format)
        audio_out = None
        logger.debug("Calling boost()...")
        for step in boost(audio_in):
            if isinstance(step, int):
                text = getattr(ln, "progress" + str(step))
                logger.debug("Progress {step}: {text}".format(step=step, text=text))
                try:
                    bot.edit_message_text(
                        text, chat_id, progress.message_id, disable_web_page_preview=True
                    )
                except TgApiServerException:
                    logger.exception("Editing status message failed")
                # end try
            # end if
            else:
                audio_out = step
            # end for
            bot.send_chat_action(chat_id, "record_audio")
        # end def
        logger.debug("Done with boost()...")
        assert_type_or_raise(audio_out, AudioSegment)
        assert isinstance(audio_out, AudioSegment)
        bot.send_chat_action(chat_id, "upload_audio")
        bot_link = "https://t.me/{bot}".format(bot=bot.username)
        tags = {
            "composer": bot_link,
            "service_name": bot_link,
            "comment": "TEST°!!!",
            "genre": "BOOSTED BASS",
            "encoder": "Horseapples 1.2 - {bot_link} (littlepip is best pony/)".format(bot_link=bot_link),
            "encoded_by": bot_link
        }
        if audio.title:
            tags["title"] = audio.title
        # end if
        if audio.performer:
            tags["artist"] = audio.performer
        # end if
        audio_out.export(fake_file_out, format="mp3",tags=tags)
        file_out = InputFile(
            fake_file_out.getvalue(), file_mime="audio/mpeg",
            file_name="bass boosted by @{bot}.mp3".format(bot=bot.username),
        )
        bot.send_chat_action(chat_id, "upload_audio")
        caption = ln.caption.format(bot=bot.username)
        logger.debug("uploading new audio")
        bot.send_audio(
            chat_id, file_out,
            caption=caption, duration=audio.duration,
            performer=audio.performer, title=audio.title,
            disable_notification=False, reply_to_message_id=message_id
        )
        logger.debug("deleting status message")
        bot.delete_message(chat_id, progress.message_id)
    except Exception as e:
        logger.exception("Got Exeption instead of bass!")
        bot.edit_message_text(
            ln.generic_error, chat_id, progress.message_id, disable_web_page_preview=True
        )
    # end try
# end def
