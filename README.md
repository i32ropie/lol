# League of Legends bot

Documentation of my [League of Legends](http://telegram.me/LoL_bot) Bot for Telegram.

<!-- # Requirements

### [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

### [Importdir.py](https://gitlab.com/aurelien-lourot/importdir)

### [Riot-Watcher](https://github.com/pseudonym117/Riot-Watcher)

### [ColorClass](https://github.com/Robpol86/colorclass) -->

# Getting Started

## IMPORTANT

This is outdated. I'll update it as soon as possible. Stay tunned :)

First of all, this bot is running in Python 3 so you need to install it and also pip for installing the modules.
```bash
sudo apt-get install python3 python3-pip
```

Then, you need the used modules.
```markdown
Tip: Type `pip` and double-tab to see different possibilities, maybe you need to need to use `pip-3.X` or only `pip`.
```
```bash
sudo pip3 install colorclass
sudo pip3 install pyTelegramBotAPI
sudo pip3 install riotwatcher
sudo pip3 install psutil
```

Then, you need an `API key` from here https://developer.riotgames.com/ and a `Token` from http://telegram.me/BotFather.

When you have the `API key` and the `Token`, paste them into `extra_data/extra.json.sample` and delete the `.sample` from the filename.

Remove also `.sample` from `usuarios.json.sample`.

Also, the `extra_data/file_ids.json` won't work for you, so you need to download the pictures and create your own `file_ids.json` file. For this, go to http://ddragon.leagueoflegends.com/tool/ and download the `dragontail-VERSION.tgz`. Extract the pics (located at `img/champion/splash/`) and use this little script in the same folder as the extracted pics are:
```bash
wget https://gist.githubusercontent.com/i32ropie/895ce1c9e4cb3a822c19/raw/d975557a5511fc6488a70a08505409daa39f4f65/script.py
# Now edit the script and add your personal ID and your Token to it, I'll use nano for this. Tip: To leave&save use ctrl+X, Y, ENTER.
nano script.py
python3 script.py
```

Once you have your `file_ids.json`, replace the one at `extra_data` with yours.

We are almost done, now go to the project folder and create a new folder called `logs`.
```bash
mkdir logs
```

Finally, to run our bot we just need to type: `./LCS_bot.py`.

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
