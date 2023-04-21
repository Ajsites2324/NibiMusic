import asyncio
import importlib

from pytgcalls import idle

from NibiMusic import BOT_USERNAME, bot, call_py
from NibiMusic.Modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def NibiX_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("NibiMusic.Modules." + all_module)
    await bot.start()
    await call_py.start()
    await idle()
    print(f"ɢᴏᴏᴅʙʏᴇ ʙʜᴀᴋ ᴍᴀᴅʜᴀʟʜᴏᴅ!\nStopping @{BOT_USERNAME}")
    await bot.stop()


if __name__ == "__main__":
    loop.run_until_complete(NibiX_boot())
