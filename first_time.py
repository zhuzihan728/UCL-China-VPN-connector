import os
import pyautogui
from myCrypto import encrypt_oracle


def first_time_login():
    keeper_file = 'data' + os.sep + 'data.txt'
    if (os.path.isfile(keeper_file)):
        return False

    email = ""
    password = ""
    while email == "":
        email = pyautogui.prompt(text='', title='', default='')

    while password == "":
        password = pyautogui.password(text='', title='', default='', mask='*')

    with open('data' + os.sep + 'data.txt', 'w') as f:
        f.writelines([email, "\n", encrypt_oracle(password)])
    return True
