class Tree: # Основной класс
	def __init__(self,name): # Создание объекта
		self.name = name
		self.age = 0
		self.height = 0
		self.moath = 1
		self.plod = 0

	def info(self): # Инфо о дереве, сруб дерева
		if self.height >= 100:
			self.height = 2
			print('[!] Дерево срубили')
		else:
			StopIteration()
		return f'{self.name}, {self.height}, {self.age},{self.moath},{self.plod}'

	def grow(self): # Выращивание
		self.height = self.height + self.age + 1
		self.moath = self.moath + 1
		if self.moath >= 6:
			self.plod = self.plod + 12
		if self.moath >= 12:
			self.age = self.age + 1
			self.moath = self.moath - 12

	def chose(self): # Новое дерево
		self.age = 0
		self.height = 0
		self.moath = 1
		self.plod = 0

# Строчки для запуска
	tree = Tree('oak')
	tree.grow()
	tree.info()