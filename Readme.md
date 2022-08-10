# Bot Pengunduh Lagu

# Bekerja Demo [![image](https://img.shields.io/badge/TELEGRAM-0000FF?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/music_c_down_bot/)

## Daftar Isi
* [Bot apa ini?](#Bot-apa-ini)
* [Pengaturan](#pengaturan)
* [Bugs](#Bugs)
* [My BOT Channel](#My-BOTs-Channel)


## Bot apa ini?

### Pernah Bertanya-tanya bagaimana cara mengunduh lagu dari Spotify atau YouTube?

### BOT ini Dapat membantu Anda mengunduh lagu dari spotify menggunakan <a href = "https://github.com/spotDL/spotify-downloader">spotdl</a>
### This BOT Can help you to download songs from YouTube using <a href = "https://github.com/spotDL/https://github.com/yt-dlp/yt-dlp">yt-dlp</a>
## Setup

### Via Heroku

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/EmiliaTzy/SpotifyDownloader)

### Via VPS atau Lokal

#### Tanpa Docker

```
git clone https://github.com/EmiliaTzy/Spotifydownloader.git
cd spotify-bot

Edit edit_me.py with Details as Follows,

Get you BOT_TOKEN from @BotFather, Required
Get API_ID and API_HASH from my.telegram.org, Required
Edit BOT_TEXT if Required
Get LOG_CHANNEL from Your Channel Settings for Logging, Required
Your MONGODB_URI from your MongoDB Account, Required
SESSION_NAME for Your Collection Name in MongoDB
BOT_OWNER is The User ID of The Developer, Required

sudo pip3 install virtualenv 
virtualenv venv 
source venv/bin/activate
pip3 install -r requirements.txt
python bot.py
```

#### Dengan Docker

```
Edit the config.py with required Details
Build Dockerfile in the Repo
Run The Docker Image
````

## Bugs

####  Ini Saat Ini dalam Tahap Pengembangan, Jadi ada Bug yang saya tidak sadari
####  Jika menemukan bug silahkan hubungi ke <a href="https://t.me/tth_kiya98_bot">Az</a>

## Kumpulan Bot Lainnya
<a href="https://t.me/eiko_support">Eiko BOT</a>
