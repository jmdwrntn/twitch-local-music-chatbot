# Twitch Local Music Chatbot

## Description

Twitch chatbot made in Python, based on this [tutorial](https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8), that responds to a !song command by reading a local text file exported from your music player of choice.

Originally created to work with the MusicBee plugin [Now Playing to External Files](https://www.getmusicbee.com/addons/plugins/47/now-playing-to-external-files/), though it would likely work plugins for other players such as [Snip](https://github.com/dlrudie/Snip/), [Tuna](https://obsproject.com/forum/resources/tuna.843/), [NowPlaying](https://github.com/jakobbsm/NowPlaying) etc. These have not been tested and some configuration of the bot and the plugin outputs may be required.

## Installation

* Install Python 3
* Clone this repo
* Install using either:
    * Install from requirements (```pip install -r requirements.txt```)
    * Install with pipenv (```pipenv install```)

## Requirements

* Request an [OAuth Token](https://twitchapps.com/tmi/)
* Register your app with [Twitch Developers](https://dev.twitch.tv/console/apps/create) and request a client ID.
* Have a spare or create a new Twitch account **for your bot** to use
* Install music player plugin of choice

## Configuration

* Open *.env.example* and paste the OAuth Token, Twitch Developer client ID and Twitch bot account into the relavant line
* It is recommended to keep the box command prefix as '!'
* Find and add the local address of the music player plugin text file output
* Rename *.env.example* to **.env**, save and close file
