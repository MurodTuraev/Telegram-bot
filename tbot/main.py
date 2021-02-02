import telebot

bot = telebot.TeleBot('1597735413:AAEA20RoZ_JJsQ3b4q8XvKuegECeH-i6exk')


@bot.message_handler()
def echo_messages(*messages):
    """
    Echoes all incoming messages of content_type 'text'.
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            bot.send_message(chatid, text)


bot.polling()
