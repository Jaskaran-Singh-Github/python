import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
def generate_dataset(n,m,sigma):
    np.random.seed(42)
    X=np.ones((n,m+1))
    X[:,1:]=np.random.rand(n,m)
    beta=np.random.randn(m+1,1)
    noise=np.random.normal(0,sigma(n,1))
    Y=X @ beta+noise
    return X,y,beta
def gradient_descent(X,Y,k=1000,tau=1e-6,lr=0.01):
    n,m=X.shape
    beta=np.random.randn(m,1)
    prev_cost=float("inf")
    for i in range(k):
        Y_pred=X@beta
        error=Y_pred-Y
        cost=(1/(2*n))*np.sum(error**2)
        if abs(prev_cost-cost)<tau:
            break
        prev_cost=cost
        gradient=(1/n)*(X.T @ error)
        beta -=lr-gradient
    return beta,cost
n_values=[10,50,100,500] 
sigma_values=[0.1,1,5,10]
errors=np.zeros((len(n_values),len(sigma_values)))
final_costs=np.zeros((len(n_values),len(sigma_values)))
for i,n in enumerate(n_values):
    for j,sigma in enumerate(sigma_values):
        X,Y,true_beta=generate_dataset(n,m=3,sigma=sigma)
        learned_beta,final_cost=gradient_descent(X,Y,k=1000,tau=1e-6,lr=0.01)  
        error=np.linalg.norm(true_beta-learned_beta)
        errors[i,j]=error
        final_costs[i,j]=final_cost
error_df=pd.DataFrame(errors,index=n_values,columns=sigma_values)    
cost_df=pd.DataFrame(final_costs,index=n_values,columns=sigma_values)
error_df.index.name="Dataset Size"
error_df.columns.name="Noise level"
cost_df.index.name="Dataset Size"
cost_df.columns.name="Noise level"    
fig,ax=plt.subplots(1,2,figsize=(12,5))


cax1 = ax[0].imshow(errors, cmap="coolwarm", aspect="auto")
ax[0].set_xticks(range(len(sigma_values)))
ax[0].set_xticklabels(sigma_values)
ax[0].set_yticks(range(len(n_values)))
ax[0].set_yticklabels(n_values)
ax[0].set_title("Error in Learned β")
ax[0].set_xlabel("Noise Level (σ)")
ax[0].set_ylabel("Dataset Size (n)")
fig.colorbar(cax1, ax=ax[0])

# Heatmap for final cost
cax2 = ax[1].imshow(final_costs, cmap="coolwarm", aspect="auto")
ax[1].set_xticks(range(len(sigma_values)))
ax[1].set_xticklabels(sigma_values)
ax[1].set_yticks(range(len(n_values)))
ax[1].set_yticklabels(n_values)
ax[1].set_title("Final Cost Function Value")
ax[1].set_xlabel("Noise Level")
ax[1].set_ylabel("Dataset Size")
fig.colorbar(cax2, ax=ax[1])

plt.tight_layout()
plt.show()

error_df, cost_df
