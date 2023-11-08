import telebot
from hugchat import hugchat
from hugchat.login import Login

# Set up the Telegram bot
bot = telebot.TeleBot("6966056998:AAGjfd04v967cq1Gn7qcl95HmGbIsLpxa3Y")  # Replace with your Telegram bot token

# Initialize the hugchat chatbot
sign = Login("jsila380@gmail.com", "u_ks~8/ZH)Xj*M7")
cookies = sign.login()
sign.saveCookiesToDir()

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
id = chatbot.new_conversation()
chatbot.change_conversation(id)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    # Send the user's input to the chatbot and send the chatbot's response as a string
    response = str(chatbot.chat(user_input))
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Welcome to the AI chatbot. You can start by typing your message.")

bot.polling()

