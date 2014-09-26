def Cust_dict():

  '''
  Function will open file, read contents, evaluate data, and close file from the Average
  Customer Rating cache
  '''

  AverageRating = open('/u/prat0318/netflix-tests/savant-cacheUsers.txt' , 'r')
  AverageRating1 = eval(AverageRating.read())
  AverageRating.close()
  return AverageRating1

def Movie_dict():

  '''
  Function will open file, read contents, evaluate data, and close file from the Average
  Movie Rating cache
  '''

  AverageMviRating = open('/u/prat0318/netflix-tests/savant-cacheMovies.txt' , 'r')
  AverageMviRating1 = eval(AverageMviRating.read())
  AverageMviRating.close()
  return AverageMviRating1

def Answ_dict():

  '''
  Function will open, read, evaluate, and close answers from the Probe data
  '''

  Probe = open('/u/prat0318/netflix-tests/savant-cacheActual.txt' , 'r')
  Probe1 = eval(Probe.read())
  Probe.close()
  return Probe1

'''
Global variables used within multiple functions
'''

global_list = []
dict_customer = Cust_dict()
AverageMviRating = Movie_dict()
Answers_Dict = Answ_dict()

def Netflix_Read (standard_in) :

  '''
  Function will take in the standard_in read by Netflix_Solve, then
  pair up movie ids with its customer id for future computations
  '''

  for items in standard_in:
    items = items.rstrip()
    if ":" in items:
      movieID = items.replace(":", "")
    else:
      global_list.append([movieID, items])

  return global_list

def root_mean_squared_error (actual_list, prediction_list) :

  '''
  Function will compute the root mean squared error for each pair of actual 
  answers and our predictions, and will return the RMSE
  '''

  for i in range(len(actual_list)):
    assert(actual_list[i] > 0)
    assert(prediction_list[i] > 0)

  return ((sum(map(lambda x, y : (x - y) ** 2, actual_list, prediction_list)) / len(actual_list)) ** (1/2))

def Cust( customer ):

  '''
  Raise KeyErrors in case if input is not found in the cache, and if KeyError is raised return 3.22 (base value)
  If key is found return the value for the specific key
  '''

  try:
  	m = dict_customer[customer]
  except KeyError:
  	m = str(3.22)
  finally:
  	return m

def Mov( movie ):

  '''
  Raise KeyErrors in case if input is not found in the cache, and if KeyError is raised return 3.22 (base value)
  If key is found return the value for the specific key
  '''

  try:
  	b = AverageMviRating[str(movie)]
  except KeyError:
  	b = str(3.22)
  finally:
  	return b

def Answ( customer , movie ):

  '''
  Raise KeyErrors in case if input is not found in the cache
  If key is found return the value for the specific key
  '''

  try:
  	c = Answers_Dict[movie + ' ' + customer]
  except KeyError:
  	c = str()
  return c

def Predict( customer , movie ):

  '''
  Function will take in the customer id and movie id, which will use them
  to compute our prediction
  '''

  Cust_Diff = eval(Cust(customer)) - 3.22
  Movie_Diff = eval(Mov(movie)) - 3.22

  Prediction = 0.6 * Cust_Diff + 0.6 * Movie_Diff + 3.22

  return round(Prediction, 1) 

def Netflix_Solve(inFile , writeFile):

  '''
  Function will obtain a standard input and read its contents, then the
  program will find the RMSE and Prediction for every pair of customer id 
  and movie id
  '''

  inFile_contents = Netflix_Read(inFile)
  prediction_list = []
  actual_list = []
  track_movie_id = ''

  for n in inFile_contents:

  	movie_id, customer_id = n[0], n[1]
  	prediction = Predict(customer_id, movie_id)
  	prediction_list.append(prediction)
  	y = Answ(customer_id, movie_id)
  	actual_list.append(float(y))

  	if track_movie_id != movie_id:
  		track_movie_id = movie_id
  		writeFile.write(str(movie_id) + ':' + '\n')

  	writeFile.write(str(prediction) + '\n')

  rmse_output = root_mean_squared_error(actual_list, prediction_list)
  writeFile.write('RMSE = ' + str(round(rmse_output, 2)))