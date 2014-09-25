global_list = []
global_id = []
def Cust_dict():

  AverageRating = open('/u/prat0318/netflix-tests/savant-cacheUsers.txt' , 'r')
  return eval(AverageRating.read())
  AverageRating.close()

def Movie_dict():
  AverageMviRating = open('/u/prat0318/netflix-tests/ctd446-movieAverageRating.txt' , 'r')
  B = eval(AverageMviRating.read())
  return B
  AverageMviRating.close()

def Answ_dict():
  Probe = open('/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt' , 'r')
  Answers_Dict = {}
  
  for line in Probe:
    CustnMov = line
    CustnMov = CustnMov.split()
    Answers = CustnMov[2]
    CustnMov = CustnMov[1] + CustnMov[0]
    Answers_Dict[CustnMov] = Answers

  Probe.close()
  return Answers_Dict


dict_customer = Cust_dict()
B = Movie_dict()
Answers_Dict = Answ_dict()

def Netflix_Read (r) :
  for items in r:
    items = items.rstrip()
    if ":" in items:
      movieID = items.replace(":", "")
    else:
      s = [movieID, items]
      global_list.append(s)
  return global_list

def root_mean_squared_error (a, p) :
  v = sum(map(lambda x, y : (x - y) ** 2, a, p))
  return ((v / len(a)) ** (1/2))

def Cust( customer ):
 try:
  m = dict_customer[customer]
 except KeyError:
  m = 3.6741013034524364

 if customer in dict_customer:
  return m

def Mov( movie ):
  
  movie = str(movie)
  if movie in B:
    return B[movie]

def Answ( customer , movie ):

  customermovie = str(customer) + str(movie)
  if customermovie in Answers_Dict:
    return Answers_Dict[customermovie]

def Predict( customer , movie ):

  Total_Cust_Avg = 3.6741013034524364
  Total_Mov_Avg = 3.228137194500105

  if eval(Cust(customer)) > Total_Cust_Avg :
    Cust_Diff = eval(Cust(customer)) - Total_Cust_Avg
  else:
    Cust_Diff = Total_Cust_Avg - eval(Cust(customer))
  if eval(Mov(movie)) > Total_Mov_Avg :
    Movie_Diff = eval(Mov(movie)) - Total_Mov_Avg
  else:
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
  prediction_list = []
  actual_list = [] 
  for n in a:
    i, j = n[0], n[1]
    v = Predict(j, i)
    prediction_list.append(v)
    y = Answ(j, i)
    actual_list.append(float(y))
    Netflix_Print(w, i, j, v)
  z = root_mean_squared_error(actual_list, prediction_list)
  w.write('RMSE = ' + str(z))