import time

def viktor_belota():
	print('Enter command>')

	user_choise = input()
	command = user_choise.split(" ")
	return command

def main():
	print('Hello and Welcome!\nChoose an option.\n1. meal - to write what are you eating now.\n2. list <dd.mm.yyyy> - lists all the meals that you ate that day,\n3. finish - Exit')

	spisache = []
	dic = {}

	while True:
		list_command = viktor_belota()
		if list_command[0] == 'finish':
			break

		elif list_command[0] == 'meal':
			spisache.append (list_command[1])
			print('Ok it is saved!\n')

		data = open('meal_list.txt', 'w')
		for i in spisache:
			data.write('meal ')
			data.write(i)
			data.write('\n')
		data.close()

		dic[time.strftime("%d.%m.%Y")] = spisache
		data2 = open('dic_list.txt', 'w')
		data2.write (dic)
		data2.write ('\n')
		data2.close()

		if list_command[0] == 'list':
			print(dic[list_command[1]])




if __name__ == '__main__':
	main()