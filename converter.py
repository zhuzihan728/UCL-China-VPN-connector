from win32con import WM_INPUTLANGCHANGEREQUEST
import win32gui
import win32api


def set_english_ime():
    # 0x0409为英文输入法的lid_hex的 中文一般为0x0804
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    im_list = win32api.GetKeyboardLayoutList()
    im_list = list(map(hex, im_list))
    result = win32api.SendMessage(hwnd, WM_INPUTLANGCHANGEREQUEST, 0, 0x0409)
    if result == 0:
        print("英文输入法切换成功！")
        

def set_chinese_ime():
    # 0x0409为英文输入法的lid_hex的 中文一般为0x0804
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    im_list = win32api.GetKeyboardLayoutList()
    im_list = list(map(hex, im_list))
    result = win32api.SendMessage(hwnd, WM_INPUTLANGCHANGEREQUEST, 0, 0x0804)
    if result == 0:
        print("中文输入法切换成功！")
