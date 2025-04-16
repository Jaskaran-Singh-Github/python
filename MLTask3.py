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
