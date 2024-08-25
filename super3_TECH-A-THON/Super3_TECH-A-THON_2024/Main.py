from chatterbot import ChatBot
import users
import trainer
print('Log in or sign up (press Enter)')
NoUser=input('To continue without login, press space + enter:')
if NoUser!=' ':
    Username=input('Username:')
    password=input('Password:')

    if users.check_user(Username,password):
        pass
    else:
        users.update_user(Username,password)
else:
    Username='general'
bot = ChatBot(
    'MANAS',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.SpecificResponseAdapter'
    ],
    database_uri=f'sqlite:///Super3_TECH-A-THON_2024\\UserData\\{Username}.sqlite3'
)
print("Loading Data...")
trainer.train(bot)
print("Loading Successful.")
print('\t\t\t\t\tTHERA - The AI mind healer')
print('!!!BELIEVE YOUR ARE NOT ALONE!!!')
while True:
    try:
        User_input=input(f'{Username}:') if Username!='general' else input(f'user:')
        if User_input=='/stop':
            break

        bot_input = bot.get_response(User_input)
        
        print(f"{bot.name}:",bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break