from datetime import datetime

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from NibiMusic import BOT_NAME, BOT_USERNAME, F_OWNER
from NibiMusic import bot as Nirjon
from NibiMusic.config import GROUP_SUPPORT, UPDATES_CHANNEL

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("ᴡᴇᴇᴋs", 60 * 60 * 24 * 7),
    ("ᴅᴀʏ", 60**2 * 24),
    ("ʜᴏᴜʀ", 60**2),
    ("ᴍɪɴ", 60),
    ("sᴇᴄ", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Nirjon.on_message(filters.command([f"ping@{BOT_USERNAME}", "ping"]) & filters.group)
async def start(client: Nirjon, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✔ **ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ**\n<b>☣ **ᴜᴘᴛɪᴍᴇ:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 ɢʀᴏᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🏡 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ]
            ]
        ),
    )


@Nirjon.on_message(filters.command(["start", "help", "ajeet", "iloveyou"]) & ~filters.group)
async def start(_, message: Message):
    await message.reply_text(
        f"""ʜᴇʏ {message.from_user.mention()}, 
       
  ᴍʏ ɴᴀᴍᴇ ɪs {BOT_NAME}.
๏ ᴀ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴍᴀɴʏ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴏᴡɴᴇᴅ ʙʏ @PAPA_BOL_SAKTEHO .. 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🥵ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ🥵",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    ),
                ],
                [
                    InlineKeyboardButton(text="❄ ʜᴇʟᴩ ❄", callback_data="cbbasic"),
                    InlineKeyboardButton(text="🥀ʙᴏᴛ ᴋᴇ ᴘᴀᴘᴀ🥀", user_id=F_OWNER),
                ],
                [
                    InlineKeyboardButton(
                        text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        text="💘 ᴄʜᴀɴɴᴇʟ 💘", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="☁ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ☁",
                        url="https://telegra.ph/file/9e2e4ef384a59ae92d4ea.mp4",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Nirjon.on_message(filters.command(["repo", "source", "ajeetpapa", "pampabol"]))
async def help(client: Nirjon, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/56557bd94afbe895ae483.jpg",
        caption=f"""ʜᴇʀᴇ ɪs ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ғᴏʀᴋ ᴀɴᴅ ɢɪᴠᴇ sᴛᴀʀs ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://github.com/Ajsites2324/NibiMusic"
                    )
                ]
            ]
        ),
    )
