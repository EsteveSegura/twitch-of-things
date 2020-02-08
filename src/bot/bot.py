from config import *
from twitchio.ext import commands
import serial

serial = serial.Serial(COM_PORT,9600) #Our COM port and baud rate!

bot = commands.Bot(
    irc_token=TMI_TOKEN,
    client_id=CLIENT_ID,
    nick=BOT_NICK,
    prefix=BOT_PREFIX,
    initial_channels=CHANNEL
)

#Event fired when bot is conected
@bot.event
async def event_ready():
     print(f'{BOT_NICK}, is working!')
     ws = bot._ws

#Event fire every time someone writes in chat
@bot.event
async def event_message(ctx):
     if ctx.author.name.lower() == BOT_NICK.lower():
          return
     await bot.handle_commands(ctx)
 
#First command to turn on the LED
@bot.command(name="onled")
async def ledOn(ctx):
     if ctx.author.is_mod: #Only if is mod
          await ctx.send(f'{ctx.author.name}, ha encendido el Led!') #Sending confirmation to chat
          serial.write('E'.encode()) #Writing data to arduino
     else:
          await ctx.send(f'{ctx.author.name}, parece que no eres mod, solo los mods pueden encender el Led!') #Giving error if is not mod

#Secon command to turn off the LED
@bot.command(name="offled")
async def ledOn(ctx):
     if ctx.author.is_mod: #Only if is mod
          await ctx.send(f'{ctx.author.name}, ha apagado el Led!') #Sending confirmation to chat
          serial.write('A'.encode()) #Writing data to arduino
     else:
          await ctx.send(f'{ctx.author.name}, parece que no eres mod, solo los mods pueden apagar el Led!') #Giving error if is not mod

if __name__ == "__main__":
    bot.run()