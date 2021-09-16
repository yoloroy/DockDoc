import time
from unittest.mock import call

from telebot import types

from controller.controller import Controller
from lib.bols import next_field
from lib.formatting import to_currency_tuple
from model.BOLs import BasicBOL
from repository.blockchain_repository import BlockchainRepository
import telebot

state = "final"
state1 = None
dict_bol = dict()
dict_id_or_name = dict()
APPROVE_ID_GETTING = "fisher"
SENDER_NAME_GETTING = "send_fish"
ID_DISAPPROVE_GETTING = "not_fisher"
RECIEVER_NAME_GETTING = "recieve_fisher"
ALL_NAME_GETTING = "all_fish"

def start():
    BlockchainRepository()
    Controller()
    bot = telebot.TeleBot('1963996182:AAGfz1olDS09AzUQmLofxzJb0_2nBa-Kd1k')
    def get_all_data(message):
        global state
        global dict_bol

        dict_bol[state] = message.text
    def get_data(message):
        global state
        global dict_id_or_name



    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        global state
        global state1

        if message.text == "/start":
            bot.send_message(message.from_user.id, "Hello, how can i help you?\n"
                                                   "Write, /List_of_commands if want to see all commands\n")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Write /List of commands.")
        elif message.text == "/List_of_commands":
            bot.send_message(message.from_user.id, "/approve - to approve the transaction\n"
                                                   "/add - to add a new transaction\n"
                                                   "/disapprove - to disapprove the transaction\n"
                                                   "/see_as_sender - to see all transactions that you have sent\n"
                                                   "/see_as_a_receiver  - to see all transactions you have received\n"
                                                   "/see_all - to see all your transactions\n")
        elif message.text == "/add":

            state = "start_state"

        elif message.text == "/approve":
            bot.send_message(message.from_user.id, "Enter the id of operation\n")
            state1 = APPROVE_ID_GETTING
            return
        elif message.text == "/disapprove":
            bot.send_message(message.from_user.id, "Enter the id of operation\n")
            state1 = ID_DISAPPROVE_GETTING
            return
        elif message.text == "/see_all":
            bot.send_message(message.from_user.id, "Enter your name\n")
            state1 = ALL_NAME_GETTING
            return
        elif message.text == "/see_as_a_receiver":
            bot.send_message(message.from_user.id, "Enter your name\n")
            state1 = RECIEVER_NAME_GETTING
            return
        elif message.text == "/see_as_sender":
            bot.send_message(message.from_user.id, "Enter your name\n")
            state1 = SENDER_NAME_GETTING
            return
        elif state != "final":
            pass
        if state != "final":
            if state != "start_state":
                get_all_data(message)
            state = next_field(state)
            if state != "final":
                bot.send_message(message.from_user.id, "Give me " + state)
            else:
                index = Controller().add_document(BasicBOL ( dict_bol["sender"],
                                          dict_bol["receiver"],
                                          dict_bol["goods_type"],
                                          dict_bol["goods_amount"],
                                          to_currency_tuple(dict_bol["goods_value"]),
                                          dict_bol["place_of_start"],
                                          dict_bol["place_of_receive"],
                                          int(time.time())
                                          ))
                bot.send_message(message.from_user.id, "Index of your transaction is " + str(index))
        if state1 != None:
            if state1 == APPROVE_ID_GETTING:
                id = message.text
                Controller().approve_document(int(id))
            elif state1 == ID_DISAPPROVE_GETTING:
                id = message.text
                Controller().disapprove_document(int(id))
            elif state1 == ALL_NAME_GETTING:
                name = message.text
                bot.send_message(message.from_user.id, Controller().get_for(sender=name, receiver=name))
            elif state1 == SENDER_NAME_GETTING:
                name = message.text
                bot.send_message(message.from_user.id, Controller().get_for(sender=name))
            elif state1 == RECIEVER_NAME_GETTING:
                name = message.text
                bot.send_message(message.from_user.id, str(Controller().get_for(receiver=name)))




    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    start()
