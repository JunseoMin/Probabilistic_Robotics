import math
import numpy as np
from scipy.integrate import quad

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

    def get_probabilistic_integrated(self, x1, x2):
        
        if x1 > x2:
            x1, x2 = x2, x1
            print("!!x1,x2 changed!!")

        return quad(lambda x: 1/(math.sqrt(2*math.pi*self.variance)) * math.exp((-0.5)*(math.pow(x-self.mean,2))/(self.variance)),x1,x2)[0]

class Multivariate_Gaussian_Distribution:
    def __init__(self,covariance_mat,mean_vector) -> None:
        self.covariance_matrix = covariance_mat
        self.mean_vector = mean_vector
        self.cov_det = np.linalg.det(self.covariance_matrix)
        

    def get_probablistic(self, x):
        exp_term = np.exp(-0.5 * np.dot(np.dot((x - self.mean_vector).T, np.linalg.inv(self.covariance_matrix)), (x - self.mean_vector)))
        return (1 / (np.sqrt((2 * np.pi) ** len(x) * self.cov_det))) * exp_term
    

    def get_probablistic_integrated(self,x1,x2):
        integrated = lambda x: self.get_probablistic(x)
        return quad(integrated,x1,x2)[0]

class Covariance:
    def __init__(self) -> None:
        pass