# terminal-media-player
Play videos in ascii art in the terminal!

**(still) only work in linux**
## External dependencies


 - ffmpeg
 
so, install **ffmpeg** in your SO and add it to environment variables.

## How to install
    * git clone
    * cd to repo
    * pipenv install
    * pipenv shell (to start the virtual environment)


## How to use
in youtube:

    python tmplayer.py link/to/youtube/video --youtube

in files:

    python tmplayer.py path/to/file --file

in absolute video urls, just give the link:

    python tmplayer.py url/to/video


In alpha, enjoy!
