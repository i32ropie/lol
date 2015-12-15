# League of Legends bot

Documentation of my [League of Legends](http://telegram.me/league_of_legends_bot) Bot for Telegram.

# Requirements

### [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

### [Importdir.py](https://gitlab.com/aurelien-lourot/importdir)

### [Riot-Watcher](https://github.com/pseudonym117/Riot-Watcher)

### [ColorClass](https://github.com/Robpol86/colorclass)

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
