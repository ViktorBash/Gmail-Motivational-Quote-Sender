import random
import config
from sendingemails import send_email

nice_messages = ["Life is tough, but you are tougher.", "Keep on pushing, one day at a time", "Dreams don't work until you do", "Quit talking, start doing",
                 "Failure is a greater teacher than success", "Apply yourself today"]
num = len(nice_messages)
random_num = random.randint(0, (num - 1))
chosen_msg = nice_messages[random_num]


config_file = open("config.py", "w")
config_file.writelines("EMAIL_ADDRESS = \"ENTER YOUR EMAIL\"")
config_file.writelines("\nPASSWORD = \"ENTER YOUR PASSWORD\"")
config_file.writelines("\nRECIEVER_ADDRESS = \"ENTER THE RECIEVING EMAIL\"")
config_file.writelines("\nSUBJECT = \"Motivational Sentence Of The Day\"")
config_file.writelines("\nMESSAGE = \"" + chosen_msg + "\"")
config_file.close()

send_email(config.SUBJECT, config.MESSAGE)

