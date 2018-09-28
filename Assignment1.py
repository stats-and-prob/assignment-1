import numpy as np


# Ex 1
def inner_product(x, y):
    """
    x and y are array-like
    """
    assert len(x) == len(y), 'Hey, the two vectors live in different dimensions!'
    return np.dot(np.array(x), np.array(y))


# Ex 2
def MAE(x, y):
    """
    x and y are array-like
    """
    assert len(x) == len(y), 'Hey, the two vectors live in different dimensions!'
    return np.absolute(np.array(y) - np.array(x)).sum() / len(x)


# Ex 3
def lead(x, n):
    """
    x is a list, n is a positive integer
    """
    return np.r_[x[n:], np.full(n, np.nan)]

def lag(x, n):
    """
    x is a list, n is a positive integer
    """
    return np.r_[np.full(n, np.nan), x[:-n]]


# Ex 4
def distance(X, y):
    """
    Input: X is an numpy array with shape (n,d), y is a vector in R^d. 
    Output: numpy array of length n
    """
    return np.linalg.norm(X-y, axis=1)





if __name__ == '__main__':
    X = np.array([[1,2],
                  [3,4]])
    y = [1,1]
    print(distance(X,y))