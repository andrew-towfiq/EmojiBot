import PIL
from PIL import Image
import io
import os
import glob
import asyncio

import discord
from discord import app_commands

# TODO:
# figure out how to persist transparent backgrounds for images when we generate emojis


class Emojibot(discord.Client):
    def __int__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)

    async def setup_hook(self):
        tree.copy_global_to(guild=discord.Object(id=guild_id_goes_here))
        await tree.sync(guild=discord.Object(id=guild_id_goes_here))

    async def on_ready(self):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="a sick guitar riff"))

        

intents = discord.Intents.default()  
client = Emojibot(intents=intents)  
tree = app_commands.CommandTree(client)

# async def make_emoji(image_data: bytes, filename: str) -> str:
#     """
#     Accepts image filepath and resizes image as a emoji-sized image
#     """

@tree.command(name = "shitpost")
async def make_emoji(interaction: discord.Interaction, attachment: discord.Attachment) -> None:
    await interaction.response.defer(thinking=True)
    filename = attachment.filename
    image_data = await attachment.read()

    base_width = 128
    image = Image.open(io.BytesIO(image_data))
    rgb_image = image.convert('RGBA')
    width_percent = (base_width / float(rgb_image.size[0]))
    hsize = int((float(rgb_image.size[1]) * float(width_percent)))
    rgb_image = rgb_image.resize((base_width, hsize), PIL.Image.ANTIALIAS)
    save_filename = f"{filename.split('.')[0]}_emojified.png"
    rgb_image.save(save_filename)
    file = discord.File(save_filename)
    sending = await interaction.followup.send(file=file)
    while not sending:
        os.remove(save_filename)
        return

    

if __name__ == "__main__":
    DELETE_THIS_FUCKING_TOKEN_BEFORE_YOU_PUSH = "get_your_token_here"
    client.run(DELETE_THIS_FUCKING_TOKEN_BEFORE_YOU_PUSH)