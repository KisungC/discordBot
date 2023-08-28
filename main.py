import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import ai

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
            #read the user uploaded file
            content = await attachment.read(use_cached=False)
            if content:
                print ("successfully read the document ", content)
            else:
                print("error - failed to retrieve the document")
                await userMessage.channel.send("Something went wrong, couldn't read the message that you uploaded. .txt file works the best.")
                return
            
            #have ai look over the content
            await userMessage.channel.send('Ask me anything based on the documentation that you have uploaded!')

            def check(msg, user_message=userMessage):
                return msg.author == user_message.author and msg.channel==user_message.channel
            
        try:
            question = await client.wait_for("message", check=check)
            user_question = question.content  # Extract the user's question from the message
            print(user_question)

            aiAnswer = ai.send_data_ai(content, user_question)
            await userMessage.channel.send(aiAnswer)
        except asyncio.TimeoutError:
            await userMessage.channel.send("You took too long to ask a question.")


# def send_question_to_ai(question):
# pass in the question from the user input, export/import from ai.py.

client.run(os.getenv('TOKEN'))

