

from pytgbot.api_types.receivable.peer import User
from pytgbot.api_types.receivable.updates import Message
from luckydonaldUtils.exceptions import assert_type_or_raise

from . import en, de, es, it, ru
from .en import Lang as DefaultLang
LANG = {
    "default": DefaultLang,
    "en": en.Lang,
    "de": de.Lang,
    "es": es.Lang,
    "it": it.Lang,
    "ru": ru.Lang,
    "en-US": en.Lang,
    "de-DE": de.Lang,
}


def l(msg_or_language_code=None) -> DefaultLang:
    assert_type_or_raise(msg_or_language_code,  None, str, Message,  parameter_name="msg")

    # if is message, get the language_code from there.
    if isinstance(msg_or_language_code, Message):
        if not msg_or_language_code.from_peer or not msg_or_language_code.from_peer.language_code:
            msg_or_language_code = None
        else:
            msg_or_language_code = msg_or_language_code.from_peer.language_code
        # end if
    # end def

    # if it now is None (default, or getting from message failed), use the default
    if msg_or_language_code is None or msg_or_language_code not in LANG:
        return LANG['default']
    # end if
    return LANG[msg_or_language_code]
# end def
