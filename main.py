import requests
import telebot
from telebot import types
#YOUR BOT TOKEN GOES HERE.
bottoken = "706896447316:FUTF4HG_HBDHnGHIN_VJdyi"
bot = telebot.TeleBot(bottoken)
@bot.message_handler(commands=['start','help'])
def send_help_message(message):
    startmess = """
Hello there, 
I am a telegram bot to get you music lyrics.
to use type /lyrics followed by the song name.
eg:
    /lyrics Buruklyn Boyz Dream ya Kutoka kwa Block.
enjoy
    """
    keyboard = types.InlineKeyboardMarkup()
    helpbutt = types.InlineKeyboardButton("HELP", url="https://t.me/EscaliBud")
    channelbutt = types.InlineKeyboardButton("CHANNEL", url="https://t.me/+eVD8089l-U82Nzhk")
    keyboard.add(helpbutt, channelbutt)
    bot.send_message(message.chat.id, startmess, reply_markup=keyboard)
@bot.message_handler(commands=['lyrics'])
def search_lyrics(message):
    fname = message.from_user.first_name
    texto = message.text
    lyric = texto.split("/lyrics", maxsplit=1)
    lyricc = lyric[-1]
    if lyricc ==" ":
        bot.send_message(message.chat.id, "I Need a song to search for its lyrics.\n\nTry /lyrics Buruklyn Boyz Dream ya kutoka kwa block.")
    else:
        try:
            url = f"https://lyrist.vercel.app/api/{lyricc}"
            res = requests.get(url)
            res_json = res.json()
            lyrics = res_json.get("lyrics")
            title = res_json.get("title")
            artist = res_json.get("artist")
            logo = res_json.get("image")
            bot.send_photo(message.chat.id, photo=logo, caption=f"""
Lyrics Requested By : {fname}
Song Title: {title}
Artist: {artist}
            """)
            bot.send_message(message.chat.id, f"""
LYRICS:
```
{lyrics}
```
""")
        except Exception as e:
            print(e)
bot.infinity_polling()
