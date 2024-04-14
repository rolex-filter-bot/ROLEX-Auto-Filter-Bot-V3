from pyrogram import Client, filters


API_ID = "28991562"
API_HASH = "215d93eeacd3d1c704887f80b0b914f4"
BOT_TOKEN = "7078618228:AAGTQ7kfJg6UYl69nzFwaK8QRiDDF5Gp9jU"

RolexFilterBot = Client(
    name="ROLEX-Auto-Filter-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
  )


@RolexFilterBot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("HAI 🖐🖐 I AM ROLEX FILTER BOT. THIS IS AN ADVANCED AND POWERFUL BOT")


@RolexFilterBot.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("ADD ME TO YOUR GROUP AS AN ADMIN. I CAN PROVIDE MOVIES FOR YOUR GROUP 👍")


print("Bot was Started")

RolexFilterBot.run() 
