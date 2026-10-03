import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.metrics import accuracy_score, confusion_matrix


np.random.seed(42)
X = np.r_[np.random.randn(50,2)-[2,2], np.random.randn(50,2)+[2,2]]
y = np.r_[np.zeros(50), np.ones(50)]

# Plot dataset
plt.scatter(X[:,0], X[:,1], c=y)
plt.title("Synthetic Dataset")
plt.show()

# Train-test split (manual)
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# -------------------- SVM From Scratch --------------------
class SVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self, X, y):
        y_ = np.where(y <= 0, -1, 1)
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y_[idx] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    self.w -= self.lr * (2 * self.lambda_param * self.w - y_[idx] * x_i)
                    self.b -= self.lr * y_[idx]

    def predict(self, X):
        linear_output = np.dot(X, self.w) - self.b
        return np.sign(linear_output)

# -------------------- KNN From Scratch --------------------
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]


svm = SVM()
svm.fit(X_train, y_train)
svm_preds = svm.predict(X_test)
svm_preds = np.where(svm_preds == -1, 0, 1)

knn = KNN(k=5)
knn.fit(X_train, y_train)
knn_preds = knn.predict(X_test)


print("SVM Accuracy:", accuracy_score(y_test, svm_preds))
print("KNN Accuracy:", accuracy_score(y_test, knn_preds))

print("SVM Confusion Matrix:\n", confusion_matrix(y_test, svm_preds))
print("KNN Confusion Matrix:\n", confusion_matrix(y_test, knn_preds))

def plot_decision_boundary(model, X, y, title):
    x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
    y_min, y_max = X[:,1].min()-1, X[:,1].max()+1
    xx, yy = np.meshgrid(np.linspace(x_min,x_max,100),
                         np.linspace(y_min,y_max,100))
    grid = np.c_[xx.ravel(), yy.ravel()]
    preds = model.predict(grid)
    preds = np.where(preds == -1, 0, preds)
    plt.contourf(xx, yy, preds.reshape(xx.shape), alpha=0.3)
    plt.scatter(X[:,0], X[:,1], c=y)
    plt.title(title)
    plt.show()

plot_decision_boundary(svm, X, y, "SVM Decision Boundary")
plot_decision_boundary(knn, X, y, "KNN Decision Boundary")
