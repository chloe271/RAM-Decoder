import datetime, asyncio
from prettytable import PrettyTable
from discord.ext import commands
import discord, os, requests, os, keep_alive
from helperfunction.all import *
from helperfunction.micron import *
from helperfunction.corsair import *
from helperfunction.gskill import *
from helperfunction.patriot import *

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!", help_command=None)

@bot.event
async def on_ready() -> None:
    print(f"Bot {bot.user} launched.")

'''@bot.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed(title=f"Error", description=f"Command not found.", color=ctx.author.color) 
        msg = await ctx.send(embed=em)
        await asyncio.sleep(5)
        await msg.delete()'''
        


@bot.command()
async def fbga(ctx, fbga):
  partnumber = (micron(fbga))
  embed=discord.Embed(title=fbga.upper(), url=f"https://www.micron.com/support/tools-and-utilities/fbga?fbga={fbga}",  description=partnumber, color=0xadd8e6)
  embed.set_thumbnail(url=f"https://upload.wikimedia.org/wikipedia/de/thumb/0/03/Micron_Logo.svg/1200px-Micron_Logo.svg.png")
  try:
    embed.add_field(name=f"Rev {revision(partnumber)}", value=f"{version(partnumber)}", inline=True)
  except: pass
  try:
    embed.add_field(name=f"{density(partnumber)}", value=f"{modtype(partnumber)}", inline=True)
  except: pass
  try:
    embed.add_field(name=f"{voltage(partnumber)}", value=f"{misc(partnumber)}", inline=True)
  except: pass
  try:
    embed.set_footer(text="_exa")
  except: pass
  embed.timestamp = datetime.datetime.utcnow()
  await ctx.reply(embed=embed)
  table = PrettyTable(["Attribute", partnumber])
  table.add_row(["Revision", revision(partnumber)])
  table.add_row(["Configuration", density(partnumber)])
  table.add_row(["DDR Version", version(partnumber)])
  await ctx.reply(table)
  
@bot.command()
async def corsair(ctx, *, vers):
  code = (clean(vers))
  corsairvers = f"v{code[:1]}.{code[1:]}"
  embed=discord.Embed(title=corsairvers, description="⠀", color=0xc08080)
  embed.set_thumbnail(url=f"{image(manu(code))}")
  embed.add_field(name=f"{manu(code)}", value=f"{dens(code)} Gbit", inline=True)
  embed.add_field(name=f"{rev(code)}-Die", value="⠀", inline=True)
  if check(code) is not None:
    embed.add_field(name=f"Note", value=f"{check(code)}", inline=False)
  embed.set_footer(text="_exa")
  embed.timestamp = datetime.datetime.utcnow()
  await ctx.reply(embed=embed)


@bot.command()
async def gskill(ctx, *, code):
  o42 = code.upper()
  gskillvers = o42[-5:]
  embed=discord.Embed(title=gskillvers, description=f"{ddr(o42)}", color=0xc08080)
  embed.set_thumbnail(url=f"{image(gskill_manuf(o42))}")
  embed.add_field(name=f"{gskill_manuf(o42)}", value=f"{die_density(o42)} Gbit", inline=True)
  embed.add_field(name=f"{die_revision(o42)}-Die", value=f"{GK_die_organisation(o42)}", inline=True)
  embed.set_footer(text="_exa")
  embed.timestamp = datetime.datetime.utcnow()
  await ctx.reply(embed=embed)

@bot.command()
async def patriot(ctx, *, patriot_code):
  pat = patriot_code.upper()
  embed=discord.Embed(title=pat, description=f"⠀", color=0xc08080)
  embed.set_thumbnail(url=f"{image(patriot_ddr_manufacturer(pat))}")
  embed.add_field(name=f"{patriot_ddr_manufacturer(pat)}", value=f"{patriot_die_density(pat)} Gbit", inline=True)
  embed.add_field(name=f"{patriot_die_revision(pat)}-Die", value=f"⠀", inline=True)
  embed.set_footer(text="_exa")
  embed.timestamp = datetime.datetime.utcnow()
  await ctx.reply(embed=embed)
  



@bot.command()
async def help(ctx):  
  embed=discord.Embed(title="Help menu", description="This bot should allow you determine which IC depending on label or IC markings.", color=0xc08080)
  embed.add_field(name="Micron FBGA", value="!help_fbga", inline=True)
  embed.add_field(name="Corsair", value="!help_corsair", inline=True)
  embed.add_field(name="Gskill", value="!help_gskill", inline=True)
  embed.add_field(name="Patriot", value="!help_patriot", inline=True)
  embed.set_footer(text="_exa")
  embed.timestamp = datetime.datetime.utcnow()
  await ctx.reply(embed=embed)

@bot.command()
async def help_corsair(ctx):  
  embed=discord.Embed(title="Corsair", description="Use the version number on the white sticker on the side here.\nUse the format `!corsair v4.31`", color=0xc08080)
  embed.set_image(url="https://i.imgur.com/Oc40csh.png")
  embed.set_footer(text="_exa")
  embed.timestamp = datetime.datetime.utcnow()
  await ctx.reply(embed=embed)


@bot.command()
async def help_fbga(ctx):  
  embed=discord.Embed(title="Micron FBGA", description="Use the 5 letter code on a Micron IC using the format\n`!fbga c9blm`", color=0xc08080)
  embed.set_image(url="https://i.imgur.com/9d67nJs.png")
  embed.set_footer(text="_exa")
  embed.timestamp = datetime.datetime.utcnow()
  await ctx.reply(embed=embed)

@bot.command()
async def help_gskill(ctx):  
  embed=discord.Embed(title="G.Skill", description="Use the 042 code on the white sticker on the side here.\nUse the format `!gskill 04266X8820C`", color=0xc08080)
  embed.set_image(url="https://i.imgur.com/cyJMIqR.png")
  embed.set_footer(text="_exa")
  embed.timestamp = datetime.datetime.utcnow()
  await ctx.reply(embed=embed)

@bot.command()
async def help_patriot(ctx):  
  embed=discord.Embed(title="Patriot", description="Use the code to the right of the barcode \nUse the format `!patriot 11EC`", color=0xc08080)
  embed.set_image(url="https://i.imgur.com/F5DDkyv.png")
  embed.set_footer(text="_exa")
  embed.timestamp = datetime.datetime.utcnow()
  await ctx.reply(embed=embed)



keep_alive.keep_alive()
bot.run(os.environ['DISCORD_BOT_SECRET'])