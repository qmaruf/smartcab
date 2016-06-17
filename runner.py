import os

for alpha in range(0, 11):
	for gamma in range(0, 11):
		alpha1 = alpha/10.0
		gamma1 = gamma/10.0
		cmd = '/usr/bin/python smartcab/agent.py %f %f  | tee agent.log' % (alpha1, gamma1)
		os.system(cmd)

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

		out = '%f\t%f\t%f' % (alpha1, gamma1, good)
		print out
		fout = open('alphagamma.txt', 'a')
		fout.write(out+'\n')
		fout.close()
		# exit()