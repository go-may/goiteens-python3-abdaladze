# 1
age = input("")
print ("Президент не может бы ть на посту больше 2 терминов")

# 2

George_Washington = 2
Thomas_Jefferson = 2
Herbert_Hoover = 1
Barack_Obama = 2
print (George_Washington)
print (Thomas_Jefferson)
print (Herbert_Hoover)
print (Barack_Obama)

# 3
text = input("")

if text == "2D":
    print ("Terraria")
elif text == "3D":
    print ("Minecraft")

# 4

cs = 2012
fortnite = 2017

if cs > fortnite:
    print ("Фортнайт старее")
elif cs < fortnite:
    print ("Кс гоу старее")

# 5
hp = 100

zombie = 5 * 5
skeleton = 15
spider = 2 * 40

monsters = zombie + skeleton + spider

if hp <= monsters:
    print ("You die")

elif hp > monsters:
    print ("Он виживет", hp - monsters)

# 6

pencil = int(input("")) # seconds
result = pencil * 120 # seconds
result2 = result / 60 # minutes
print ( result2 )

# 7
memory = 400 # МБ
programma = 200 # МБ
kilobat_mb = 1000 # в одном Мигобайте 1000 килобайтов

memory_kilobat = memory * kilobat_mb
programma_kilobat = programma * kilobat_mb

print ("Paint занимает на ", memory_kilobat - programma_kilobat, "килобайтов больше чем программа конкурентов")