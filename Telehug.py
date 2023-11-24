import telebot
from hugchat import hugchat
from hugchat.login import Login
import time
import traceback

# Set up the Telegram bot
bot_token = "bot-token"
bot = telebot.TeleBot(bot_token)

# Initialize the hugchat chatbot
sign = Login("hugchat-email", "Hugchat-password")
cookies = sign.login()
sign.saveCookiesToDir()

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
id = chatbot.new_conversation()
chatbot.change_conversation(id)

def handle_message(message):
    user_input = message.text
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    response = str(chatbot.chat(user_input))
    bot.send_message(message.chat.id, response)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        handle_message(message)
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
        reconnect_and_handle_errors()

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Welcome to the AI chatbot. You can start by typing your message.")

def reconnect_and_handle_errors():
    global bot
    while True:
        try:
            bot.stop_polling()
            bot = telebot.TeleBot(bot_token)
            bot.infinity_polling(timeout=30, long_polling_timeout=5)
        except Exception as e:
            print(f"Reconnection failed: {e}")
            traceback.print_exc()
            time.sleep(10)  # Add a longer delay before attempting to reconnect again

# Start the bot
try:
    bot.infinity_polling(timeout=30, long_polling_timeout=5)
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
    reconnect_and_handle_errors()
