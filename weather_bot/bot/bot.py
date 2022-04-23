from os import environ
import telebot
import psycopg2


conn = psycopg2.connect(dbname='db', user='postgres', password='postgres', host='db')
cursor = conn.cursor()


tg_token = environ['tg_token']

bot = telebot.TeleBot(tg_token)
