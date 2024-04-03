import math
import numpy as np

class Gaussian:
    def __init__(self,variance,mean) -> None:
        self.mean = mean
        self.variance = variance
        self.standard_deviation = math.sqrt(variance)

    def get_probabilistic(self,x):
        return 1/(math.sqrt(2*math.pi*self.variance)) * math.exp((-0.5)*(math.pow(x-self.mean,2))/(self.variance))

    def get_mutivariate(self,x):
        '''
        x in np.array object
        '''
        
        return

    def PDF(self):
        pass



class Covariance:
    def __init__(self) -> None:
        pass

