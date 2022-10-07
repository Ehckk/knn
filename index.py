from math import sqrt
from random import random

class DataPoint:
	def __init__(self, x, y, index):
		self.__x = x
		self.__y = y
		self.__index = index

	def getIndex(self):
		return self.__index

	def getPoint(self):
		return [self.__x, self.__y]

class KNN:
	def __init__(self, data=[]) -> None:
		self.__data = data

	def getData(self):
		return self.__data

	def getSize(self):
		return len(self.__data)

	def generatePoints(self, amount, limit):
		self.__data = []
		for i in range(0, amount, 1):
			x = round(random() * limit, 2)
			y = round(random() * limit, 2)
			point = DataPoint(x, y, i)
			print([x, y])
			self.__data.append(point)

	def nearestNeighbors(self, target, k):
		(x1, y1) = target
		distances = []
		for point in self.__data:
			(x2, y2) = point.getPoint()
			d = round(sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2)), 2)
			distances.append((d, point))
		# sort them
		distances.sort(key=lambda item: item[0])
		return distances[:k] if k < len(self.__data) else distances

def main():
	knn = KNN()
	active = True
	while (active):
		option1 = "\t1. Generate new points\n"
		option2 = "\t2. K-nearest neighbors of a point\n"
		option3 = "\t3. Display all points\n"
		i = int(input(f"Enter an option:\n{option1}{option2 + option3 if knn.getSize() > 0  else ''}\t4. Exit\n> "))
		if i == 1:
			n = int(input(f"Enter number of points to generate:\n> "))
			limit = int(input(f"Enter upper bound of generated points:\n> "))
			knn.generatePoints(n, limit)
			print("Generated points!")
			input("Press Enter to Continue\n> ")
		elif i == 2 and knn.getSize() > 0:
			x = int(input(f"Enter an x coordinate:\n> "))
			y = int(input(f"Enter an y coordinate:\n> "))
			k = int(input(f"Enter a number of neighboring points to search for (k):\n> "))
			print(f"{k} closest points: to {x, y}:")
			for i, value in  enumerate(knn.nearestNeighbors((x, y), k)):
				(d, point) = value
				print(f"{i + 1}: {point.getPoint()}({point.getIndex()}) - Distance: {d}")
			input("Press Enter to continue\n> ")
		elif i == 3 and knn.getSize() > 0:
			print([f"{point.getPoint()}" for point in knn.getData()])
			input("Press Enter to Continue\n> ")
		elif i == 4:
			active = False
			print("Goodbye!")
		else:
			print("Invalid input")

if __name__ == "__main__":
	main()
