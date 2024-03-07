from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
import telegram.ext
from telegram import InputFile
import cv2
import requests
from datetime import datetime
import telebot
import time
from .models import *
from dotenv import load_dotenv
load_dotenv() 
def start(update, context):
    
    chat_id = update.message.chat_id
    rr=chat_id1.objects.filter(chat_idname=chat_id).values()
    if rr:
        telegram_bot_token = os.getenv("TOKEN_ID")
        telegram_chat_id = chat_id
        bot = telebot.TeleBot(telegram_bot_token)

        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        if ret:
            cv2.imwrite("initial_snapshot.jpg", frame)
            photo = open("initial_snapshot.jpg", "rb")
            bot.send_photo(telegram_chat_id, photo)
        else:
            print("Error capturing the initial photo.")
        camera.release()

        fullbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
        camera = cv2.VideoCapture(0)
        start_time = datetime.now()

        while True:
            ret, frame = camera.read()
            if not ret:
                print("Error reading the camera feed.")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            bodies = fullbody_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            if len(bodies) > 0:
                for (x, y, w, h) in bodies:
                    current_time = datetime.now()
                    waiting_time = (current_time - start_time).total_seconds() / 60
                    body_image = frame[y:y + h, x:x + w]

                    if waiting_time > 1:
                        alert_message = f"Visitor has been waiting for {waiting_time:.2f} minutes."
                        bot.send_message(telegram_chat_id, alert_message)
                        cv2.imwrite("visitor_snapshot.jpg", body_image)
                        photo = open("visitor_snapshot.jpg", "rb")
                        bot.send_photo(telegram_chat_id, photo)

                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Full Body Snapshot", frame)
            cv2.waitKey(1000)

            if 0xFF == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()
        update.message.reply_text("Hello! Welcome to Kognitiv Security Bot!!")
        help(update, context)
    else:
        x=chat_id1.objects.create()
        x.chat_idname=chat_id
        x.save()
        print("Create Successfully")
        main()
def help(update, context):
    update.message.reply_text("""
    The following commands are available:
    /start -> Commands
    /content -> About us
    /photo -> Send me a photo
    /contact -> About My Club
     """)
def content(update, context):
    update.message.reply_text("We are developing this bot for security purposes")
def photo(update, context):
    update.message.reply_text("I sent my photo")
    photo_path = '/content/1678342903750.jpeg'
    with open(photo_path, 'rb') as photo_file:
        context.bot.send_photo(chat_id=update.message.chat_id, photo=InputFile(photo_file))
def contact(update, context):
    update.message.reply_text("Feel free to contact")
def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")
def main():
    updater = telegram.ext.Updater(token="6577062227:AAEu_7tFR_HqK1qTIghx1a-O4QU4pr4M4Gc", use_context=True)
    # django_url = "http://127.0.0.1:8000/"
    # response = requests.get(django_url)
    # print(response.text)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
    dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
    dispatcher.add_handler(telegram.ext.CommandHandler('content', content))
    dispatcher.add_handler(telegram.ext.CommandHandler('photo', photo))
    dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
    updater.start_polling()
    updater.idle()
def home(request):
    # django_url = "http://127.0.0.1:8000/"
    # response = requests.get(django_url)
    # print(response.text)
    print("BOT Started")
    main()
class MyClass(APIView):
    def get(self,request):
        print("Bot")
        main()
