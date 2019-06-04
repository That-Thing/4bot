import discord
from discord.ext import commands
from discord.ext.commands import Bot
import basc_py4chan
import datetime
import random
import time
class chan:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    #@commands.cooldown(rate=1, per=2.0) #command cooldown. If you are going to use this in an actual server I suggest enabling it to reduce spam.
    async def randthread(self, *args):
        output = ""
        for word in args:
            output += word
            board = basc_py4chan.Board(output, https=False, session=None)
            thread_ids = board.get_all_thread_ids()
            str_thread_ids = [str(id) for id in thread_ids]
            randid = random.choice(str_thread_ids)
            thread = board.get_thread(randid)
            embed=discord.Embed(description="Board: "+"/"+output+"/")
            embed.add_field(name="Url", value=thread.url)
            embed.add_field(name="Replies",value=len(thread.replies), inline=False)
            await self.bot.say(embed=embed)

            for post in thread.posts:#a seperate embed for every single post because discord doesn't allow multiple images in an embed. 
        
                embed=discord.Embed(description="Post")
                embed.add_field(name="No.", value=post.post_id, inline=False)#this shit is so fucking annoying
                embed.add_field(name="Tripcode:", value=post.tripcode, inline=False)
                embed.add_field(name="Datetime:", value=post.datetime, inline=False) 
                embed.add_field(name="Name:", value=post.name, inline=True)
                embed.add_field(name="Subject:", value=post.subject, inline=True)
                embed.add_field(name="Comment: ",value=post.text_comment, inline=False)
                if post.has_file==True: #There is probably a better way of doing this, but I don't give a fuck. 
                    embed.set_image(url=post.file_url)
                    await self.bot.say(embed=embed)
                else:
                    await self.bot.say(embed=embed)
                time.sleep(1)   #Uncomment if you don't want the bot spamming the channel and completely destroying your notifications (it still will but at a slower pace)
            

    @commands.command()
    async def thread(self, *argv):
        boardid = ""
        threadid=""
        boardid += argv[0]
        threadid += argv[1]



        board = basc_py4chan.Board(boardid, https=False, session=None)
        thread = board.get_thread(threadid)
        embed=discord.Embed(description="Board: "+"/"+boardid+"/")
        embed.add_field(name="Url", value=thread.url)
        embed.add_field(name="Replies",value=len(thread.replies), inline=False)
        await self.bot.say(embed=embed)

        for post in thread.posts:
        
            embed=discord.Embed(description="Post")
            embed.add_field(name="No.", value=post.post_id, inline=False)
            embed.add_field(name="Tripcode:", value=post.tripcode, inline=False)
            embed.add_field(name="Datetime:", value=post.datetime, inline=False) 
            embed.add_field(name="Name:", value=post.name, inline=True)
            embed.add_field(name="Subject:", value=post.subject, inline=True)
            embed.add_field(name="Comment: ",value=post.text_comment, inline=False)
            if post.has_file==True:
                embed.set_image(url=post.file_url)
                await self.bot.say(embed=embed)
            else:
                await self.bot.say(embed=embed)
            time.sleep(1)  









def setup(bot):
    bot.add_cog(chan(bot))