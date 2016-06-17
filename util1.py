A = []
good = 0
bad = 0
for n, line in enumerate(open('agent.log')):
	if 'has' in line:
		A.append((n, 'has'))
		good += 1
	elif 'could' in line:
		A.append((n, 'could'))
		bad += 1

B = []
x = []
for i in range(0, len(A)):
	if A[i][1] == 'has':
		if i != 0:
			B.append(A[i][0]-A[i-1][0])
		else:
			B.append(A[i][0])
	else:
		B.append(0)
	x.append(i)




print B, len(B)

import numpy as np
import matplotlib.pyplot as plt

print x, len(x)


print 'good', good
print 'bad', bad
plt.bar(x,B)
plt.xlabel('n_trials')
plt.ylabel('move to reach destination')
axes = plt.gca()
axes.set_xlim([0, 5000])
plt.show()
