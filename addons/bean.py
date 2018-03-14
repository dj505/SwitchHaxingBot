import discord
from discord.ext import commands

class Bean:
    '''
    B E A N E D
    '''
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.cooldown(1, 5.0, commands.BucketType.user)
    @commands.command(pass_context=True,brief="B E A N E D")
    async def bean(self, ctx, *string):
        # await self.bot.say('{} is now <:banB:423155991706730499><:banE:423155991798874121><:banA:423155991664787456><:banN:423155991497146380><:banE:423155991798874121><:banD:423155991677501440>'.format(ctx.message.content[8:]))
        if '@everyone' in str(ctx.message.content):
            embed = discord.Embed(title='Bean command failed!', description='Please do not attempt to ban everyone thx', color=0xFF0000)
            embed.set_thumbnail(url='https://i.imgur.com/z2xfrsH.png')
            await self.bot.say(embed=embed)
        else:
            await self.bot.say('{} is now <:banB:423155991706730499><:banE:423155991798874121><:banA:423155991664787456><:banN:423155991497146380><:banE:423155991798874121><:banD:423155991677501440>'.format(parser(ctx.message.content)))
      
def parser(message):
    command=message[message.find(prefix)+len(prefix):] 
    return([command[:command.find(' ')], command[command.find(' ')+1:]]) 

def setup(bot):
    bot.add_cog(Bean(bot))