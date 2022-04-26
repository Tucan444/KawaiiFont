import discord
from discord.ext import commands
from KawaiiFont.AnimeFont.main import *


class Functions(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.letter_height = 300
        self.letters = get_letters(self.letter_height, "AnimeFont/")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if str(message.content)[0] == ".":
            await message.channel.purge(limit=1)
            img = get_image(str(message.content)[1:], self.letters, self.letter_height)
            pygame.image.save(img, f"AnimeFont/KawaiiFolder/KawaiiFont - {str(message.content)}.png")
            with open(f"AnimeFont/KawaiiFolder/KawaiiFont - {str(message.content)}.png", "rb") as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)


def setup(client):
    client.add_cog(Functions(client))