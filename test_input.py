def main():
	import os
	# Open remote directory to read data
	movieid_avg_rate = {}
	cust_avg_rate = {}
	for i in range (1, 1000):
		changing_num = str(i)
		while len(changing_num) < 7:
			changing_num = '0' + changing_num
		base = ('/u/downing/cs/netflix/training_set/mv_' + changing_num + '.txt')
		inFile = open(base , 'r')

		count = 0
		rating = 0

		for line in inFile:
			if line.find(':') != (-1) :
				movie_id = line[:-1]
			else:
				customer_id = line[:-(line.find(','))]
				line.replace(customer_id, '')
				rating += int(line[0])
		rating = rating / count

		movieid_avg_rate['movie_id'] = 'rating'			

		inFile.close()

	print(movieid_avg_rate)
main()

