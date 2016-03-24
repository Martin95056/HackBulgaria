import json
import random
import sys

def read_cars_json():
	with open ('cars.json', 'r') as j:
		data = json.load(j)

	return data

def read_results():
	with open ('results.json', 'r') as j:
		data = json.load(j)

	return data

def write_results(a):
	data = read_results()
	data['races'].append(a)

	with open('results.json', 'w') as jout:
		json.dump(data, jout)

	return data

def racers_for_the_track():
	all_given_racers = read_cars_json()

	all_cars = []
	racers_for_the_track = []

	for i in range(len(all_given_racers['people'])):
		curr = all_given_racers['people'][i]
		all_cars.append(Car(curr['car'], curr['model'], curr['max_speed']))

	for i in range(len(all_given_racers['people'])):
		curr = all_given_racers['people'][i]
		racers_for_the_track.append(Driver(curr['name'], all_cars[i], curr['skill_lvl']))

	return racers_for_the_track


class Car:

	def __init__(self, car, model, max_speed):
		self._car = car
		self._model = model
		self._max_speed = max_speed

	def __str__(self):
		return self._car + " " + self_model

	def __hash__(self):
		return hash(self._car + "afafafa")

	def __int__(self):
		return self._max_speed


class Driver:

	def __init__(self, name, car, skill_lvl):
		self._name = name
		self._car = car
		self._skill_lvl = skill_lvl

	def __str__(self):
		return self._name

	def __int__(self):
		return self._car._max_speed

	def __eq__(self, other):
		return int(self) == int(other)

	def __lt__(self, other):
		return int(self) < int(other)

	def get_max_speed(self):
		return self._car._max_speed

class Race:

	def __init__(self, drivers):
		self._drivers = drivers
		self._crash_chance = random.randint(4, 10)
		self._has_crashed = []
		self._table = {}

	def generate_random_number(self):
		for i in self._drivers:
			if i._name[-1] == 'a':
				return 5

			if i._car == 'Opel':
				return 4

		rand = random.randint(1, 5)
		return rand

	def crash(self):
		for i in self._drivers:
			if i._skill_lvl >= self._crash_chance:
				r = self.generate_random_number()

				formula = r * i.get_max_speed() / 100

			elif i._skill_lvl < self._crash_chance:
				r = self.generate_random_number()

				formula = (self._crash_chance - i._skill_lvl) * r * i.get_max_speed() / 100
			
			if formula >= 20:
				self._has_crashed.append(i._name)

		return self._has_crashed

	def bubble_sort(self):
	    for passnum in range(len(self._drivers) -1, 0, -1):
	        for i in range(passnum):
	            if self._drivers[i] < self._drivers[i + 1]:
	                temp = self._drivers[i]
	                self._drivers[i] = self._drivers[i + 1]
	                self._drivers[i + 1] = temp
	
	def race(self):
		self.crash()
		self.bubble_sort()

		qualifiers = []
		score_list = [8, 6, 4]

		for i in self._has_crashed:
			print("Unfortunatelly, {} has crashed.".format(i))

		for racer in self._drivers:
			if racer._name not in self._has_crashed:
				qualifiers.append(racer)

		if len(qualifiers) < 3:
			for i in range(len(qualifiers)):
				self._table[str(qualifiers[i])] = score_list[i]

		else:
			for i in range(3):
				self._table[str(qualifiers[i])] = score_list[i]

		write_results(self._table)
		return self._table


def main():
	racers = racers_for_the_track()
	
	if sys.argv[1] == 'start':
		print('Starting a new Grand Pri called {0} with {1} races.'.format(sys.argv[2], sys.argv[3]))
		print("Running {} races...\n".format(sys.argv[3]))

		for i in range(1, int(sys.argv[3]) + 1):
			temp = Race(racers)
			print('RACE #{}'.format(i))
			print("~~~~ START ~~~~")
			print(temp.race())
			print('\n')

if __name__ == '__main__':
	main()
