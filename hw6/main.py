import datetime

time = datetime.datetime.now()
name_is_file = 'calendar.txt'
file = open(name_is_file, 'w')
file.write("Day - " +  str(time.day))
file.write("\nMonth - " + str(time.month))
file.write("\nYear - " + str(time.year))

print ("Приветствую вас")

file = open(name_is_file, 'r')

print (file.read())