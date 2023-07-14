import datetime
import logging
from imaplib import Time2Internaldate
from typing import Optional
logger = logging.getLogger(__name__)


def str_encode(
    value: str, encoding: Optional[str] = None, errors: str = "strict"
) -> str:
    """
    Encodes a string with the specified encoding and error handling.

    Args:
        value: The string to encode.
        encoding: The name of the encoding to use. If not provided, the default encoding is used.
        errors: The error handling scheme. Default is 'strict'.

    Returns:
        The encoded string.

    Raises:
        UnicodeError: If the string cannot be encoded.

    Examples:
        >>> str_encode('hello', encoding='utf-8')
        'hello'

        >>> str_encode('Привет', encoding='utf-8')
        'Привет'
    """
    logger.debug(
        f"Encode str '{value}' with encoding '{encoding}' and error handling '{errors}'"
    )
    return str(value.encode(encoding, errors))


def str_decode(value='', encoding=None, errors='strict'):
    if isinstance(value, str):
        return bytes(value, encoding, errors).decode('utf-8')
    elif isinstance(value, bytes):
        return value.decode(encoding or 'utf-8', errors=errors)
    else:
        raise TypeError("Cannot decode '{}' object".format(value.__class__))


def date_to_date_text(date):
    """Return a date in the RFC 3501 date-text syntax"""
    tzutc = datetime.timezone.utc
    dt = datetime.datetime.combine(date, datetime.time.min, tzutc)
    return Time2Internaldate(dt)[1:12]
