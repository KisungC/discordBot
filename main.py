import discord
import os
import requests
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(userMessage):
    if userMessage.author == client.user:
        return
    
    if userMessage.content.startswith('!hello'):
        await userMessage.channel.send('hi')

    if userMessage.content.startswith('!upload'):
        await userMessage.channel.send('choose file(s) to upload for chatgpt to help you')

    if userMessage.attachments:
        for attachment in userMessage.attachments:
            global global_content
            content = await attachment.read(use_cached=False)
            global_content = content
            print ("successfully read the document ", global_content)
            await userMessage.channel.send('how can I help you?')

    else:
        await userMessage.channel.send('Command not listed, type !help for command list')

# def send_content_to_ai(content):
# pass in content, export/import from ai.py.

# def send_question_to_ai(question):
# pass in the question from the user input, export/import from ai.py.

client.run(os.getenv('TOKEN'))

