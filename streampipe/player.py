import logging
import os
import pathlib
import subprocess
from typing import Optional, Union

DEFAULT_QUALITY = "720,720p60,best"
# PLAYER_PATH = "/Applications/IINA.app/Contents/MacOS/iina-cli"
PLAYER_PATH = "/Applications/VLC.app/Contents/MacOS/VLC"
STREAMLINK_PATH = "/opt/homebrew/bin/streamlink"
CONFIG_FILENAME = ".streampiperc"


def load_config() -> dict[str, str]:
    """
    load_config loads an OAuth token from the home directory
    """
    rc = pathlib.Path.home() / CONFIG_FILENAME
    if not rc.exists():
        logging.debug(f"No {CONFIG_FILENAME} found")
        return {}

    config = {}
    with open(rc, "r") as f:
        config["token"] = f.read().strip()
        logging.debug(f"Found token: {config['token']}")
    return config


def format_channel(channel: str) -> str:
    if (
        channel.startswith("https://")
        or channel.startswith("http://")
        or channel.startswith("twitch.tv")
        or channel.startswith("m.twitch.tv")
    ):
        pass
    else:
        channel = "https://www.twitch.tv/" + channel

    return channel


class Player:
    """
    Player loads streamlink and the video player
    """

    @classmethod
    def play(
        cls,
        stream_url: str,
        quality: "Optional[str]" = DEFAULT_QUALITY,
        pip: bool = False,
        oauth_token: "Optional[str]" = None,
    ):
        if not stream_url.startswith("http"):
            raise TypeError(f"invalid stream url {stream_url}")

        logging.info("Opening {} @ {}, pip={}".format(stream_url, quality, pip))

        if pip:
            iina_pip = "--pip"
        else:
            iina_pip = ""

        # Really dumb bug alert: if iina gets passed the filename, `-`, it will crash.
        # streamlink will add the filename if we don't add it to the args, so we add it
        # in a way where it won't be parsed by iina
        cmd = [
            STREAMLINK_PATH,
            "--http-header=Authorization=OAuth {}".format(oauth_token),
            # "--player={}".format(PLAYER_PATH),
            # "--player-args=--stdin {pip} {{filename}}-ignorethis".format(pip=iina_pip),
            stream_url,
            quality
            # Superseded by using oauth token
            #   --twitch-disable-ads \
        ]

        # print(" ".join(cmd))

        player_env = os.environ
        # app2py sets PYTHONPATH, breaking streamlink packages
        # TODO: this may be configurable, see --use-pythonpath in app2py
        if "PYTHONPATH" in player_env:
            del player_env["PYTHONPATH"]
        player_env["PATH"] = "/usr/local/bin"


        # Want to log in realtime
        with subprocess.Popen(
            cmd, env=player_env, stdout=subprocess.PIPE, bufsize=1, text=True
        ) as p:
            for line in p.stdout:
                logging.info(line.removesuffix("\n"))
            p.communicate()
            logging.info(f"Streamlink closed with code {p.returncode}")
