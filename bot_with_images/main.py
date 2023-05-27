import discord
from discord.ext import commands
import os
import random
import requests
all_mem = {
    'mem1.jpg': 1,   
    'mem2.jpg': 1,
    'mem3.jpg': 2   
}

all_cosmos = {
    'cosmonaut1.jpg': 1,   
    'cosmonaut2.jpg': 1,
    'cosmonaut3.jpg': 2,
    'cosmonaut4.jpg': 2   
}
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='£', intents=intents)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    
    images_with_rarity = []
    for mem, weight in all_mem.items():
        images_with_rarity.extend([mem] * weight)

    # Select a random image from the weighted list
    img_name = random.choice(images_with_rarity)

    with open(f'C:\\Users\\denis\\Desktop\\kodland\\M2\\M2L1\\bot_with_images\\images\\{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def cosmonaut(ctx):
    print('!!!!!', os.getcwd())
    images_with_rarity = []
    for cosmos, weight in all_cosmos.items():
        images_with_rarity.extend([cosmos] * weight)

    # Select a random image from the weighted list
    img_name = random.choice(images_with_rarity)

    with open(f'C:\\Users\\denis\\Desktop\\kodland\\M2\M2L1\\bot_with_images\\images\\{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''По команде dog вызывает функцию get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run('token')
