# w2l.py


def word2list(filename):
	names = []
	with open(filename, 'r') as f:
		for l in f.readlines():
			names.append(l.strip())
	return names