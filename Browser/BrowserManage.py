__author__ = 'sunny.yu2'


class BrowserManage(object):
	browsers = []
	def __init__(self):
		if(self.browsers.__len__()==0):
			self.browsers=[]

	def add_browser_queue(self,browser):
		self.browsers.append(browser)


	def get_browser(self,index=-1):
		return self.browsers[index]


	def clear_browsers(self):
		self.browsers.clear()
