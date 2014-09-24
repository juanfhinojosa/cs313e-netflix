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
