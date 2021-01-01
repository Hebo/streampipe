import argparse

from streampipe.player import Player, format_channel, load_config

DEFAULT_QUALITY = "720p"

parser = argparse.ArgumentParser()
parser.add_argument("channel", help="Twitch channel name")
parser.add_argument("quality", help="Video quality", nargs="?", default=DEFAULT_QUALITY)
parser.add_argument(
    "-p", "--pip", help="Open in Picture in Picture mode", action="store_true"
)

def run():
    args = parser.parse_args()
    config = load_config()
    # print(f"Using oauth token {config['token']}")

    stream_url = format_channel(args.channel)

    print("Opening {}".format(stream_url))
    Player.play(stream_url, quality=args.quality, pip=args.pip, oauth_token=config["token"])
