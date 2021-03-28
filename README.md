# Streampipe

Some tools for opening Twitch streams in native video players

## CLI tool

Start stream in [IINA](https://iina.io) via the command line

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
Build for development (.app aliased to dev source files)

```
make build
```

Testing
```
./dist/streampipe.app/Contents/MacOS/streampipe twitch://open?channel=hasanabi
```

Run directly
```
python main.py "twitch://open?channel=hasanabi&quality=720p&pip=false"
```

Run via URL handler
```
open twitch://open?channel=hasanabi
```


### Building App

Need to make sure Python is installed with frameworks:

```
env PYTHON_CONFIGURE_OPTS="--enable-framework" asdf install python
```


To build the self-contained streampipe.app

```
make build-prod
```

### Logs

Logs for `streampipe.app` are sent to `~/Library/Logs/streampipe.log`. Logs for `stream` cli app are only sent to the console.

```
tail -f ~/Library/Logs/streampipe.log
```
