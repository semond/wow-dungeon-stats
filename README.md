# World of Warcraft Dungeon Statistics (Legion)

This is a simple *personal* python script to get, using [WoW's Dev API][dev-portal], Dungeon statistics.

“Personal” means that it doesn’t follow “best practices” and won’t care about errors and such.

For the moment, this obtains and prints :

- the total number of dungeon end boss kills, for normal, heroic and mythic (including mythic+) ;
- the counters associated with the achievements for *completing within the allotted time* :
    - [Keystone Initiale](http://www.wowhead.com/achievement=11183) (Level 2 or higher keystone) ;
    - [Keystone Challenger](http://www.wowhead.com/achievement=11184) (Level 5 or higher keystone) ;
    - [Keystone Conqueror](http://www.wowhead.com/achievement=11185) (Level 10 or higher keystone) ;
    - [Keystone Master](http://www.wowhead.com/achievement=11162) (Level 15 or higher keystone).

## Requirements

Python. Tested with Python 2.7, known to work on OS X, should work elsewhere too.

## Support

I will not give any kind of support for this. Install it and use it if you can (and want to). If you don’t understand how to do this, I don’t care, and I won’t help.

## Installation

I suggest a virtual environment.

```shell
$ pip install -U git+https://github.com/semond/wow-dungeon-stats
```

## Usage

### Configuration file

First, you need a configuration file. The current script looks for :

1. your home directory, a file named “.wow-dungeon-stats.json” ;
2. your home directory, a file named “wow-dungeon-stats.json” ;
3. the current directory, a file named “config.json”.

You can also specify the filename (with path) using the --config-file argument.

The configuration file is in JSON format. Example :

```json
{
    "key": "WOW-API-KEY",
    "secret": "WOW-API-SECRET",
    "realm": "Default Realm"
}
```

`realm` is the only optional configuration option.

`key` and `secret` are generated using [Blizzard’s Developper Portal][dev-portal].


[dev-portal]: https://dev.battle.net


### Usage

```console
$ dungeon-stats --help
Usage: dungeon-stats [OPTIONS] CHARACTER_NAME

  Run.

Options:
  --realm TEXT        Character's realm
  --config-file TEXT  Configuration file (json)
  --help              Show this message and exit.
```

Example :

```console
$ dungeon-stats --realm "Kel'Thuzad" Bluecedar
  2 Wrath of Azshara kills (Normal Eye of Azshara)
  4 Wrath of Azshara kills (Heroic Eye of Azshara)
 20 Wrath of Azshara kills (Mythic Eye of Azshara)
  4 Shade of Xavius kills (Normal Darkheart Thicket)
  6 Shade of Xavius kills (Heroic Darkheart Thicket)
 13 Shade of Xavius kills (Mythic Darkheart Thicket)
  1 Dargrul kills (Normal Neltharion's Lair)
  6 Dargrul kills (Heroic Neltharion's Lair)
 23 Dargrul kills (Mythic Neltharion's Lair)
  2 Odyn defeats (Normal Halls of Valor)
  9 Odyn defeats (Heroic Halls of Valor)
 15 Odyn defeats (Mythic Halls of Valor)
  1 Fel Lord Betrug kills (Normal Assault on Violet Hold)
  0 Sael'orn kills (Normal Assault on Violet Hold)
  5 Fel Lord Betrug kills (Heroic Assault on Violet Hold)
  4 Sael'orn kills (Heroic Assault on Violet Hold)
  4 Fel Lord Betrug kills (Mythic Assault on Violet Hold)
  3 Sael'orn kills (Mythic Assault on Violet Hold)
  1 Cordana Felsong kills (Normal Vault of the Wardens)
  5 Cordana Felsong kills (Heroic Vault of the Wardens)
 20 Cordana Felsong kills (Mythic Vault of the Wardens)
  1 Kur'talos Ravencrest defeats (Normal Black Rook Hold)
  9 Kur'talos Ravencrest defeats (Heroic Black Rook Hold)
 21 Kur'talos Ravencrest defeats (Mythic Black Rook Hold)
  1 Helya defeats (Normal Maw of Souls)
  7 Helya defeats (Heroic Maw of Souls)
 32 Helya defeats (Mythic Maw of Souls)
 18 Advisor Vandros kills (Mythic Arcway)
 13 Advisor Melandrus kills (Mythic Court of Stars)


Normal Dungeons: 13
Heroic Dungeons: 55
Mythic Dungeons: 182
Total: 250


Completed Keystone 2+ within time: 86
Completed Keystone 5+ within time: 55
Completed Keystone 10+ within time: 2
Completed Keystone 15+ within time: 0
```


