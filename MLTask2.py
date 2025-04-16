import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost(X, Y, beta):
    m = len(Y)
    predictions = sigmoid(X @ beta)
    cost = -np.mean(Y * np.log(predictions) + (1 - Y) * np.log(1 - predictions))
    return cost

def logistic_regression_gd(X, Y, k, tau, learning_rate):
    n, m = X.shape
    beta = np.random.randn(m)  # Initialize beta randomly
    prev_cost = float('inf')

    for i in range(k):
        predictions = sigmoid(X @ beta)
        gradient = (X.T @ (predictions - Y.flatten())) / n  # Compute gradient
        beta -= learning_rate * gradient  # Update beta

        cost = compute_cost(X, Y, beta)

        if abs(prev_cost - cost) < tau:
            print(f"Converged at iteration {i} with cost: {cost}")
            break  # Stop if cost change is below threshold
        prev_cost = cost

    return beta, cost

# Example usage:
if __name__ == "__main__":
    # Generate dataset
    np.random.seed(42)  # For reproducibility
    n, m = 100, 5
    X = np.hstack((np.ones((n, 1)), np.random.randn(n, m)))
    beta_true = np.random.randn(m + 1)
    probabilities = sigmoid(X @ beta_true)
    Y = (probabilities >= 0.5).astype(int)

    # Train logistic regression model
    beta_learned, final_cost = logistic_regression_gd(X, Y, k=1000, tau=1e-6, learning_rate=0.01)

    # Print results
    print("Learned Beta:", beta_learned)
    print("Final Cost:", final_cost)  

import numpy as np
import matplotlib.pyplot as plt

def investigate_impact(n_values, theta_values, m=3):
    """
    Investigates how dataset size (n) and noise (θ) affect logistic regression learning.
    
    Parameters:
        n_values (list): Different dataset sizes.
        theta_values (list): Different noise probabilities.
        m (int): Number of independent variables.

    Returns:
        None (Prints results and plots β comparison).
    """
    for n in n_values:
        for theta in theta_values:
            # Generate Dataset
            X, Y, beta_true = generate_dataset(n, m, theta)

            # Train Logistic Regression
            beta_learned, _ = logistic_regression(X, Y)

            # Compute Mean Absolute Error (MAE)
            mae = np.mean(np.abs(beta_learned - beta_true))
            print(f"n={n}, θ={theta:.2f} → MAE={mae:.4f}")

            # Plot True vs. Learned β
            plt.plot(beta_true, 'ro-', label="True β")
            plt.plot(beta_learned, 'bo-', label="Learned β")
            plt.title(f"n={n}, θ={theta:.2f} (MAE={mae:.4f})")
            plt.legend()
            plt.show()

# Example Run
investigate_impact(n_values=[50, 200], theta_values=[0.0, 0.3])
