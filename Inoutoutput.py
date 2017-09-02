'''
Created on Sep 3, 2017

@author: BHUSHAN
'''

from pip._vendor.distlib.compat import raw_input
fact=1
count=raw_input()
count=int(count)
for i in range(1,count+1):
      fact=fact*i
print(fact)

    

