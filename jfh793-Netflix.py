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

def Answ( customer ):

  '''
  Probe = open('/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt' , 'r')
  Probe = eval(Probe.readline())
  '''
  for items in Probe:
    print(items)
  '''
  #return Probe[customer]
  return Probe
  '''

  Probe = open('/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt' , 'r')
  Answers_Dict = {}

  CustnMov = Probe.readline()
  while CustnMov:
    CustnMov = CustnMov.rstrip ('\n')
    CustnMov = CustnMov.split()
    Answers = CustnMov[2]
    CustnMov = CustnMov[0] + CustnMov[1]
    Answers_Dict[CustnMov] = Answers
    CustnMov = Probe.readline()


def Predict( customer , movie ):

  Total_Cust_Avg = 3.6741013034524364
  Total_Mov_Avg = 3.228137194500105

  Cust_Diff = Total_Cust_Avg - float(Cust(customer))
  Movie_Diff = Total_Mov_Avg - float(Mov(movie))

  Prediction = Cust_Diff + Movie_Diff + Total_Mov_Avg
  return Prediction

def main():
  
  print(Predict(1657689 , 4446))
  
main()

  


