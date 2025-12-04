# Meme Bot 🤖

A Discord bot that sends random memes from Reddit using the [Meme API](https://meme-api.com/gimme).  
This project was my **final project** for the Codedex Python course, where I elaborated on each line of code to fully understand how APIs work and how to interact with Discord servers via Python.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

---

## About

Meme Bot is a fun Discord bot built with Python. It fetches memes from Reddit in real-time using the Meme API and posts them directly to your Discord server.  
This project was inspired by the tutorial by **Hong Jeon** on [Codedex](https://www.codedex.io/projects/build-a-discord-bot-with-python), but I expanded the code by adding detailed comments to understand every part of the API interaction and bot functionality.

---

## Features

- Fetches **random memes** from Reddit using Meme API.
- Posts memes directly into a Discord server channel.
- Fully commented Python code for learning purposes.
- Lightweight and easy to set up.

---

## Installation

1. **Clone the repository**
```
git clone https://github.com/sbcxty/Meme-Bot.git
cd Meme-Bot
```

2. **Install Dependencies**
```
py -3 -m pip install -U discord.py
python3 -m pip install requests
```

3. **Create a Discord bot**
- Go to [Discord Developer Portal](https://discord.com/developers/applications)
- Create a new application and bot
- Copy the bot token
- Enable *Message Content Intent* under Privileged Gateway Intents
- Go to OAuth2, select *bot* under OAuth2 URL Generator, and *Send Messages* under Bot Permissions
- Copy the Generated URL below and paste it on a new tab to invite the bot to your server.

4. **Set your bot token**
- Install python-dotenv
```
pip install python-dotenv
```
- Create a .env file in the project root and input your token:
```
DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE
```
- Run the bot
```
python bot.py
```

---


## Usage
Once the bot is added to your server, type the following command in any text channel where it has permissions:
```
$memes
```

---


## Credits
- [Hong Jeon](https://www.codedex.io/projects/build-a-discord-bot-with-python) - Original tutorial for learning Discord bots with Python.
- [Meme API Repository](https://github.com/D3vd/Meme_Api) - API for fetching random memes from Reddit.
- My own elaboration and detailed comments to fully understand how the bot and API work.

  
***Made with ❤️ by Shekainah Bag-ao***
