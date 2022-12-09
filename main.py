import requests, re, os, time

import datetime, asyncio
from discord.ext import commands
import discord, os, requests, os, keep_alive

from bs4 import BeautifulSoup
from prettytable import PrettyTable
from functions.micron import *
from functions.corsair import *
from functions.gskill import *
from functions.all import *

bot = commands.Bot(intents=discord.Intents.all(),
                   command_prefix=".",
                   help_command=None)


@bot.event
async def on_ready() -> None:
  print(f"Bot {bot.user} launched.")


def micron(code):
  partnum = code
  code = str(decode(code))
  embed = discord.Embed(
    title=f"{partnum.upper()}",
    url=
    f"https://www.micron.com/support/tools-and-utilities/fbga?fbga={partnum}",
    description=f"{code}",
    color=0xadd8e6)
  embed.set_thumbnail(
    url=
    f"https://upload.wikimedia.org/wikipedia/de/thumb/0/03/Micron_Logo.svg/1200px-Micron_Logo.svg.png"
  )
  try:
    embed.add_field(name=f"Rev {code.split(':')[1]}",
                    value=f"{version(code)}",
                    inline=True)
  except:
    pass
  try:
    embed.add_field(name=f"{density(code)}", value=f"⠀", inline=True)
  except:
    pass
  try:
    embed.set_footer(text="_exa")
  except:
    pass
  embed.timestamp = datetime.datetime.utcnow()

  return embed


def corsair(code):
  partnum = (clean(code))

  corsairvers = f"v{partnum[:1]}.{partnum[1:]}"
  embed = discord.Embed(title=corsairvers, description="⠀", color=0xc08080)
  embed.set_thumbnail(url=f"{image(manu(partnum))}")
  embed.add_field(name=f"{manu(partnum)}",
                  value=f"{dens(partnum)} Gbit",
                  inline=True)
  embed.add_field(name=f"{rev(partnum)}-Die", value="⠀", inline=True)
  if check(partnum) is not None:
    embed.add_field(name=f"Note", value=f"{check(partnum)}", inline=False)
  embed.set_footer(text="_exa")
  embed.timestamp = datetime.datetime.utcnow()

  return embed


def gskill(code):
  o42 = code.upper()
  gskillvers = o42[-5:]
  embed = discord.Embed(title=gskillvers,
                        description=f"{ddr(o42)}",
                        color=0xc08080)
  embed.set_thumbnail(url=f"{image(gskill_manuf(o42))}")
  embed.add_field(name=f"{gskill_manuf(o42)}",
                  value=f"{die_density(o42)} Gbit",
                  inline=True)
  embed.add_field(name=f"{die_revision(o42)}-Die",
                  value=f"{GK_die_organisation(o42)}",
                  inline=True)
  embed.set_footer(text="_exa")
  embed.timestamp = datetime.datetime.utcnow()

  return embed


def sort(code):
  try:
    partnum = (clean(code))
    if len(partnum) == 3:
      return corsair(code)
    if len(partnum) == 1:
      return micron(code)
    else:
      return gskill(code)
  except:
    print("Error please double check format")
    pass


@bot.command()
async def code(ctx, *, code):
  if len(code) > 11:
    await ctx.reply("Error please double check format")
    main()
  else:
    try:
      await ctx.reply(embed=sort(code))
    except:
      print(sort(code))


@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    em = discord.Embed(title=f"Error",
                       description=f"Command not found.",
                       color=ctx.author.color)
    msg = await ctx.reply(embed=em)
    await asyncio.sleep(5)
    await msg.delete()


keep_alive.keep_alive()
bot.run(os.environ['DISCORD_BOT_SECRET'])
