# stream.py
# URL Scheme:
# twitch://open?channel=hasanabi&quality=720p&pip=false
#
import logging
import sys
from typing import Union
import urllib.parse

from .player import format_channel, Player, load_config


def handle_exception(exc_type, exc_value, exc_traceback):
    """
    Ensure exceptions are logged instead of being discarded
    """
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


LOG_PATH = "/tmp/streampipe.log"


def main():
    logging.basicConfig(filename=LOG_PATH, level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    sys.excepthook = handle_exception

    if not len(sys.argv) >= 2:
        logging.error("Not enough arguments")
        sys.exit()

    config = load_config()
    if "token" in config:
        logging.info(f"Using oauth token {config['token']}")

    logging.info("Handling URL: {}".format(sys.argv[1]))
    url = urllib.parse.urlparse(sys.argv[1])
    query = urllib.parse.parse_qs(url.query)

    play_url = format_channel(query["channel"][0])

    player_kwargs: dict[str, Union[str, bool]] = dict(
        pip=False, oauth_token=config["token"]
    )
    if "quality" in query:
        player_kwargs["quality"] = query["quality"][0]

    if "pip" in query and query["pip"][0] == "true":
        player_kwargs["pip"] = True

    Player.play(play_url, **player_kwargs)
