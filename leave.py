#!/usr/bin/env python
# -*- coding: utf-8 -*-
import discord, asyncio
import os
import shutil
import subprocess
from discord.ext import commands
import json
import time
import sys
import datetime
import random
import ctypes

if not os.path.exists('config.json'):
    data = {
        'token': "",
        'prefix': "",
    }
    with open('config.json', 'w') as f:
        json.dump(data, f)

config = json.loads(open("config.json","r").read())
token = config['token']
prefix = config['prefix']


def getembed(text):
    embed = discord.Embed(
        description=text,
        color=0x2f3136
    )
    return embed

def checkConfig():
    if not token == "" and not prefix == "":
        return
    else: 
        if token == "":
            config['token'] = input('What is your token?\n')
        if prefix == "":
            config['prefix'] = input('Please choose a prefix for your commands e.g "+"\n')
        open('config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
        print('The program will now close so everything works correctly.')
        time.sleep(5)
        sys.exit()
        return

Client = discord.Client()
Client = commands.Bot(
    description='cnr selfbot',
    command_prefix=config['prefix'],
    self_bot=True
)
Client.remove_command('help') 

def getav(url, user):
    return discord.Embed(title='Avatar', color=0x2f3136).set_image(url=url).set_footer(text=user)    

@Client.event
async def on_ready():
    
    os.system('cls')
    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print()
        print("[+] Made by cnr [+]".center(width))
        print()
        print(f"Current User: {Client.user}".center(width))
        print(f"User ID: {Client.user.id}".center(width))
        print()
        print(f"Prefix: {prefix}".center(width))
        print(f"Date: {datetime.date.today().strftime('%d, %B %Y')}".center(width))
        print()
        print("Commands:".center(width))
        print(f" {prefix}leave - LEAVE THE FUCKING CHANNELS".center(width))
    ui()
 
    @Client.command()
    async def leave(ctx):
        await ctx.message.delete()
        args = ctx.message.content.split()
        if len(args) == 1:
            text = f"""
**Invalid Parse Of Arguments**

`{args[0]}` **[partial group name]**
"""
            embed = getembed(text)
            try:
                await ctx.send(embed=embed,delete_after=30)
            except:
                await ctx.send(f">>> {text}")
        else:
            args.pop(0)
            groupname = ' '.join(args)
            counter = 0
            for channel in Client.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    if groupname in str(channel):
                        try:
                            await channel.leave()
                            counter +=1
                            ctypes.windll.kernel32.SetConsoleTitleW(
                                    f"Discord group leaver / Left [{counter}] "
                                    f"github.com/terrorist"
                                )
                            print(f'Left channel {channel}')
                        except:
                            pass
            print(f'Left {counter} channels in total.')

checkConfig()
Client.run(config['token'], bot=False, reconnect=True)