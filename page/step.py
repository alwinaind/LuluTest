class Step:
	def __init__(self, action, element, data=''):
		self.action = action
		self.element = element
		self.data = data
	def explain(self):
		print("This step {0} {1} into an {2} element of id {3}".format(self.action, self.data, self.element, self.element.id))
