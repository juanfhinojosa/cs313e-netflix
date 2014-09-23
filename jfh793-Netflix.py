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

def Predict( customer , movie ):
  global C
  global B
  
  Total_Cust_Avg = 3.6741013034524364
  Total_Mov_Avg = 3.228137194500105
  
  Cust_Diff = Total_Cust_Avg - C[customer]
  Movie_Diff = Total_Mov_Avg - B[movie]
  
  return Cust_Diff + Movie_Diff + Total_Mov_Avg 

def main():
  
  AvgCustRt = 0
  AverageRating = open('/u/prat0318/netflix-tests/ctd446-userAverageRating.txt' , 'r')
  C = eval(AverageRating.readline())
  for items in C:
    AvgCustRt += float(C[items])
  
  finalavg = (AvgCustRt / len(C))
  print(finalavg)


  
  AvgMviRt = 0
  AverageMviRating = open('/u/prat0318/netflix-tests/ctd446-movieAverageRating.txt' , 'r')
  B = eval(AverageMviRating.readline())
  for things in B:
    AvgMviRt += float(B[things])
  
  MvAvg = (AvgMviRt / len(B))
  print(MvAvg)

  '''
  F = open('/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt' , 'r')
  File = F.read()
  File = File.split()
  #for i in range(0 , len(File) , 3):
    #print(File[i])
  '''

main()

