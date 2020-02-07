from config import *
from twitchio.ext import commands
import serial
import time

serial = serial.Serial('COM5',9600) #your COMport

bot = commands.Bot(
    irc_token=TMI_TOKEN,
    client_id=CLIENT_ID,
    nick=BOT_NICK,
    prefix=BOT_PREFIX,
    initial_channels=CHANNEL
)

@bot.event
async def event_message(ctx):
     if ctx.author.name.lower() == BOT_NICK.lower():
          return

     if (ctx.content == "!encender"): # Command to perform
          print('Encendido') 
          serial.write('E'.encode()) # Data to send via serial PORT

     if (ctx.content == "!apagar"): # Command to perform
          print('Apagado')
          serial.write('A'.encode())# Data to send via serial PORT
     
     await bot.handle_commands(ctx)


if __name__ == "__main__":
    bot.run()

