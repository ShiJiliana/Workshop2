weight = float(input('Введите вес (в фунтах): '))
height = float(input('Введите высоты (в дюймах): '))
weight_kg = weight*0.45359237
height_m = height*0.0254
index = weight_kg/(height_m**2)
print(round(index, 2))

