# Telegram Percentage Bot

This is a simple Telegram bot that calculates percentage discounts like:
```
User sends: 450 15
Bot replies:
15% of 450 = 67.5

450 - 67.5 = 382.5

Please pay: 383
```

### How to Deploy on Render

1. Create a new Web Service on [https://render.com](https://render.com)
2. Connect this GitHub repo
3. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
4. Add environment variable `BOT_TOKEN=your_telegram_bot_token`
