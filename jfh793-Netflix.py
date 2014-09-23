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

def main():
  
  AverageRating = open('/u/prat0318/netflix-tests/ctd446-userAverageRating.txt' , 'r')
  Customer = eval(AverageRating.readline())
    print(Customer)
  '''
  F = open('/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt' , 'r')
  File = F.read()
  File = File.split()
  #for i in range(0 , len(File) , 3):
    #print(File[i])
  '''

main()

