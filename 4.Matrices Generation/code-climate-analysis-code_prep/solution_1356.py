import os
print('Iterate over a root level path:')
path = '/tmp/'
for root, dirs, files in os.walk(path):
 print(root)
