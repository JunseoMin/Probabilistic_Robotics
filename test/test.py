import sys
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'reculsive_state_estimation'))

import probabilistic_basic

if __name__ == '__main__':
    gaus = probabilistic_basic.Gaussian(100, 10)
    print(gaus.get_probabilistic_integrated(0, 0, 10))

    cov_mat = np.array([[2,1],[1,2]])
    mean_vec = np.array([1,2])
    multi_gaus = probabilistic_basic.Multivariate_Gaussian_Distribution
    print(multi_gaus.get_probablistic_integrated())
