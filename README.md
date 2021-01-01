# Streampipe

Some tools for opening Twitch streams in native video players

## CLI tool

Start stream in IINA via the command line

**Examples:**
```bash
stream kitboga
stream https://www.twitch.tv/kitboga 720p
```

## streampipe.app

MacOS app that handles `twitch://` urls and loads streams in IINA.

**URL Examples:**
```
twitch://open?channel=hasanabi
twitch://open?channel=hasanabi&quality=720p&pip=false
```

### Development

build (alias to current dir)

```
python setup.py py2app -A
```

argv emulation converts url to argv param

testing

```
/Users/hebo/code/streampipe/dist/streampipe.app/Contents/MacOS/streampipe twitch://open?channel=hasanabi
```

run directly
```
python main.py "twitch://open?channel=hasanabi&quality=720p&pip=false"
```


actual run
```
open twitch://open?channel=hasanabi
```


## prod

```
python setup.py py2app --argv-emulation
```

### Logs

Logs are sent to `/var/log/streampipe.log`

```
tail -f /tmp/streampipe.log
```
