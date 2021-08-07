import random

with open("fa.txt", "w") as out:
	for i in range(1, 1001):
		year = random.randint(1300, 1400)
		month = random.randint(1, 13)
		day = random.randint(1, 32)
		date = str(year) + "/" + str(month) + "/" + str(day)
		out.write(date + "\n")