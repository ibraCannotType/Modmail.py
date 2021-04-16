# Modmail.py
[![discord](https://discord.com/api/guilds/832430286741700618/embed.png)](https://discord.gg/m7ZbuSP4y8)
[![pypi](https://img.shields.io/pypi/v/discord.py.svg)](https://pypi.org/project/discord.py/)
### Modmail discord bot 


**First thing** you have to install [python](https://www.python.org/downloads/) 

> After that you have to install discord.py lib using pip

``` 
$ pip install discord 
```
After that make a new folder and make a new file and name it ```main.py```
( this is an example code if you wanna try it )

```py
import discord
from discord.ext import commands

client = commands.Bot(commands.when_mentioned_or("!"))
client.remove_command("help")

@client.event #Online event
async def on_ready():
	print("Bot is working!")
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))

@client.command() #Ping
async def ping(ctx):
	await ctx.reply(f"**{round(client.latency *1000)}**ms")


client.run("SECRET_TOKEN") #Token
```

Now you're ready to use the **Modmail** bot !

you can join my [Discord](https://discord.gg/m7ZbuSP4y8) to test it !

Just go to the bot DM's and type ```Lmodmail {message}```
