import discord
from discord.ext import commands, tasks
import asyncio
from discord_slash import SlashCommand, cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice


intents = discord.Intents.all()
client = commands.Bot(command_prefix=['!'], intents=intents)
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"INFINIX#7276 (My Dev/Creator)"))

    print("Bot Made by INFINIX#7276")


@slash.slash(name="slashtest",
             description="A test command (You can change it)",
             options=[
               create_option(
                 name="opt",
                 description="The option",
                 option_type=3,  #check out the docs (link is provided in readme.md file) to know more about different types of options
                 required=False,
                 choices=[
                  create_choice(
                    name="FirstChoise",
                    value="Happy"
                  ),
                  create_choice(
                    name="SecondChoice",
                    value="Sad :("
                  )
                ]
               )
             ])

async def test(ctx, optone: str):
  await ctx.send(content=f"Okay! I'm setting your current mood to {opt} :p")
  await ctx.send(content="Contact `INFINIX#7276` to know more!\n\nJoin our discord at https://www.discord.gg/DNvFcrhdzr") 
  
  
  
token = bot token here
client.run(token)
