def logistic_regression_regularized(X, Y, k=1000, learning_rate=0.01, lambda_l1=0.0, lambda_l2=0.0):
    """
    Logistic Regression with L1 & L2 Regularization using Gradient Descent.

    Parameters:
        X (numpy.ndarray): Feature matrix.
        Y (numpy.ndarray): Binary target labels.
        k (int): Number of iterations.
        learning_rate (float): Step size for gradient descent.
        lambda_l1 (float): Strength of L1 regularization (Lasso).
        lambda_l2 (float): Strength of L2 regularization (Ridge).

    Returns:
        beta (numpy.ndarray): Learned coefficients.
    """
    n, m_plus_1 = X.shape
    beta = np.random.randn(m_plus_1, 1)  # Initialize coefficients

    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    for _ in range(k):
        # Compute predictions
        predictions = sigmoid(X @ beta)

        # Compute gradient with L1 and L2 regularization
        gradient = (X.T @ (predictions - Y)) / n
        gradient += lambda_l2 * beta  # L2 Regularization
        gradient += lambda_l1 * np.sign(beta)  # L1 Regularization

        # Update beta
        beta -= learning_rate * gradient

    return beta

# Example Usage
X, Y, beta_true = generate_dataset(n=100, m=3, theta=0.1)

# Train Logistic Regression with L1 & L2 Regularization
beta_learned = logistic_regression_regularized(X, Y, lambda_l1=0.1, lambda_l2=0.1)

# Print Results
print("True Beta:\n", beta_true)
print("\nLearned Beta with Regularization:\n", beta_learned)
