import os
import getpass
import sys
import pyautogui

from first_time import first_time_login
from myCrypto import decrypt_oracle
from converter import set_english_ime, set_chinese_ime

'''
todo:
优化用户密码采集框
增加重设密码选项
增加判断：vpn未打开，vpn已开启
优化error handling
'''

# def run_VPN():
#     custom_user = getpass.getuser()

#     def GetDesktopPath():
#         return os.path.join(os.path.expanduser("~"), 'Desktop')

#     desktop_path = GetDesktopPath()

#     users_dir = desktop_path[0:len(desktop_path)-len(custom_user)-9]

#     lnk_path = []
#     for i in os.listdir(users_dir):
#         print(i)
#         sub_dir = os.path.join(users_dir, i)
#         sub_dir = os.path.join(sub_dir, 'Desktop')
#         sub_dir = os.path.join(sub_dir, 'FortiClient VPN.lnk')
#         print(sub_dir)

#         if os.path.exists(sub_dir):
#             print('---------Found---------')
#             print(sub_dir)
#             lnk_path.append('"' + sub_dir + '"')


#     print(lnk_path)
#     for i in lnk_path:
#         try:
#             res = subprocess.Popen(i, shell=True)
#             sleep(5)
#             res.terminate()
#             print("---------run---------")
#             break
#         except Exception as e:
#             print(e)
#             print("---------run failed---------")
#             continue


def findElement(a):
    if not os.path.isfile(a):
        print('找不到图片')
        sys.exit()

    buttonLocation = None
    while buttonLocation == None:
        print("等待"+a+"出现")
        try:
            buttonLocation = pyautogui.locateOnScreen(a, confidence=0.8)
        except Exception as e:
            print('出异常了', e)
            continue
    return buttonLocation


def searchElement(a):
    if not os.path.isfile(a):
        print('找不到图片')
        sys.exit()
    buttonLocation = None
    try:
        buttonLocation = pyautogui.locateOnScreen(a, confidence=0.8)
    except Exception as e:
        print('出异常了', e)
    return buttonLocation


def clickElement(a):
    print("点击图片")
    btn_pos = findElement(a)
    x, y = pyautogui.center(btn_pos)
    pyautogui.click(x, y)


def auto_run():
    set_english_ime()
    first_time_login()
    pwd = os.getcwd()
    print(pwd)
    with open('data' + os.sep + 'data.txt', 'r') as f:
        email = f.readline()
        password = f.readline()
    password = decrypt_oracle(password)
    custom_user = getpass.getuser()

    def GetDesktopPath():
        return os.path.join(os.path.expanduser("~"), 'Desktop')

    desktop_path = GetDesktopPath()

    users_dir = desktop_path[0:len(desktop_path)-len(custom_user)-9]

    lnk_path = []
    for i in os.listdir(users_dir):
        print(i)
        sub_dir = os.path.join(users_dir, i)
        sub_dir = os.path.join(sub_dir, 'Desktop')
        sub_dir = os.path.join(sub_dir, 'FortiClient VPN.lnk')
        print(sub_dir)

        if os.path.exists(sub_dir):
            print('---------Found---------')
            print(sub_dir)
            lnk_path.append('"' + sub_dir + '"')
    pyautogui.PAUSE = 0.5
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite(lnk_path[0])
    pyautogui.press('enter')
    #---------- 点击登录 ----------#
    clickElement('data' + os.sep + 'btn.png')

    #---------- 输入账号密码 ----------#
    findElement('data' + os.sep + 'ucl.png')
    pyautogui.typewrite(message=email)
    pyautogui.press('enter')
    findElement('data' + os.sep + 'ucl.png')
    pyautogui.typewrite(message=password)
    pyautogui.press('enter')
    findElement('data' + os.sep + 'ucl.png')
    pyautogui.press('enter')

    set_chinese_ime()


auto_run()
print("-------auto run--------")
