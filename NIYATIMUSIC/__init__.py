from NIYATIMUSIC.core.bot import NIYATI
from NIYATIMUSIC.core.dir import dirr
from NIYATIMUSIC.core.git import git
from NIYATIMUSIC.core.userbot import Userbot
from NIYATIMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = NIYATI()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "ll_DRAGON_MUSIC_BOT"  # connect music api key "Dont change it"