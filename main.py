import telebot
Token = "Your token"
bot=telebot.TeleBot(Token)

channel="your channel name"

#cuses of eror "invalid 400"
#bot shoude be in the group 
#bot shoude be admin of group
#group not privet


def is_user_member(user_id):
    try:
        member = bot.get_chat_member(chat_id=f"@{channel}" , user_id=user_id)
        if member.status['member','adminestrator','creator']:
            return True
        
    except Exception as e :
        print(f"Eror{e}")
    return False    

@bot.message_handler(commands=['start'])
def welcome (message):
    user_id= message.from_user.id
    if is_user_member(user_id):
        bot.send_message(message.chat.id , "welcome to Bot")
    else:
        bot.send_message(message.chat.id , "bot faild")


if __name__ == "__main__":
    print("Bot is working")
    try:
        bot.polling()
    except Exception as e:
        print(f"{e}")