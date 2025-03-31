import os
import discord
from discord.ext import tasks, commands
from datetime import datetime, time

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

bot = commands.Bot(command_prefix="!")

async def send_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Hello! This is your daily message at 18:00.")

@tasks.loop(minutes=1)
async def daily_message():
    now = datetime.now()
    if now.hour == 18 and now.minute == 0:
        await send_message()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    daily_message.start()

bot.run(TOKEN)
