import json


def read_json():
	with open('data.json', 'r') as f:
		data = json.load(f)

		dic = { 'C++' : [' ', 0],
				'PHP' : [' ', 0],
				'JavaScript' : [' ', 0],
				'Python' : [' ', 0],
				'C#' : [' ', 0],
				'Haskell' : [' ', 0],
				'Java' : [' ', 0],
				'Ruby' : [' ', 0],
				'C' : [' ', 0],
				'CSS' : [' ', 0] }

		for person in data["people"]:
			name = person['first_name']
			second_name = person['last_name']
			for shit in person["skills"]:
				if shit['level'] > dic[shit['name']][1]:
					dic[shit['name']][1] = shit['level']
					dic[shit['name']][0] = name + " " + second_name

	return dic


print(read_json())