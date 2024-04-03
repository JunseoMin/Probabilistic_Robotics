import math
import numpy as np

class Gaussian:
    def __init__(self,variance,mean) -> None:
        '''
        value for PDF
        '''
        self.mean = mean
        self.variance = variance
        self.standard_deviation = math.sqrt(variance)

    def get_probabilistic(self,x):
        return 1/(math.sqrt(2*math.pi*self.variance)) * math.exp((-0.5)*(math.pow(x-self.mean,2))/(self.variance))

    def get_probabilistic_integrated(self,x1,x2,dx = 0.1):
        sum = 0
        if x1 > x2:
            x1, x2 = x2, x1
            print("!!x1,x2 changed!!")

        while x1 != x2:
            sum += self.get_probabilistic(x1)
            x1 += dx

        return sum

    def get_mutivariate(self,x):
        '''
        x in np.array object
        '''
        
        return

class Covariance:
    def __init__(self) -> None:
        pass

