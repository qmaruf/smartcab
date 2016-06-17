A = []
good = 0
bad = 0
reward = 0
r = 1
cnt = 0
for n, line in enumerate(open('agent.log')):
	if 'reward' in line:
		parts = line.rstrip().split(' = ')
		reward += float(parts[len(parts)-1])
		cnt += 1
	if 'Primary agent' in line:
		print r, reward, reward/(cnt*1.0)
		reward = 0
		r += 1
		cnt = 0