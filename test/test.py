import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'reculsive_state_estimation'))

import probabilistic_basic

if __name__ == '__main__':
    gaus = probabilistic_basic.Gaussian(100, 10)
    print(gaus.get_probabilistic_integrated(0, 10,1))
