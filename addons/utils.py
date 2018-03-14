import discord
from discord.ext import commands
from configparser import SafeConfigParser
import datetime

class Utils:
    '''
    User utilities. Anyone can use.
    '''
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command(pass_context="True",brief="Gets user information.")
    async def userinfo(self, ctx, user: discord.Member):
        """
        Allows you to get information on a user simply by tagging them.
        """
        embed = discord.Embed(title='User Information Panel', description='User information for {}:'.format(user.name), color=0x00FF99)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name='Name', value=user.name, inline=True)
        embed.add_field(name='ID', value=user.id, inline=True)
        embed.add_field(name='Status', value=user.status, inline=True)
        embed.add_field(name='Highest Role', value=user.top_role, inline=True)
        embed.add_field(name='Join Date', value=user.joined_at, inline=True)
        await self.bot.say(embed=embed)

    @commands.command(pass_context="True",brief="Adds 150 to your currency count. Can be used once every 24 hours.", aliases=['money','coin','wallet'])
    @commands.cooldown(1, 86400.0, commands.BucketType.user)
    async def daily(self, ctx):
        """
        This command adds 150 credits to your wallet. Can only be used once per day. This command is still a WIP.
        """
        config = SafeConfigParser()
        currenttime = datetime.datetime.now()
        user = ctx.message.author.id
        config.read('wallet.ini')
        if config.has_section('{}'.format(user)):
            balance = int(config.get('{}'.format(user), 'balance'))
            balance = balance + 150
            balance = str(balance)
            config.set('{}'.format(user), 'balance', "{}".format(balance))
            config.set('{}'.format(user), 'lastused', '{}'.format(currenttime))
            with open('wallet.ini', 'w') as f:
                config.write(f)

            embed = discord.Embed(title='Added Balance', description='Your balance has been updated successfully!', color=0xFFD000)
            embed.add_field(name='Balance', value='Your balance is now {}.'.format(balance), inline=True)
            embed.set_thumbnail(url='https://i.imgur.com/akZqYz8.png')
            await self.bot.say(embed=embed)

        else:
            config.add_section('{}'.format(user))
            config.set('{}'.format(user), 'lastused', '{}'.format(currenttime))
            config.set('{}'.format(user), 'balance', '150')
            with open('wallet.ini', 'w') as f:
                config.write(f)

            embed = discord.Embed(title='Created Wallet', description='Your wallet has been created successfully!', color=0xFFD000)
            embed.add_field(name='Balance', value='Your balance is now 150.', inline=True)
            embed.set_thumbnail(url='https://i.imgur.com/akZqYz8.png')
            await self.bot.say(embed=embed)

    @commands.command(pass_context="True",brief="Posts a reaction gif",aliases=["reaction","reactiongif","gif","jif"])
    async def react(self, ctx, arg):
        """
        Posts a reaction image or copypasta from a keyword specified.
        """
        config = SafeConfigParser()
        config.read('reactions.ini')
        gif = config.get('gifs','{}'.format(arg))
        if gif.startswith('http'):
            embed = discord.Embed(title=None, description=None, color=0x00FF99)
            embed.set_image(url=gif)
            await self.bot.say(embed=embed)
        else:
            embed = discord.Embed(title=None, description=None, color=0x00FF99)
            embed.add_field(name=gif, value='Requested by {}'.format(ctx.message.author), inline=True)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, brief='Displays server information')
    async def serverinfo(self, ctx):
        embed = discord.Embed(name='Server Information Panel', description='Here you go!', color=0x00FF99)
        embed.set_author(name='{}'.format(ctx.message.author.name) + '\'s Info Request')
        embed.add_field(name='Name', value=ctx.message.server.name, inline=True)
        embed.add_field(name='ID', value=ctx.message.server.id, inline=True)
        embed.add_field(name='Roles', value=len(ctx.message.server.roles), inline=True)
        embed.add_field(name='Members', value=len(ctx.message.server.members), inline=True)
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True, brief='A Link to the Source')
    async def source(self, ctx):
        embed = discord.Embed(title='Bot Source Code', description='Have some spaghetti code!', color=0x00FF99)
        embed.set_thumbnail(url='https://opensource.org/files/osi_keyhole_600X600_90ppi.png')
        embed.add_field(name='GitHub Repository', value='https://github.com/dj505/SwitchHaxingBot', inline=True)
        await self.bot.say(embed=embed)

#    @commands.command(pass_context=True, brief='Says something')
#    async def say(self, ctx, *string):
#        if '@' in str(ctx.message.content):
#            embed = discord.Embed(title='Say command failed!', description='Please do not attempt to tag users with this command. \
#                                                                            This results in either double tagging, or sending an `@everyone` tag \
#                                                                            without permissions by using the bot as a loophole.', color=0xFF0000)
#            embed.set_thumbnail(url='https://i.imgur.com/z2xfrsH.png')
#            await self.bot.say(embed=embed)
#
#        elif ctx.message.author.name == "chucknorify17":
#            config = SafeConfigParser()
#            config.read('settings.ini')
#            truefalse = config.get('main','chuckcanuse')
#            if truefalse == 'True':
#                await self.bot.say(ctx.message.content[7:])
#                await self.bot.delete_message(ctx.message)
#            else:
#                await self.bot.say('Sorry chuck, you can\'t use that right now')
#
#        else:
#            await self.bot.say(ctx.message.content[7:])
#            await self.bot.delete_message(ctx.message)
#
#    @commands.command(pass_context=True)
#    @commands.has_permissions(ban_members=True)
#    async def letchuckusesay(self, ctx, tf):
#        if ctx.message.author.name == "chucknorify17":
#            await self.bot.say('nice try chuck')
#
#        else:
#            config = SafeConfigParser()
#            config.read('settings.ini')
#            truefalse = str(tf)
#            config.set('main','chuckcanuse','{}'.format(truefalse))
#            with open('settings.ini', 'w') as f:
#                config.write(f)
#            await self.bot.say('Can Chuck use the `say` command: {}'.format(truefalse))

    @commands.command(pass_context=True, brief='Get user avatar')
    async def avatar(self, ctx, user: discord.Member):
        embed = discord.Embed(name='Avatar', description=None, color=0x000000)
        embed.set_image(url=user.avatar_url)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True, brief='Lists hax status on a given FW')
    async def fwinfo(self, ctx, fw):
        '''
        Lists information on a given firmware.
        '''
        config = SafeConfigParser()
        config.read('fwinfo.ini')
        if config.has_section('{}'.format(fw)):
            information = config.get('{}'.format(fw), 'info')
            embed = discord.Embed(title='Firmware Information for {}'.format(fw), description='{}'.format(information), color=0x00FF99)
            await self.bot.say(embed=embed)

        else:
            embed = discord.Embed(title='Invalid firmware!', description='I cannot find that firmware version!', color=0xFF0000)
            embed.set_thumbnail(url='https://i.imgur.com/z2xfrsH.png')
            await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Utils(bot))
