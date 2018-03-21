import discord
from discord.ext import commands
import datetime
import time

class Testing:
    '''
    Making sure things actually work using one handy module
    '''
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """
        PONG.
        """
        msgtime = ctx.message.timestamp.now()
        await (await self.bot.ws.ping())
        now = datetime.datetime.now()
        ping = now - msgtime
        pong = discord.Embed(title='Pong! Response Time:', description=str(ping.microseconds / 1000.0) + ' ms',
                             color=0x00FF99)
        pong.set_thumbnail(url='http://odysseedupixel.fr/wp-content/gallery/pong/pong.jpg')
        await self.bot.say(embed=pong)

def setup(bot):
    bot.add_cog(Testing(bot))