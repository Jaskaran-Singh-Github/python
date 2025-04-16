#Solution Task 1
import numpy as np
def generate_dataset(n,m,theta):
    X=np.random.randn(n,m)
    X=np.hstack((np.ones((n,1)),X))
    beta=np.random.randn(m+1,1)
    logits = X @ beta
    probabilites=1/(1+np.exp(-logits))
    Y=(probabilites>=0.5).astype(int)
    noise=np.random.binomial(1,theta,size=(n-1))
    Y=np.abs(Y-noise)
    return X,Y,beta
n,m,theta=1000,5,0.1
X,Y,beta=generate_dataset(n,m,theta)
print("Shape of X:",X.shape)
print("Shape of Y:",Y.shape)    
print("Beta Cofficients:\n",beta)