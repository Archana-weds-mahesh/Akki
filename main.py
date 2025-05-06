import telebot
import re

# Hardcoded bot token (for private use only)
BOT_TOKEN = '7816936602:AAFNlwAXZLNd7fU1l56QhS-VW-WD4niBfBA'
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='Markdown')

# Only match messages like "450 15"
pattern = re.compile(r'^\s*(\d+(\.\d+)?)\s+(\d+(\.\d+)?)\s*$')

@bot.message_handler(func=lambda message: bool(pattern.match(message.text)))
def calculate_percentage(message):
    try:
        matches = pattern.match(message.text.strip())
        amount = float(matches.group(1))
        percent = float(matches.group(3))

        discount = (percent / 100) * amount
        final_amount = amount - discount
        rounded_amount = round(final_amount)

        def clean(val):
            return int(val) if val == int(val) else round(val, 2)

        amount = clean(amount)
        percent = clean(percent)
        discount = clean(discount)
        final_amount = clean(final_amount)

        reply = (
            f"*{percent}%* of *{amount}* = *{discount}*\n\n"
            f"*{amount}* - *{discount}* = *{final_amount}*\n\n"
            f"*Please pay:* *{rounded_amount}*"
        )

        bot.reply_to(message, reply)
    except:
        pass

bot.polling()
