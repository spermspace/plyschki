from termcolor import colored, cprint
try:
	filename = input('File-Cover: ')
	with open(filename, 'rb') as file1:
		read1 = file1.read()

except FileNotFoundError:
	print(colored('[err] File: "' + str(filename) + '" is not defined!', 'red'))
	raise SystemExit

try:
	zipfile = input('Zip-File: ')
	with open(zipfile, 'rb') as file2:
		read2 = file2.read()
except FileNotFoundError:
	print(colored('[err] File: "' + str(zipfile) + '" is not defined!', 'red'))
	raise SystemExit

with open(filename, 'wb') as file3:
	file3.write(read1)
	file3.write(read2)
	print('[+] File: ' + str(filename) + ' successfully overwritten!')