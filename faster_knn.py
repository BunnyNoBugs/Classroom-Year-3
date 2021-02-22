import pandas as pd
from collections import defaultdict, Counter
import numpy as np


class FasterKNNClassifier:
    def __init__(self, n_quadrants=10):
        self.n_quadrants = n_quadrants
        self._quadrant_sizes = []
        self._quadrant2class = defaultdict(list)

    def _find_quadrant(self, x) -> tuple:
        quadrant = [round(x[i] / self._quadrant_sizes[i]) for i in range(len(x))]

        return tuple(quadrant)

    def _find_closest_quadrant(self, x) -> tuple:
        return min(self._quadrant2class, key=lambda i: np.linalg.norm(np.array(self._find_quadrant(x)) - np.array(i)))

    def fit(self, X: pd.DataFrame, y: pd.Series):
        for i in X:
            self._quadrant_sizes.append(X[i].max() - X[i].min() / self.n_quadrants)

        for i in range(len(X)):
            self._quadrant2class[self._find_quadrant(X.iloc[i])].append(y[i])
        self._quadrant2class = {i: Counter(self._quadrant2class[i]).most_common()[0][0] for i in self._quadrant2class}

    def predict(self, X: pd.DataFrame) -> list:
        y_pred = [self._quadrant2class[self._find_closest_quadrant(X.iloc[i])] for i in range(len(X))]

        return y_pred


def main():
    knn = FasterKNNClassifier()
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [1, 2, 3]])
    knn.fit(df, ['c', 'b', 'a'])
    print(knn.predict(pd.DataFrame([[4, 5, 5], [1, 2, 3]])))


if __name__ == '__main__':
    main()
