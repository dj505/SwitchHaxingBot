import discord
from discord.ext import commands
from configparser import SafeConfigParser
import datetime
import asyncio

class ModUtils:
    '''
    Moderator utilities. Only moderators can use these (obviously).
    '''
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context="True",brief="Kicks a member.")
    async def kick(self, ctx, user: discord.Member):
        """
        Allows you to kick a member from the server quickly and easily.
        """
        embed = discord.Embed(title='Kicked Member', description='Bye, {}!'.format(user.name), color=0x00FF99)
        embed.set_thumbnail(url='https://icon-icons.com/icons2/564/PNG/512/Action_2_icon-icons.com_54220.png')
        await self.bot.say(embed=embed)
        await self.bot.kick(user)

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context="True",brief="Bans a member.")
    async def ban(self, ctx, user: discord.Member):
        """
        Allows you to ban a member from the server quickly and easily.
        """
        embed = discord.Embed(title='Banned Member', description='See ya, {}!'.format(user.name), color=0x00FF99)
        embed.set_thumbnail(url='https://findicons.com/files/icons/2625/google_plus_interface_icons/128/hammer.png')
        await self.bot.say(embed=embed)
        await self.bot.ban(user)

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context="True",brief="Gives a member credits.", aliases=['givecredits','giveprize','addcredits','addcredit'])
    async def givecredit(self, ctx, user: discord.Member, amount):
        """
        Used for adding credits to a member's wallet (in case of prizes, etc)
        """
        config = SafeConfigParser()
        currenttime = datetime.datetime.now()
        user = str(user.id)
        config.read('wallet.ini')
        if config.has_section(user):
            balance = int(config.get('{}'.format(user), 'balance'))
            balance = balance + int(amount)
            balance = str(balance)
            config.set('{}'.format(user), 'balance', "{}".format(balance))
            config.set('{}'.format(user), 'lastused', '{}'.format(currenttime))
            with open('wallet.ini', 'w') as f:
                config.write(f)

            embed = discord.Embed(title='Added Balance', description='Your balance has been updated successfully!', color=0xFFD000)
            embed.add_field(name='Balance', value='{} has given you {} credit(s)! Your balance is now {}.'.format(ctx.message.author, amount, balance), inline=True)
            embed.set_thumbnail(url='https://i.imgur.com/akZqYz8.png')
            await self.bot.say(embed=embed)

        else:
            config.add_section('{}'.format(user))
            config.set('{}'.format(user), 'lastused', '{}'.format(currenttime))
            credits = int(amount) + 150
            credits = str(credits)
            config.set('{}'.format(user), 'balance', '{}'.format(credits))
            with open('wallet.ini', 'w') as f:
                config.write(f)

            balance = int(config.get('{}'.format(user), 'balance'))
            embed = discord.Embed(title='Created Wallet', description='Your wallet has been created and updated successfully!', color=0xFFD000)
            embed.add_field(name='Balance', value='{} has given you {} credit(s)! Your balance is now {}.'.format(ctx.message.author, amount, balance), inline=True)
            embed.set_thumbnail(url='https://i.imgur.com/akZqYz8.png')
            await self.bot.say(embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context="true",brief="Adds a reaction gif",aliases=['addreact','addreaction','addjif'])
    async def addgif(self, ctx, arg1, arg2):
        """
        Adds a reaction gif.
        """
        config = SafeConfigParser()
        config.read('reactions.ini')
        config.set('gifs', '{}'.format(arg1), str('{}'.format(arg2)))
        with open('reactions.ini', 'w') as f:
            config.write(f)

        embed = discord.Embed(title='Added a reaction!', description='Your reaction has been successfully recorded.', color=0x00FF99)
        await self.bot.say(embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context=True, no_pm=True)
    async def prune(self, ctx, amount : int = 50):
        """
        Prunes bot messages.
        """
        channel = ctx.message.channel

        calls = 0
        async for msg in self.bot.logs_from(channel, limit=amount, before=ctx.message):
            if calls and calls % 5 == 0:
                await asyncio.sleep(1.5)

            if msg.author == self.bot.user:
                await self.bot.delete_message(msg)
                calls += 1
        if calls == 1:
            embed = discord.Embed(name='Pruned Messages', description='Complete.', color=0x00FF00)
            embed.set_author(name='Pruned Message(s)')
            done_message = await self.bot.say(embed=embed)
            await self.bot.delete_message(ctx.message)
            await asyncio.sleep(3)
            await self.bot.delete_message(done_message)
        else:
            embed = discord.Embed(name='Pruned Messages', description='Complete.'.format(str(calls)))
            embed.set_author(name='Pruned Message(s)')
            done_message = await self.bot.say(embed=embed)
            await self.bot.delete_message(ctx.message)
            await asyncio.sleep(3)
            await self.bot.delete_message(done_message)

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context=True, brief='Sets hax status for a given FW')
    async def setfw(self, ctx, fw, desc):
        '''
        Sets information for a given firmware version.
        '''
        config = SafeConfigParser()
        config.read('fwinfo.ini')
        firmware = str(fw)
        description = str(desc)
        if config.has_section('{}'.format(firmware)):
            config.set('{}'.format(firmware), 'info', '{}'.format(description))
            with open('fwinfo.ini', 'w') as f:
                config.write(f)
            embed = discord.Embed(title='Added a firmware config', description='Your config has been successfully recorded.', color=0x00FF99)
            await self.bot.say(embed=embed)

        else:
            config.add_section('{}'.format(firmware))
            config.set('{}'.format(firmware), 'info', '{}'.format(description))
            with open('fwinfo.ini', 'w') as f:
                config.write(f)
            embed = discord.Embed(title='Added a firmware config', description='Your config has been successfully recorded.', color=0x00FF99)
            await self.bot.say(embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context=True, brief='Removed a reaction gif entry', aliases=['delreact','removereact','killreact'])
    async def deletereact(self, ctx, reaction):
        '''
        Removes a reaction gif or entry from the database.
        '''
        config = SafeConfigParser()
        config.read('reactions.ini')
        if config.has_option('gifs','{}'.format(reaction)):
            config.remove_option('gifs','{}'.format(reaction))
            with open('reactions.ini','w') as f:
                config.write(f)
            embed = discord.Embed(title='Removed a reaction!', description='Your reaction has been successfully removed.', color=0x00FF99)
            await self.bot.say(embed=embed)
        else:
            embed = discord.Embed(title='I could not find that reaction!', description='Please enter a valid reaction or try again.', color=0xFF0000)
            embed.set_thumbnail(url='https://i.imgur.com/z2xfrsH.png')
            await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(ModUtils(bot))