# 1
car_bots = {
    "Оптимус Прайм": "Грузовик Peterbilt 379",
    "Бамблби": "Chevrolet Camaro",
    "Джаз": "Porsche 935 Turbo"
}

for car_bot_key, car_bot_value in car_bots.items():
    print (car_bot_key, " - ", car_bot_value)

# 2

for car_bot_key in car_bots.keys():
    if car_bot_key == "Оптимус":
        print ("Оптимус Прайм прибыл")
    else:
        print ("Оптимус Прайм не прибыл")
    break

# 3
transformersWeight = {
    "Оптимус": 5000,
    "Бамблби": 2500,
    "Джаз": 3000
}

transformersWeight_all = 0

for transformerWeight in transformersWeight.values():
    transformersWeight_all += transformerWeight

print ("Вес всех трансформеров равен - ",transformersWeight_all)

# 4

megatron = ("Megatron", "Кибертронський истребитель Танк, Кибертронський звездолет.", "Десептикон")

for mega in megatron:
    if mega == "Десептиком":
        print ("Мегатрон - враг")
        break
        

# 5

car_bots.update({"Сентинел Прайм": "Пожарная машина"})

print (car_bots)