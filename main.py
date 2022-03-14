from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = '5256740903:AAF3uBytnyLXS6w_KcVOkrBcuhzI5mje5wg'
updater = Updater(TOKEN, use_context = True)
dispatcher = updater.dispatcher
print('Bot Started!')
def start(update,context):
    chat = update.effective_chat
    greetings = ''' Hello! Welcome to my math calculator bot. 
Input /solve and write like /solve 2 + 2 (with spaces!). 
My bot has four operations: +, -, *, /. '''
    context.bot.send_message(chat_id = chat.id, text = greetings)



def solve(a, b, action):
    if action == "+":
        print(a + b)
        final = a + b
    elif action == "-":
        print(a - b)
        final = a - b
    elif action == "*":
        print(a * b)
        final = a * b
    elif action == "/":
        print(a / b)
        final = a / b
    else:
        return "Choose correct operation"
    return final

def logic(update, context):
    chat = update.effective_chat
    l = update.message.text
    try:
        q, b, c, d = l.split()
    except ValueError:
        context.bot.send_message(chat_id = chat.id, text = "Error")
        return
    if b.isdigit():
        floatb = float(b)
    else:
        context.bot.send_message(chat_id = chat.id, text = "Error")
    if d.isdigit():
        floatd = float(d)
    else:
        context.bot.send_message(chat_id = chat.id, text = "Error")
    w = solve(floatb, floatd, solve)
    context.bot.send_message(chat_id=chat.id, text=w)


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('solve', logic))
updater.start_polling()
updater.idle()