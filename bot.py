import discord
from dotenv import load_dotenv
import os

# create a child class of discord.Client(parent) with all its properties. Allows for customization of the parent class.
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
        if message.content.startswith('$hello'):
            await message.channel.send("Hello, World!")

    

# create an instance/object of the discord.Intents class with default attributes as defined by default() method
intents = discord.Intents.default() 
intents.message_content = True

# create an instance/object of the MyClient class and assign the intents object created earlier to the intents parameter from the __init__ constructor of Client class. Allows the bot to listen to message events
# constructor is a special method of a class that runs automatically when an object is created. It assigns initial values to the object’s properties and can accept parameters to set those values.
# after creating the client object, aka our live bot, it starts the bot using the run method inherited from the Client class. It connects the the bot to Discord's backend using the provided token, allowing the bot to listen for events, specifically messages.
client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))
