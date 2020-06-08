# test.py

from MetaClass import Clean
from MataClass import Crawler

# test_string = '''hi this is a simple test for the class,\
#  change the string to test different functions'''

# test = None
# def prep():
# 	return Clean(test_string)

# prep().Separate(gram=3).Close()
# prep().DeleteRedundant().Close()
# prep().DeletePunctuation().Close()
# prep().Capitalize().Close()
travis = TestCleaner('this is a test')
travis.Capitalize()

class TestCleaner(Clean):
	def __init__(self, text):
		super().__init__(text)

	def Capitalize(self):
		self = self.upper()

		return self

	def Separate(self):

		return self


	def DeletePunctuation(self,
			Punctuation=[',','.','-','"',"'","'S","S'"]
        ):
		for p in Punctuation:
			self.Text = self.Text.replace(p,'')
		return self

	def DeleteRedundant(self
            ,Words=['A','THE','AN','TO','AND','OR','NOT']
        ):
		for w in Words:
			self.Text = self.Text.replace(w,'')

		return self

	def Substitute(self, Oldletter, Newletter):
		self.Text = self.Text.replace(Oldletter, Newletter)

		return self

	def Close(self):
		return self.Text


class TestCrawler(Crawler):
	def __init__(self, name, source):
		super().__init__(name, source)

	def CrawlerRawData(self):
		return self

	def __RecordCrawlerTime(self):
		return self

	def ParseRawData(self):

	def Close(self):
		return self.ParsedData






