# Educational project of simple telegram bot on aiogram framework

### Bot features:
1. Show current weather:
   * Show the current weather for your location (you must attach your current location to the message);
   * Show the weather in the city you specified;
2. Show the official hryvnia exchange rate set by the national bank;
3. Show the latest cryptocurrency rate to USD.

---
### Video Demo: [YouTube](https://youtu.be/lOlyZjSbJ3g)

---
### Under the hood:
`bot.py` - the main control file.

`buttons.py` - the file contains buttons used in the bot interface.

`crypto_rate` - the file is responsible for interacting with https://api.coingecko.com/

`openweathermap` - the file is responsible for interacting with https://api.openweathermap.org/

`UAH_rate` - the file is responsible for interacting with https://bank.gov.ua/

`requirements.txt` - it is a file listing all the dependencies for project.
