time = int(input('Введите вермя в секундах:'))

hour = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60

print("Время в формате чч:мм:сс - ", hour, ":", minutes, ":", seconds)