# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 21:52:26 2022

@author: Samson Thibaut

"""

from telegram import *
from telegram.ext import *
from requests import *

token = 'your-token'
# {update.effective_chat.username}

def start(update, context):
    update.message.reply_text(f"""
Bonjour {update.effective_user.first_name} {update.effective_user.last_name},
Je suis Samson, l’assistant intelligent de l'Institut Universitaire de la Cote. Que puis-je faire pour vous ?

Les commandes disponibles sont :
- /site pour obtenir l'adresse du site web
- /youtube pour obtenir la chaine YouTube
- /linkedin pour obtenir le profil LinkedIn
- /instagram pour obtenir le profil Instagram
- /facebook pour obtenir le profil Ifacebook 
- /twitter pour obtenir le profil Twitter
- /conditions_admission pour obtenir les conditions d’admission
- /partner pour obtenir l’ensemble des partenaires 
- /formation pour obtenir les formations que l'on propose
- /contact pour etre mis en contact avec un de nos operateurs
    """)

def site(update, context):
    update.message.reply_text('l\'adresse web de l\'IUC est la suivante : https://myiuc.com/')
    
def instagram(update, context):
    update.message.reply_text('le profil instagram de l\'IUC est le suivant : https://www.instagram.com/iucdouala/')

def twitter(update, context):
    update.message.reply_text('le profil twitter de l\'IUC est le suivant : https://twitter.com/iucdouala')
    
def facebook(update, context):
    update.message.reply_text('le profil facebook de l\'IUC est le suivant : https://www.facebook.com/IucDouala')

def conditions_admission(update, context):
    update.message.reply_text('les conditions d\'admission dependent de la formation que vous souhaitez. Pour commencer, laissez moi pour poser quelques questions concernant vos choix')

def partner(update, context):
    update.message.reply_text('les partenaires bla bla bla test test test test : https://myiuc.com/')

def youtube(update, context):
    update.message.reply_text('la chaine YouTube de l\'IUC est la suivante : https://www.youtube.com/channel/UC-w1EIXTvmUhPsRaEZlU_2Q')

def linkedin(update, context):
    update.message.reply_text('le profil linkedIn de l\'IUC est le suivant : https://www.linkedin.com/in/iucdouala/')
    
def formation(update, context):
    update.message.reply_text('Nos programmes de formations sont sur notre site web a cette adresse : https://myiuc.com/nos-formations/tous-programmes/')
    
def contact(update, context):
    update.message.reply_text('Vous souhaitez contacter le CallCenter ? C\'est ici : +237 699684612')

                              
def main():
    # La classe Updater permet de lire en continu ce qu'il se passe sur le channel
    updater = Updater(token, use_context=True)

    # Pour avoir accès au dispatcher plus facilement
    dp = updater.dispatcher

    # On ajoute des gestionnaires de commandes
    # On donne a CommandHandler la commande textuelle et une fonction associée
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("youtube", youtube))
    dp.add_handler(CommandHandler("formation", formation))
    dp.add_handler(CommandHandler("contact", contact))
    dp.add_handler(CommandHandler("linkedin", linkedin))
    dp.add_handler(CommandHandler("instagram", instagram))
    dp.add_handler(CommandHandler("twitter", twitter))
    dp.add_handler(CommandHandler("conditions_admission", conditions_admission))
    dp.add_handler(CommandHandler("partner", partner))
    dp.add_handler(CommandHandler("facebook", facebook))
    
    # Sert à lancer le bot
    updater.start_polling()
    
    # Pour arrêter le bot proprement avec CTRL+C
    updater.idle()


if __name__ == '__main__':
    main()
                              

