import discord
from dotenv import load_dotenv
import os
import requests
import json

# Function that allows the bot to send memes through the Meme API.
def get_meme():
    # requests package makes an HTTP request to the URL using the GET method and returns an instance of the Response class (specified within the requests package), named as response, an object, which contains attributes such as text (the body of the response as a string, in this case JSON), headers (response metadata), and status code (HTTP status code).
    response = requests.get('https://meme-api.com/gimme')
    # json package reads response and converts it into a dictionary, so that it is usable by Python.
    # response.text is a json data format from response object. json is essentially a string formatted like dictionaries/objects.
    # json.loads converts json into dictionary, so that we can access the key-value pairs and retrieve the url link. 
    json_data = json.loads(response.text)
    return json_data['url']

# Child class of discord.Client(parent) with all its properties. Allows for customization of the parent class.
class MyClient(discord.Client):
    # when bot successfully logged in, print the message, but code continues even while waiting for it to log in. Bot listens to events while this line runs in the background
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    # Async function that overrides the on_message event from the Client class.
    # This runs automatically whenever a new message is received in a server
    # where the bot has access, unless the message is sent by the bot itself.
    async def on_message(self, message):
        
        # 'message' is an instance of the Message class from discord.py.
        # It is automatically created when a new message is detected.
        if message.author == self.user:
            return

        # 'await' pauses only this coroutine while the message is being sent,
        # allowing the bot to continue handling other events at the same time.
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

    

# create an instance/object of the discord.Intents class with default attributes as defined by default() method
intents = discord.Intents.default() 
intents.message_content = True

# create an instance/object of the MyClient class and assign the intents object created earlier to the intents parameter from the __init__ constructor of Client class. Allows the bot to listen to message events
# constructor is a special method of a class that runs automatically when an object is created. It assigns initial values to the object’s properties and can accept parameters to set those values.
# after creating the client object, aka our live bot, it starts the bot using the run method inherited from the Client class. It connects the the bot to Discord's backend using the provided token, allowing the bot to listen for events, specifically messages.
client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))

