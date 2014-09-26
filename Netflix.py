def Cust_dict():
  AverageRating = open('/u/prat0318/netflix-tests/savant-cacheUsers.txt' , 'r')
  return eval(AverageRating.read())
  AverageRating.close()

def Movie_dict():
  AverageMviRating = open('/u/prat0318/netflix-tests/savant-cacheMovies.txt' , 'r')
  return eval(AverageMviRating.read())
  AverageMviRating.close()

def Answ_dict():
  Probe = open('/u/prat0318/netflix-tests/savant-cacheActual.txt' , 'r')
  return eval(Probe.readline())
  Probe.close()

global_list = []
dict_customer = Cust_dict()
AverageMviRating = Movie_dict()
Answers_Dict = Answ_dict()

def Netflix_Read (r) :
  for items in r:
    items = items.rstrip()
    if ":" in items:
      movieID = items.replace(":", "")
    else:
      global_list.append([movieID, items])
  return global_list

def root_mean_squared_error (a, p) :
  return ((sum(map(lambda x, y : (x - y) ** 2, a, p)) / len(a)) ** (1/2))

def Cust( customer ):
  try:
  	m = dict_customer[customer]
  except KeyError:
  	m = str(3.22)
  finally:
  	return m

def Mov( movie ):
  try:
  	b = AverageMviRating[str(movie)]
  except KeyError:
  	b = str(3.22)
  finally:
  	return b

def Answ( customer , movie ):
  try:
  	c = Answers_Dict[movie + ' ' + customer]
  except KeyError:
  	c = str()
  return c
def Predict( customer , movie ): 

  Cust_Diff = eval(Cust(customer)) - 3.22
  Movie_Diff = eval(Mov(movie)) - 3.22

  Prediction = 0.6 * Cust_Diff + 0.6 * Movie_Diff + 3.22

  return round(Prediction, 1) 

def Netflix_Solve(r , w):
  a = Netflix_Read(r)
  prediction_list = []
  actual_list = []
  count = ''
  for n in a:
  	i, j = n[0], n[1]
  	v = Predict(j, i)
  	prediction_list.append(v)
  	y = Answ(j, i)
  	actual_list.append(float(y))
  	if count != i:
  		count = i
  		w.write(str(i) + ':' + '\n')
  	w.write(str(v) + '\n')
  z = root_mean_squared_error(actual_list, prediction_list)
  w.write('RMSE = ' + str(round(z, 2)))