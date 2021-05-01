import discord
import asyncio
from discord.ext import commands

client = commands.Bot(commands.when_mentioned_or("!"))
client.remove_command("help")

# On_ready event

@client.event
async def on_ready():
	print("Bot is working!")
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Mails!")) #Custom status

# Ping command

@client.command()
async def ping(ctx):
    embed = discord.Embed(description=f"Pong! **{round(client.latency *1000)}**ms" ,color=0x8CFED8)
    await ctx.reply(embed=embed)

# Modmail command

@client.command()
async def modmail(ctx, *, message=None):
   author = ctx.author
   if message == None:
      return await ctx.reply('> Please type things to send this mail to the staff!')
   if isinstance(ctx.channel, discord.channel.DMChannel):
     channel = client.get_channel(CHANNEL_ID)
     embed = discord.Embed(title=f"We found a new mail! 📧" ,description=f"**{message}**" ,color=0x8CFED8)
     embed.set_footer(text=f"{author}")
     embed.set_thumbnail(url=f"{author.avatar_url}")
     await channel.send(embed=embed)
   else:
     return await ctx.reply("> Sorry but this command only works on my dm :)")

# Modmail responde

@client.command()
@commands.has_permissions(administrator=True) # Premission #
async def responde(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(f"**{ctx.message.author} Responded =>** {content}")


# Token

client.run("SECRET_TOKEN")
