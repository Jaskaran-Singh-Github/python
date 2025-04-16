class LogisticRegression:
    """Logistic Regression with L1 & L2 Regularization."""
    
    def __init__(self, learning_rate=0.01, k=1000, lambda_l1=0.0, lambda_l2=0.0):
        """
        Initialize Logistic Regression model.

        Parameters:
            learning_rate (float): Step size for gradient descent.
            k (int): Number of iterations.
            lambda_l1 (float): L1 regularization strength (Lasso).
            lambda_l2 (float): L2 regularization strength (Ridge).
        """
        self.learning_rate = learning_rate
        self.k = k
        self.lambda_l1 = lambda_l1
        self.lambda_l2 = lambda_l2
        self.beta = None  # Will be set after training

    def sigmoid(self, z):
        """Apply sigmoid function."""
        return 1 / (1 + np.exp(-z))

    def fit(self, X, Y):
        """
        Train the logistic regression model using gradient descent.

        Parameters:
            X (numpy.ndarray): Feature matrix (n x m).
            Y (numpy.ndarray): Target labels (n x 1).

        Returns:
            self.beta (numpy.ndarray): Learned coefficients.
        """
        X = np.hstack((np.ones((X.shape[0], 1)), X))  # Add bias term
        n, m_plus_1 = X.shape
        self.beta = np.random.randn(m_plus_1, 1)  # Initialize coefficients

        for _ in range(self.k):
            # Compute predictions
            predictions = self.sigmoid(X @ self.beta)

            # Compute gradient with L1 and L2 regularization
            gradient = (X.T @ (predictions - Y)) / n
            gradient += self.lambda_l2 * self.beta  # L2 Regularization
            gradient += self.lambda_l1 * np.sign(self.beta)  # L1 Regularization

            # Update beta
            self.beta -= self.learning_rate * gradient

        return self.beta

    def predict(self, X):
        """
        Predict binary labels for input data.

        Parameters:
            X (numpy.ndarray): Feature matrix (n x m).

        Returns:
            numpy.ndarray: Predicted binary labels (0 or 1).
        """
        X = np.hstack((np.ones((X.shape[0], 1)), X))  # Add bias term
        return (self.sigmoid(X @ self.beta) >= 0.5).astype(int)

# Example Usage
X, Y, beta_true = generate_dataset(n=100, m=3, theta=0.1)

# Train Logistic Regression with L1 & L2 Regularization
model = LogisticRegression(learning_rate=0.01, lambda_l1=0.1, lambda_l2=0.1)
beta_learned = model.fit(X, Y)

# Predictions
predictions = model.predict(X)

# Print Results
print("True Beta:\n", beta_true)
print("\nLearned Beta with Regularization:\n", beta_learned)
print("\nPredictions:\n", predictions[:10])  # Show first 10 predictions
