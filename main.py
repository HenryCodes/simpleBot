import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = '-')

# Initialisation of the bot.

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Try -help"))
    print('I have woken!')

# End of Initialisation.

#Start of Ping

@client.command()
async def ping(ctx):
    'Pings simpleBot'
    embed=discord.Embed(title="Pong! 🏓", description=f"This message took {client.latency * 1000}ms", color=0x0080c0)
    await ctx.send(embed=embed)

# End of ping.


client.run('Your bot token goes in here!')
