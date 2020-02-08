<p align=center>

  <img width=300 src="https://i.imgur.com/CWHoH08.png"/>

  <br>
  <span><strong>Twitch of Things( ToT )</strong> It is a methodology to control arduino from twitch chat <br />
<img src="https://img.shields.io/badge/Python-3.8.1-green"> 
<img src="https://img.shields.io/badge/License-MIT-blue">
<a href="http://girlazo.com"><img src="https://img.shields.io/badge/Website-up-green"></a>
<img src="https://img.shields.io/badge/Version-0.0.1-blue">
</p>


<p align="center">
     <a href="#installation">Installation</a>
          &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
     <a href="#configuration">Configuration</a>
          &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
     <a href="#usage">Usage</a>
          &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#how-does-it-work">How does it work</a>
</p>



## Installation

**NOTE**: Python 3.8.1 or higher is required.

```bash
# clone the repo
$ git clone https://github.com/EsteveSegura/twitch-of-things.git

# change the working directory to insta-growth
$ cd twitch-of-things/src/bot

# install Python if is not installed

# install the requirements
$ pip install -r requeriments.txt
```


## Configuration 
Once we have installed our python project, we have to copy the code in ``src/arduino/demo.ino`` on our **arduino IDE** and send the code to the board


Now we have to go to the ``src/bot`` folder and open the ``config.py`` file and fill it with the credentials of our twitch bot and also the port on which our arduino runs.

```python
# config.py
TMI_TOKEN="oauth:xxxxxxxxxxxxxxxx"
CLIENT_ID="xxxxxxxxxxxxxxxx"
BOT_NICK="NICK_OF_THE_BOT"
BOT_PREFIX="!" #leave this like that
CHANNEL=["OUR_TWITCH_CHANNEL"]
COM_PORT="COM_PORT" #example "COM5"
```

## Usage
Being inside the ``src/bot`` folder, we simply have to run the python ``bot.py`` 
``` bash
$ cd src/bot
$ python bot.py
```
We can go to our **twitch chat** and write the following commands:

**!onled** : turns on the led
**!offled** : turns off the led

## How does it work
**ToT** uses the serial communication available on **USB** connections to create communication with our hardware. **ToT** gets all the chat messages from our **twitch** and interacts with **Arduino** when it receives certain commands.

**Being able to create hardware that will handle our twitch chat.**

## License
MIT © twitch-of-things