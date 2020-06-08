import argparse

parser = argparse.ArggumentParser(description='')
parser.add_argument('--readfile', dest='readfile',
	help='file to be read')

from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

import gensim
from gensim.models import Word2Vec as w2v

warnings.filterwarnings(action='ignore')

args = parser.parse_args()

readfile = args.readfile

model = {}

model['cbow'] = create_model(filename=filename)
model['sg'] = create_model(filename=filename, sg=1)


class Set:
	def __init__(self, contents=None, filename=None, text=None):
		self.filename = filename
		self.text = text
		self.contents = contents
		if not contents:
			self.clean_contents()
		if not self.filename:
			self.model = create_model(filename=filename)
		else:
			self.model = create_model(text=text)

	def create_model(self, min_count=1, size=100, window=5, sg=0):
		if not filename==None:
			token = file_tokenize(filename)
		else:
			token = text_tokenize(text)
		return w2v(token, min_count=min_count,
			size=100, window=5)

	def text_tokenize(self):
		data = []
		text = self.text.replace('\n', ' ').lower()
		for i in sent_tokenize(text):
			data.append(word_tokenize(i))
		return data

	def file_tokenize(self):
		data = []
		with open(self.filename) as f:
			txt = f.read().replace('\n', ' ').lower()
			for i in sent_tokensize(txt):
				data.append(word_tokenize(i))
		return data

	def clean_contents(self):
		self.text = ''
		for i, a in self.contents:
			text = a.strip()
			self.contents[i] = text
			self.text += text + ' '
		self.text = self.text[:-1]




















