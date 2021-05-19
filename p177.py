class Square:
	square_list = []
	def __init__(self,name):
		self.name = name
		self.square_list.append(self.name)

>>> s1 = Square("world!")
>>> s2 = Square("Hello!")
>>> print(Square.square_list)
['world!', 'Hello!']




class Square:
	def __init__(self,name):
		self.name = name
		
	def __repr__(self):
		return "{}by{}by{}by{}".format(self.name,self.name,self.name,self.name)

	
>>> s1 = Square(29)
>>> print(s1)




def number(x,y):
	if x == y:
		print(x is y)
	else:
		print(x is y)

		
>>> number(4,4)
True
>>> number(4,5)
False



