from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app
from config import BOT_USERNAME

start_txt = """
❖ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ.

● ɪ ᴀᴍ ➥ 𝐒ᴏʜɪɴɪ ♡ ᴍᴜsɪᴄ ʙᴏᴛ.

❖ ɪғ ʏᴏᴜ ᴡᴀɴᴛ 𝐒ᴏʜɪɴɪ ♡ ᴍᴜsɪᴄ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("𝐒ᴜᴘᴘᴏʀᴛ🌱", url="https://t.me/TheBongFamily_Chatt"),
          InlineKeyboardButton("𝐑ᴇᴘᴏ⛈️", url="https://github.com/ShubhoEditx/SohiniMusicXPro")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/245f55c3ae09d24bcebdc.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

