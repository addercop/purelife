#!/usr/bin/python
import time

def view(squares):
	ret = ""
	for y in range(10,-11,-1):
		for x in range(-10,11):
			if (y,x) in squares:
				ret += "O"
			else:
				ret += "."
		ret += "\n"
	ret += "\n"
	return ret

def neighbors(point):
	offsets = [(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]
	for offset in offsets:
		yield (point[0]+offset[0], point[1]+offset[1])

def live_neighbors(squares, point):
	return set([neighbor for neighbor in neighbors(point) if neighbor in squares])

def dead_neighbors(squares, point):
	return set([neighbor for neighbor in neighbors(point) if neighbor not in squares])

def all_dead_neighbors(squares):
	adn = set()
	for point in squares:
		adn.update(dead_neighbors(squares, point))
	return adn

def survivors(squares):
	return set([point for point in squares if len(live_neighbors(squares,point)) in [2,3]])

def births(squares):
	dead_neighbors = all_dead_neighbors(squares)
	return set([point for point in dead_neighbors if len(live_neighbors(squares,point)) == 3])

def step(squares):
	return survivors(squares).union(births(squares))

def life(squares):
	for i in range(40):
		print view(squares)
		squares = step(squares)
		time.sleep(0.1)

def main():
	squares = set( [(2,0),(1,1),(0,-1), (0,0), (0,1)] )
	life(squares)

if __name__ == "__main__":
	main()
