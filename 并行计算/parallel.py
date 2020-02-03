# -*- coding: UTF-8 -*-
import math
import time

from joblib import Parallel, delayed


def my_fun(i):
    """ We define a simple function here.
    """
    time.sleep(1)
    return math.sqrt(i ** 2)


if __name__ == '__main__':
    # 串行运行
    num = 10
    start = time.time()
    for i in range(num):
        my_fun(i)
    end = time.time()
    print('{:.4f} s'.format(end - start))

    # 并行运行
    start = time.time()
    # n_jobs is the number of parallel jobs
    Parallel(n_jobs=2)(delayed(my_fun)(i) for i in range(num))
    end = time.time()
    print('{:.4f} s'.format(end - start))
