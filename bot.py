import discord
import responses
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_CAIUS_BOT_TOKEN')
print("Token from .env:", TOKEN)

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        # Check if the message starts with a specific command prefix
        if user_message.lower().startswith('c!'):
            user_message = user_message[2:]
            await send_message(message, user_message, is_private=False)
        elif user_message.lower().startswith('c?'):
            user_message = user_message[2:]
            await send_message(message, user_message, is_private=True)

    client.run(TOKEN)

run_discord_bot()
