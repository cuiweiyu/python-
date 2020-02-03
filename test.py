import numpy as np
import pandas as pd

ss = pd.DataFrame(np.array([[2, 4], [1, 4]]), columns=['a', 'b'])
ss1 = pd.DataFrame(np.array([[1, 4], [1, 1]]), columns=['a', 'b'])
print(ss)
iter = np.array(pd.concat([ss, ss1])).tolist()
print(iter)

