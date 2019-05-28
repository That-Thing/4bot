#########################################
import discord                         ##Stupid
from discord.ext import commands       ##Discord
from discord.ext.commands import Bot   ##Shit
#########################################
import asyncio
import os 
import random
import requests
#################################################################
##                                                             ##
##      DO NOT USE THIS BOT IN AN ACTUAL SERVER, IT SPAMS      ##
##                                                             ##
#################################################################

#bot prefix
bot = commands.Bot(command_prefix = '4!')
bot.remove_command('help')#I don't even know if this is nessecarry but I do it anyways because I saw it on the internet
 


extentions = [
'ping',  
"help",
"chan"
]

 
print("Starting Bot")#Itoddlers please get the fuck out.

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    await bot.change_presence(game=discord.Game(name='Based and Redpilled | $help', url='https://www.twitch.tv/monstercat',type=1))
    print("                         .-. .-.")
    print("                        (   |   )")
    print('                      .-.:  |  ;,-.')
    print("                     (_ __`.|.'__ _)")
    print("                     (    .'|`.    )")
    print("                      `-'/  |  \`-'")
    print("                        (   !   )")
    print("                         `-' `-'")
    print("")
#every project has to have a cool ascii thing in the terminal or it is considered a disgrace

@bot.command(pass_context=True)
async def cls(ctx):#I still have yet to figure out what the keyboard shortcut for clearing the console is on windows. 
    if ctx.message.author.id == 'Bot owner ID':
        await bot.say("**Console cleared!**")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("clear")



#basic cog unloading/reloading/loading/whatever the fuck
@bot.command(hidden=True, pass_context=True)
async def load(ctx, extension):
    """Loads a module."""
    if ctx.message.author.id == 'Bot owner ID':
        try:
            bot.load_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Loaded', color=random.choice(colors))
            embed.add_field(name='Loaded', value='Loaded {}'.format(extension))
            await bot.say(embed=embed)
        except Exception as error:
            print("{} Can't be fucking loaded. [{}]".format(extension, error))

@bot.command(hidden=True, pass_context=True)
async def unload(ctx, extension):
    """Unloads a module."""
    if ctx.message.author.id == 'Bot owner ID':
        try:
            bot.unload_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Unloaded', color=random.choice(colors))
            embed.add_field(name='Unloaded', value='Unloaded {}'.format(extension))
            await bot.say(embed=embed)
        except Exception as error:
            print("{} Can't be fucking unloaded. [{}]".format(extension, error))

@bot.command(hidden=True, pass_context=True)
async def reload(ctx, extension):
    """Reloads a module."""
    if ctx.message.author.id == 'Bot owner ID':
        try:

            bot.unload_extension(extention)
            bot.load_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Reloaded', color=random.choice(colors))
            embed.add_field(name='Reloaded', value='Reloaded {}'.format(extension))
            await bot.say(embed=embed)
        except Exception as error:
            print("{} Can't be fucking reloaded. [{}]".format(extension, error))





if __name__ == "__main__":
    for extention in extentions:
        try:
            bot.load_extension(extention)
        except Exception as error:
            print("{} couldn't be loaded, something fucked up! [{}]".format(extention, error))



#put your token here
bot.run('Token')