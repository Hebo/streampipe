from streampipe import player
import pytest

@pytest.mark.parametrize("channel,expected", [
    ("hasanabi", "https://www.twitch.tv/hasanabi"),
    ("http://twitch.tv/hasanabi", "http://twitch.tv/hasanabi"),
    ("https://twitch.tv/hasanabi", "https://twitch.tv/hasanabi"),
    ("http://m.twitch.tv/hasanabi", "http://m.twitch.tv/hasanabi"),
    ("twitch.tv/hasanabi", "twitch.tv/hasanabi"),
])
def test_format_channel(channel, expected):
    got = player.format_channel(channel)
    print(got)
    assert got == expected
