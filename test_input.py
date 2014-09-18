def main():
	import os
	# Open remote directory to read data
	for i in range (0, 17771):
		changing_num = str(1)
		while len(changing_num) < 7:
			changing_num = '0' + changing_num
		base = ('/u/downing/cs/netflix/training_set/mv_' + changing_num + '.txt')
		inFile = open(base , 'r')
	
		for line in inFile:
			print(line)
main()

