import discord
import random
import requests
import os
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import gen_emodji

with open("token.txt", "r") as f: # Membaca token dari file token.txt
    token = f.read() # Menyimpan token ke dalam variable token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def passwd(ctx):
    await ctx.send(gen_pass(5))

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji())


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    nama_img = random.choice(os.listdir('images'))

    with open(f'images/{nama_img}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run(token)