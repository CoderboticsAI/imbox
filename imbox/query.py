import datetime

from imbox.utils import date_to_date_text
from typing import Dict, Any


def format_value(value: Any) -> str:
    """Formats the value based on its type."""
    if isinstance(value, datetime.date):
        value = date_to_date_text(value)
    if isinstance(value, str) and '"' in value:
        value = value.replace('"', "'")
    return value


def build_search_query(imap_attribute_lookup: Dict[str, str], **kwargs: Any) -> str:
    """Builds a search query string for IMAP based on the given criteria.

    Args:
        imap_attribute_lookup (Dict[str, str]): A dictionary mapping attribute names to IMAP attribute placeholders.
        kwargs (Any): Keyword arguments representing search criteria.

    Returns:
        str: The search query string.

    Example:
        >>> imap_attribute_lookup = {'subject': 'SUBJECT "{}"', 'from': 'FROM "{}"'}
        >>> build_search_query(imap_attribute_lookup, subject="Hello", from="example@gmail.com")
        'SUBJECT "Hello" FROM "example@gmail.com"'
    """
    query = []
    for name, value in kwargs.items():
        if value is not None:
            value = format_value(value)
            query.append(imap_attribute_lookup[name].format(value))

    if query:
        return " ".join(query)

    return "(ALL)"
