import discord
from discord.ext import commands

class Testing:
    '''
    Making sure things actually work using one handy module
    '''
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command(pass_context="True",brief="PING!")
    async def ping(self, ctx):
        """
        PONG.
        """
        embed = discord.Embed(title='Pong!', description='The bot is up and running!', color=0x000)
        embed.set_thumbnail(url='http://play.egames.com/img/console/atari-pong-game-screen.jpg')
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Testing(bot))