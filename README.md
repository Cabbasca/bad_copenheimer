# Bad Copenheimer

A Python impelentation of a discord bot that acts as a server scanner.

This is a discord bot that will scan ip adresses to see if they are minecraft servers and will post the results in your channel.

----

## Beta Release

The new bot is now public, you can check it out in the [dev-builds](https://github.com/Pilot1782/bad_copenheimer/tree/dev-builds) branch and by following the README.

## Installation

[Installation Page](https://www.github.com/Pilot1782/bad_copenheimer/wiki/Installation)

[Wiki](https://www.github.com/Pilot1782/bad_copenheimer/wiki)

[Troubleshooting](https://www.github.com/Pilot1782/bad_copenheimer/wiki/troubleshooting)

----

## Usage

### Experimental

**The New Bot is Done!**

You can now use the new bot, it is still in beta, but it is much more stable and has more features. You can find it [here](https://github.com/Pilot1782/bad_copenheimer/blob/dev-builds/mongoBot.pyw).

### Requirements

* Python 3.6 or higher
* Linux/Docker (for the scanner, the bot will run on windows)
* Masscan (for the scanner)
* requirements.txt (needs to be run with pip3)

### Normal

`/help`
This shows all of the commands you can use and their usage. Then to create your server list, run:

`/server_scan`
This will get a list of all active minecraft servers, you may want to set the threads higher than the current value. This will take several hours to complete.
**(legacy bot only)**

`/status`
This will get information about the requested server, including players online, ping, and if possible players connected.
**(legacy bot only)**

`/find`
This will look through your database to find servers that match the provided paramaters. In the new build, there are two more buttons that can be used to either show the player names and uuids of players found on the server or to pick another random server from the list, after pressing it, wait for the message to update.

![showcase](https://raw.githubusercontent.com/Pilot1782/bad_copenheimer/doc-resources/Screenshot_20230111_083824.png)

`/stats`
This will show you the stats of the databse.

![showcase](https://raw.githubusercontent.com/Pilot1782/bad_copenheimer/doc-resources/Screenshot_20221220_124016.png)

#### Important

In order for /status to work properly the server should have enable-query=true in the server.properties file. This allows the server to brodcast who is currently logged onto the server.

----

## Help

Please check the wiki before posting an issue and read through the [troubleshooting](https://github.com/Pilot1782/bad_copenheimer/wiki/troubleshooting) first.

----

## Todo

Moved to [Project](https://github.com/users/Pilot1782/projects/1)
