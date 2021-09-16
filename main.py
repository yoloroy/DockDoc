from controller.controller import Controller
from repository.blockchain_repository import BlockchainRepository
import telebot


def start():
    BlockchainRepository()
    Controller()
    bot = telebot.TeleBot('1963996182:AAGfz1olDS09AzUQmLofxzJb0_2nBa-Kd1k')

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == "Hello" or message.text == "hello":
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
            pass

        elif message.text == "/approve":
            pass
        elif message.text == "/disapprove":
            pass
        elif message.text == "/get_all":
            pass
        elif message.text == "/get_as_a_receiver":
            pass
        elif message.text == "/get_as_sender":
            pass
        else:
            bot.send_message(message.from_user.id, "Can't understand you write /List_of_commands.")

    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    start()
