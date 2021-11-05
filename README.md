# Streampipe

Some tools for opening Twitch streams in native video players

## CLI tool

Start stream in [IINA](https://iina.io) via the command line

**Examples:**
```bash
stream kitboga
stream https://www.twitch.tv/kitboga 720p
```

## StreamPipe.app

Applescript .app to handle `twitch://` urls and load streams in IINA.

**URL Examples:**
```
twitch://open?channel=hasanabi
twitch://open?channel=hasanabi&quality=720p&pip=false
```

Limitations:
- Hardcoded paths in .scpt, including homebrew python
- Janky AF
- Logging in .app is not easily accessible
- TODO: Replace with a Swift app one day...

### Development

Edit AppleScript Shim
```
open StreamPipe.app/Contents/Resources/Scripts/main.scpt
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
