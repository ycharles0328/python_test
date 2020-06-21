import os
import re

##user_input = input('What is the name of your directory')
user_input = 'C:\DeepLearning'
directory = os.listdir(user_input)

##searchstring = input('What word are you trying to find?')
searchstring ='tensorflow'

def Parser():
	for fname in directory:
		if os.path.isfile(user_input + os.sep + fname):
			# Full path
			#f = open(user_input + os.sep + fname, 'r')
			with open(user_input + os.sep + fname, 'r') as f:
				for line in f:
					#print(f)
					
					#result = regex.search(line)
					#if searchstring in f.read():
					#	print('found string in file %s' % fname)
					#else:
					#	print('string not found')
					#print(result)
					
					#print(line)
					
					pattern = 'def'
					result = re.match(pattern, line)
					#print(result)
					if(result):
						##print(result)
						print(line)
					

		
		

if __name__ == '__main__':
    Parser()  