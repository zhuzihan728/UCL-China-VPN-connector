# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py','converter.py','first_time.py','myCrypto.py'],
    pathex=['C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\charset_normalizer',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\Crypto',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\mouseinfo',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\PIL',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\pyautogui',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\pygetwindow',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\pymsgbox',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\pyrect',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\pyscreeze',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\pywin32_system32',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\win32',
    'C:\\Users\\mechabunny19c\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\win32con'],
    binaries=[],
    datas=[('C:\\Users\\mechabunny19c\\Desktop\\code\\fcConnector\\data','data')],
    hiddenimports=['altgraph', 'autopep8', 'certifi', 'charset-normalizer', 'comtypes', 'crypto', 'docopt', 'future', 'idna', 'MouseInfo', 'Naked', 'numpy', 'opencv-python', 'pefile', 'Pillow', 'PyAutoGUI', 'pycodestyle', 'pycryptodome', 'PyGetWindow', 'PyMsgBox', 'pyperclip', 'PyRect', 'PyScreeze', 'pytweening', 'pywin32', 'pywin32-ctypes', 'PyYAML', 'requests', 'shellescape', 'toml', 'urllib3', 'yarg'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
