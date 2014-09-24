
def collatz_read (r) :

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
  '''
  for items in C:
    AvgCustRt += float(C[items])
  
  finalavg = (AvgCustRt / len(C))
  print(finalavg)
  '''
  customer = str(customer)
  if customer in C:
    return C[customer]

def Mov( movie ):
  
  AvgMviRt = 0
  AverageMviRating = open('/u/prat0318/netflix-tests/ctd446-movieAverageRating.txt' , 'r')
  B = eval(AverageMviRating.readline())
  '''
  for things in B:
    AvgMviRt += float(B[things])
  
  MvAvg = (AvgMviRt / len(B))
  print(MvAvg)
  '''
  movie = str(movie)
  return B[movie]

def Answ( customer , movie ):

  '''
  Probe = open('/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt' , 'r')
  Probe = eval(Probe.readline())
  
  for items in Probe:
    print(items)
  
  #return Probe[customer]
  return Probe
  '''

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

def Predict( customer , movie ):

  Total_Cust_Avg = 3.6741013034524364
  Total_Mov_Avg = 3.228137194500105

  Cust_Diff = Total_Cust_Avg - float(Cust(customer))
  Movie_Diff = Total_Mov_Avg - float(Mov(movie))

  Prediction = Cust_Diff + Movie_Diff + Total_Mov_Avg
  return Prediction

def Netflix_Print(w, i, j, v) :
  w.write(str(i) + ':' + '\n')
  w.write(str(v) + '\n')

def Netflix_Solve(r , w):
  a = collatz_read(r)
  for n in a:
    i, j = n[0], n[1]
    v = Predict(i, j)
    Netflix_Print(w, i, j, v)

def main():
  
  print(Predict(1657689 , 4446))
  print(Answ(1657689 , 4446))
  
main()

  


