"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup, find_packages


APP = ["main.py"]
DATA_FILES = []
OPTIONS = {
    "packages": find_packages(),
    "plist": dict(
        #   CFBundleName="Shelf",
        #   NSMainNibFile="MainMenu",
        #   NSPrincipalClass='PyShelfApplication',
        #   CFBundleIdentifier="org.jerakeen.pyshelf", # historical
        #   CFBundleShortVersionString=version,
        #   CFBundleVersion=version,
        #   NSHumanReadableCopyright="Copyright 2008 Tom Insam",
        #   NSAppleScriptEnabled=True,
        CFBundleURLTypes=[
            dict(
                CFBundleURLName="Twitch callback",
                CFBundleURLSchemes=["twitch"],
            )
        ],
    ),
    "iconfile": "icon.icns",
    "argv_emulation": 1,
}


setup(
    name="streampipe",
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
