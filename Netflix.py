global_list = []
global_id = []

def Netflix_Read (r) :
  for items in r:
    items = items.rstrip()
    if ":" in items:
      movieID = items.replace(":", "")
    else:
      s = [movieID, items]
      global_list.append(s)
  return global_list

def root_mean_squared_error (x, y) :

  '''
  This program will do the following:
    1.  Take 'x' the actual value and 'y' our guess, as inputs
    2.  Compute Root-Mean-Squared-Error 
    3.  Output RMSE
  '''

  sum = 0

  for i in range(len(x)) :
    assert (len(x) == len(y)) # not sure if corrrect syntax
    sum += (y[i] - x[i]) ** 2

  rmse = (sum / len(x)) ** (1/2)

  assert (5 > rmse > 0)

  return rmse
# /u/prat0318/netflix-tests/

def Cust( customer ):
  
  AvgCustRt = 0
  AverageRating = open('/u/prat0318/netflix-tests/ctd446-userAverageRating.txt' , 'r')
  C = eval(AverageRating.readline())

  customer = str(customer)
  if customer in C:
    return C[customer]

  AverageRating.close()

def Mov( movie ):
  
  AvgMviRt = 0
  AverageMviRating = open('/u/prat0318/netflix-tests/ctd446-movieAverageRating.txt' , 'r')
  B = eval(AverageMviRating.readline())

  movie = str(movie)
  return B[movie]

  AverageMviRating.close()

def Answ( customer , movie ):



  Probe = open('/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt' , 'r')
  Answers_Dict = {}

  
  for line in Probe:
    CustnMov = line
    CustnMov = CustnMov.split()
    Answers = CustnMov[2]
    CustnMov = CustnMov[1] + CustnMov[0]
    Answers_Dict[CustnMov] = Answers
  customermovie = str(customer) + str(movie)
  return Answers_Dict[customermovie]

  Probe.close()

def Predict( customer , movie ):

  Total_Cust_Avg = 3.6741013034524364
  Total_Mov_Avg = 3.228137194500105

  Cust_Diff = Total_Cust_Avg - eval(Cust(customer))
  Movie_Diff = Total_Mov_Avg - eval(Mov(movie))

  Prediction = Cust_Diff + Movie_Diff + Total_Mov_Avg
  return Prediction

def Netflix_Print(w, i, j, v) :
  if i not in global_id :
    global_id.append(i)
    w.write(str(i) + ":" + '\n')
  w.write(str(v) + '\n')

def Netflix_Solve(r , w):
  a = Netflix_Read(r)
  if not a:
    return 
  for n in a:
    i, j = n[0], n[1]
    v = Predict(j, i)
    Netflix_Print(w, i, j, v)