# © Cyril C Thomas
# https://t.me/cyril_c_10

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Song.database.access_db import db
import shutil
import psutil

#-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*#
def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2 ** 10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

#-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*#

async def start(bot, update):
        await update.reply_text(
            text=f"Hai yang disana, {update.from_user.mention} \n\nsaya dapat mengunduh <b>Lagu Spotify</b> dan mengirimnya kembali ke kamu\n\nKirimkan saya sebuah link untuk diunggah......\n\n\nDibuat oleh ❤️ @eiko_support",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
                            [[
                                InlineKeyboardButton(
                                    "Support Channel", url="https://t.me/eiko_support"),
                                InlineKeyboardButton(
                                    "Developer", url="https://t.me/tth_kiya98_bot")
                                ]]
                            ),
            disable_web_page_preview=True,
            parse_mode="html")



async def helper(bot, update):
        await update.reply_text(
            text=f"Kirimkan sebuah tautan lagu\n\nMengunduh lagu\n\nKirim sebagai file musik untukmu\n\nTidak semua file musik bisa diunduh, So Please be Patient\n\nFeel Free to Conatct me If you Spot any Bugs\n\n\nDibuat Oleh ❤️ @eiko_support",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
                            [[
                                InlineKeyboardButton(
                                    "Support Channel", url="https://t.me/eiko_support"),
                                InlineKeyboardButton(
                                    "Developer", url="https://t.me/tth_kiya98_bot")
                                ]]
                            ),
            disable_web_page_preview=True,
            parse_mode="html")


async def status(bot, update):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await update.reply_text(
        text=f"**Total ruang disk:** {total} \n**Penggunaan ruang:** {used}({disk_usage}%) \n**Ruang kosong:** {free} \n**Penggunaan CPU:** {cpu_usage}% \n**Penggunaan RAM:** {ram_usage}%\n\n**Total Pengguna di DB:** `{total_users}`",
        parse_mode="Markdown",
        quote=True
    )

