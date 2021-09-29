# Project 2
## Setup
  - How to get an API
    - First you need to create a discord account and create a server. 
    - Next you need to create a new application using the developer portal and then create a new bot.
    - Then you need to add your bot to the server that you created earlier using the OAuth2 menu in the developer portal.
    - The API token you need for this project is located in the bot menu of the developer portal you should copy this for the next step. 
  - Where to put it to work with the code
    - you need to put this token into your .env file with the line DISCORD_TOKEN = {your API token}
  - Dependencies (what packages need to be installed to run the code)
    - You need to first install python3 using the command $ sudo apt install python3
    - Next you need to install the pip package manager usin the command $ sudo apt install python3-pip
    - Then you need to use pip to install discord.py and python-dotenv using the commands $ pip3 install -U discord.py and $ pip3 install -U python-dotenv 
## Usage
  - While the bot is running you can type the name of the ship from the Expanse "rocinante!" and it will return respond with a randomly selected quote from the show. 
## Research
  - One way that I found to keep the bot running is to use the screen command which in this project would be $ screen python3 bot.py
  - This command allows the bot to run in the background of the terminal and even allows us to keep it running after the SSH connection has been terminated.   
