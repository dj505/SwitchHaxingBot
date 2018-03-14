import discord
import re
import xkcd
from discord.ext import commands
from sys import argv
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

class xkcdparse:
    """
    xkcd parser! Gets either a random comic, specified by number, or specified by keyword.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    word_responses = {
        "pointers": 138,
        "sudo": 149,
        "sandwich": 149,
        "compiling": 303,
        "code compiling": 303,
        "bobby tables": 327,
        "little bobby tables": 327,
        "duty calls": 386,
        "security": 538,
        "standards": 927,
        "password": 936,
        "denvercoder9": 979,
        "workflow": 1172,
        "free speech": 1357,
        "screenshot": 1373,
        "tasks": 1425,
        "real programmers": 378
    }

    @commands.command()
    async def xkcd(self, *, comic):
        comic = comic.lower()
        """Show xkcd comic by number. Use "latest" to show the latest comic, or "random" to show a random comic."""
        if comic == "latest":
            # await self.bot.say("https://xkcd.com/{}/".format(xkcd.getLatestComic().number))
            comicpage = "https://xkcd.com/{}/".format(xkcd.getLatestComic().number)
            page = requests.get(comicpage).content
            soup = BeautifulSoup(page, "html.parser")
            comicImageBlock = soup.find("div",{"id":"comic"})
            comicImageTag = comicImageBlock.find("img")
            comicURL = comicImageTag['src']
            embed = discord.Embed(title='Latest xkcd', description='Here\'s your comic!', color=0xFFFFFF)
            embed.set_image(url='https:{}'.format(comicURL))
            await self.bot.say(embed=embed)

        elif comic == "random":
            # await self.bot.say("https://xkcd.com/{}/".format(xkcd.getRandomComic().number))
            comicpage = "https://xkcd.com/{}/".format(xkcd.getRandomComic().number)
            page = requests.get(comicpage).content
            soup = BeautifulSoup(page, "html.parser")
            comicImageBlock = soup.find("div",{"id":"comic"})
            comicImageTag = comicImageBlock.find("img")
            comicURL = comicImageTag['src']
            embed = discord.Embed(title='Random xkcd', description='Here\'s your comic!', color=0xFFFFFF)
            embed.set_image(url='https:{}'.format(comicURL))
            await self.bot.say(embed=embed)

        elif comic.isdigit():
            # await self.bot.say("https://xkcd.com/{}/".format(xkcd.getComic(comic).number))
            comicpage = "https://xkcd.com/{}/".format(xkcd.getComic(comic).number)
            page = requests.get(comicpage).content
            soup = BeautifulSoup(page, "html.parser")
            comicImageBlock = soup.find("div",{"id":"comic"})
            comicImageTag = comicImageBlock.find("img")
            comicURL = comicImageTag['src']
            embed = discord.Embed(title='xkcd number {}'.format(comic), description='Here\'s your comic!', color=0xFFFFFF)
            embed.set_image(url='https:{}'.format(comicURL))
            await self.bot.say(embed=embed)


        elif comic in self.word_responses:
            # await self.bot.say("https://xkcd.com/{}/".format(xkcd.getComic(self.word_responses[comic]).number))
            comicpage = "https://xkcd.com/{}/".format(xkcd.getComic(self.word_responses[comic]).number)
            page = requests.get(comicpage).content
            soup = BeautifulSoup(page, "html.parser")
            comicImageBlock = soup.find("div",{"id":"comic"})
            comicImageTag = comicImageBlock.find("img")
            comicURL = comicImageTag['src']
            embed = discord.Embed(title='Keyphrase: {}'.format(comic), description='Here\'s your comic!', color=0xFFFFFF)
            embed.set_image(url='https:{}'.format(comicURL))
            await self.bot.say(embed=embed)

        else:
            await self.bot.say("I can't find that one!")

def setup(bot):
    bot.add_cog(xkcdparse(bot))
