import numpy as np

class  LinearRegression:
  def __init__(self):
    self.m = 1;
    self.b = 0
  def fit(self, x_train, y_train):
    self.x_train = np.array(x_train)
    self.y_train = np.array(y_train)
    self.calculate()
  
  def __createLine(self,x):
    return self.m * x + self.b

  def predict(self,x_test):
    return list(map(self.__createLine,x_test))

  def calculate(self):
    xmean = np.mean(self.x_train)
    ymean = np.mean(self.y_train)
    num = 0
    den = 0
    for idx,elt in enumerate(self.x_train):
      x = elt
      y = self.y_train[idx]
      num += (x - xmean) * (y - ymean)
      den += (x - xmean) * (x - xmean)
    self.m = num / den
    self.b = ymean - self.m * xmean
    return (self.m,self.b)


