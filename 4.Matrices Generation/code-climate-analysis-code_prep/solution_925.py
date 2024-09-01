import numpy as np
matrix = [[1, 0, 'aaa'], [0, 1, 'bbb'], [0, 1, 'ccc']]
np.savetxt('test', matrix, delimiter='  ', header='string', comments='', fmt='%s')
