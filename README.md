# League of Legends bot

Documentation of my [League of Legends](http://telegram.me/LoL_bot) Bot for Telegram.


# Getting Started

First of all, this bot is running under Docker with the help of Docker Compose, so you need to install it.

- [Install Docker](https://docs.docker.com/engine/install/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

Then you need to create your configuration file. You can file a sample configuration file at `extra_data/extra.json.sample` so you can just remove the `.sample` part and edit it with your configuration.

For setting up your configuration, you should edit the next parameters from that file:

- **admins**: Change `admin_id` with your Telegram ID
- **token**: Your bot token. Get it from [Bot Father](https://telegram.me/botfather)
- **token_logbot**: Your logging bot token. This is optional, only if you are going to use the `/log` command
- **lol_api**: Your LoL API key from RIOT. Request it at the [developer's portal](https://developer.riotgames.com/)
- **tft_api**: Your TFT API key from RIOT. Request it at the [developer's portal](https://developer.riotgames.com/)

You can use the developing token for both **lol_api** and **tft_api** for your tests, but the ideal is to request an API key for accessing the LoL API and the TFT API.

Next thing you should be changing is the file `extra_data/file_ids.json` replacing the content with only this:

```json
{}
```

That's pretty much all the pre-steps you should do before setting up the bot. If you have already done all the above steps, you can now run the bot by typing this in the folder where the bot is:

```bash
docker-compose up -d --build
```

If you followed all the steps, your bot should have received a message from your bot telling you it has started.

Now you should use the command `/update_champs x.x.1` changing `x.x` with the lattest version of the game, so if the lattest version is the `11.12` you should send to the bot `/update_champs 11.12.1`. Then the bot will start sending you some messages and it will send you all the game splasharts to fill the file `extra_data/file_ids.json` automatically.

Now it is your time to play with the bot, learn how it works internally and make a pull request with some interesting new features :) PS: You can use the file called `plantilla.py` as a template for new commands 😉

For troubleshooting, check the bot logs by typing:

```bash
docker-compose logs -f
```
# Commands

### Main commands
```
/lang: Shows a keyboard to change the bot language.
/info: Gives information about the bot.
/roles: Shows info to filter the champions by them role.
/help: Shows help about the commands.
/champs: Gives a list with the name of all the champions.
/sale: Gives the champions and skins on sale.
/patch: Gives information about the last patch.
/credits: Bot credits.
/rate: Rate the bot :)
/contact: Send a message to the bot administrator.
/notify: Enable/Disable the notifications.
/keyboard: Shows the keyboard (Not available for groups).
/cancel: Cancel the current command.
/hideboard: Hides the keyboard (Not available for groups).
/rotation: Gives the champions on rotation this week.
/summoner: Shows info to search for summoners.
/match: Shows info to search matches.
```

#### The `/roles`, `/summoner` and `/match` commands will show another list of commands

##### `/roles`
```
/assassins: Filter the champions by the role: Assassin
/fighters: Filter the champions by the role: Fighter
/adcs: Filter the champions by the role: Marksman
/tanks: Filter the champions by the role: Tank
/mages: Filter the champions by the role: Mage
/supports: Filter the champions by the role: Support
```

##### `/summoner`
```
The bot has some commands for obtaining information about summoners in the different servers. The commands are:
/euw test - Information of the summoner 'test' at EUW
/eune test - Information of the summoner 'test' at EUNE
/br test - Information of the summoner 'test' at BR
/na test - Information of the summoner 'test' at NA
/las test - Information of the summoner 'test' at LAS
/lan test - Information of the summoner 'test' at LAN
/kr test - Information of the summoner 'test' at KR
/tr test - Information of the summoner 'test' at TR
/ru test - Information of the summoner 'test' at RU
/oce test - Information of the summoner 'test' at OCE
Remember to change 'test' for the name of the summoner you are searching.
```

##### `/match`
```
The bot has some commands for obtaining information about matches in the different servers. The commands are:
/match_euw test - Information about the current match of the summoner 'test' at EUW
/match_eune test - Information about the current match of the summoner 'test' at EUNE
/match_br test - Information about the current match of the summoner 'test' at BR
/match_na test - Information about the current match of the summoner 'test' at NA
/match_las test - Information about the current match of the summoner 'test' at LAS
/match_lan test - Information about the current match of the summoner 'test' at LAN
/match_kr test - Information about the current match of the summoner 'test' at KR
/match_tr test - Information about the current match of the summoner 'test' at TR
/match_ru test - Information about the current match of the summoner 'test' at RU
/match_oce test - Information about the current match of the summoner 'test' at OCE
Remember to change 'test' for the name of the summoner you are searching.
```

# Screenshots
|   |   |   |
|:---:|:---:|:---:|
|<img src="http://i.imgur.com/LXSlNVK.jpg" width="275">|<img src="http://i.imgur.com/hqbhwps.jpg" width="275">|<img src="http://i.imgur.com/Z7b1PqC.jpg" width="275">|
|Language|Intro|Help|
|<img src="http://i.imgur.com/k7Y9uhB.jpg" width="275">|<img src="http://i.imgur.com/817Vuys.jpg" width="275">|<img src="http://i.imgur.com/GfKEyTE.jpg" width="275">|
|Champions|Champion's info|Champion's info 2|
|<img src="http://i.imgur.com/ZHOzTZA.jpg" width="275">|<img src="http://i.imgur.com/eYRFMlY.jpg" width="275">|<img src="http://i.imgur.com/jPTRiqJ.jpg" width="275">|
|Champion's extra|Summoner|Skin|
|<img src="http://i.imgur.com/zqq3mBO.jpg" width="275">|<img src="http://i.imgur.com/uHuBn2h.jpg" width="275">|<img src="http://i.imgur.com/ymBSpIG.jpg" width="275">|
|Sales|Match blue team|Match red team|

Screenshots reorganized by [@mathieuzen](https://github.com/mathieuzen/)
