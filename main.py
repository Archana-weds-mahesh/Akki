import telebot
import re
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')  # Get token from environment variable
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='Markdown')

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
