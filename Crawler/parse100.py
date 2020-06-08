# parse100.py

def parse(filename):
	newline = '\n'
	names = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		for l in lines:
			if not l.strip()=='':
				names.append(l.replace('twitter.com/', '').strip())
	with open(filename, 'w') as f:
		for i, name in enumerate(names):
			if i==len(names)-1:
				f.write(name)
			else:
				f.write(name+newline)
