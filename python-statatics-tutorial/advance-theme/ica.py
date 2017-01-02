import numpy as np
from scipy import linalg
def test():
    data = np.random.random((5000,100))
    u,s,v = linalg.svd(data)
    pca = np.dot(u[:,:10].T,data)
if __name__ == '__main__':
   test()
