#-----------------------------------------
#|--------------- Mod Mail ---------------
#| -----This Code Made By Vibin'#5404-----
#| Thx for : Glowstikk#5127 for helping !
#|--------------- Mod Mail ---------------
#-----------------------------------------

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
    embed.set_author(name="ModMail", icon_url="https://cdn.discordapp.com/attachments/832430398377689159/832574187180261396/Lmail.png")
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
     embed.set_author(name="ModMail", icon_url="https://cdn.discordapp.com/attachments/832430398377689159/832574187180261396/Lmail.png")
     embed.set_footer(text=f"{author}")
     embed.set_thumbnail(url=f"{author.avatar_url}")
     await channel.send(embed=embed)
   else:
     return await ctx.reply("> Don't be an idiot and type this command in DM")

# Modmail responde

@client.command()
@commands.has_permissions(administrator=True)
async def responde(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(f"**{ctx.message.author} Responded =>** {content}")


# Modmail unknown responde

@client.command()
@commands.has_permissions(administrator=True)
async def unknown_res(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(f"**Staff Responded =>** {content}")


# Token

client.run("SECRET_TOKEN")
