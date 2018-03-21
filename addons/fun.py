import discord
from discord.ext import commands
import random

class Fun:
    '''
    Fun stuff to mess with
    '''
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command(pass_context=True,brief="Consult the Helix Fossil",aliases=['fossil','8ball','ask','consult','helixfossil'])
    async def helix(self, ctx, *question):
        """
        Consult the all-knowing helix fossil!
        """
        responses = ['It is certain.','It is decidedly so.','Without a doubt.','Yes, definitely.','You may rely on it.',
                     'As I see it, yes.','Most likely.','Outlook good.','Yes.','Signs point to yes.',
                     'Reply hazy, try again.','Ask again later.','Better not tell you now.','Cannot predict now.','Concentrate and ask again.',
                     'Don\'t count on it.','My reply is no.','My sources say no.','Outlook not so good.','Very doubtful.','Nope.',
                     'This isn\'t the time to use that!']

        embed = discord.Embed(name='The Helix Fossil Says:',description='_{}_'.format(random.choice(responses)), color=0xD1B163)
        embed.set_author(name='The Helix Fossil Says:')
        embed.set_thumbnail(url='https://askhelixfossil.com/img/fossil.png')
        await self.bot.say(embed=embed)

    @commands.command(brief="Flip a coin!", aliases=['tosscoin','flip','flipcoin','coinflip'])
    async def cointoss(self):
        embed = discord.Embed(name='Coin Flip!',description='The winner is...', color=0xEDEDED)
        embed.set_author(name='Coin Flip!')
        sides = ['heads','tails']
        result = random.choice(sides)
        if result == 'tails':
            embed.set_image(url='https://upload.wikimedia.org/wikipedia/en/thumb/3/37/Quarter_Reverse_2010.png/220px-Quarter_Reverse_2010.png')
        elif result == 'heads':
            embed.set_image(url='https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Quarter_Obverse_2010.png/220px-Quarter_Obverse_2010.png')
        await self.bot.say(embed=embed)

    @commands.command(brief='Roll a D20 for a specified stat!',aliases=['rollfor'])
    async def d20(self, *stat):
        result = random.randint(1,20)
        embed = discord.Embed(name='D20 roll!',description='Your result is...', color=0xFF0000)
        embed.set_author(name='D20 roll!')
        embed.set_thumbnail(url='https://i.imgur.com/s2qFxaa.png')
        if result <= 5:
            rollcomment = 'Way Off'
        elif result > 5 and result <= 10:
            rollcomment = 'Decent'
        elif result > 10 and result <= 15:
            rollcomment = 'Great!'
        elif result > 15 and result <= 19:
            rollcomment = 'Excellent!'
        if result == 20:
            embed.add_field(name='Natural 20!',value='_Perfect!_')
        else:
            embed.add_field(name='**{}**'.format(result),value=rollcomment)
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
