import numpy as np
print("First Monday in May 2017:")
print(np.busday_offset('2017-05', 0, roll='forward', weekmask='Mon'))
