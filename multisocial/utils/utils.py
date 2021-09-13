import re
import csv
import json
from datetime import datetime, timezone
from pyshorteners import Shortener

# convert UTC to YYYY-MM-DD HH:MM:SS format
convert_utc = lambda utc: datetime.utcfromtimestamp(int(utc)).strftime("%Y-%m-%d %H:%M:%S")

# shorten URLs using tinyurl
shorten_url = lambda url: Shortener().tinyurl.short(url)

# get current UTC timestamp in YYYY-MM-DD HH:MM:SS format
TIMESTAMP = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

def validate_url(url: str) -> bool:
    """
    Validate the input URL

    Parameters
    ----------
    url
        string
        URL to validate
    
    Returns
    -------
    bool
        True if URL is valid, else False
    """
    REGEX = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$',
        re.IGNORECASE
    )
    RESULT = re.match(REGEX, url) is not None

    return RESULT
