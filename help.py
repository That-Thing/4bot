import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random



class help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
        )


        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

        embed = discord.Embed(title="Commands", colour=random.choice(colors))
        embed.set_author(name='4bot Commands')
        embed.add_field(name='4!ping', value='Sends a image from the subreddit', inline=False)
        embed.add_field(name='4!randthread *board*', value='Gets an entire post from a subreddit', inline=False)
        await self.bot.send_message(author, embed=embed)








def setup(bot):
    bot.add_cog(help(bot))