A = []
for n, line in open('agent.py'):
	if 'Primary agent' in line:
		A.append(n)

B = [A[0]]
for i in range(1, len(A)):
	B.append(A[i]-A[i-1])


print B
