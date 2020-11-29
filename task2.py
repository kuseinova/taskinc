# 1. Создайте класс Car. Пропишите в __init__ параметры make, model, year, odometer, fuel.
# Пусть у показателя odometer будет первоначальное значение 0, а у fuel 70.
# Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте,
# хватит ли вам бензина из расчета того, что машина расходует 10 л / 100 км (1л - 10 км) . Если
# его хватит на введенное расстояние, то пусть этот метод добавляет эти километры к значению
# одометра, но не напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью приватного
# метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не Let’s drive!”. Если же бензина не
# хватит, то распечатайте “Let’s drive!”. Если же бензина не Need more fuel, please, fill more!”

# class Car:
#     """spending  benzin  for cars"""
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.fuel = 70
    
#     def drive(self,km):
#         needed_fuel = km / 10
#         if needed_fuel <= self.fuel:
#             self.__add_distance(km)
#             self.__subtract_fuel(needed_fuel)
#             print('Let\'s drive!')
#         else:
#             print('Need more fuel, please fill more!')


#     def read_oddometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it")


#     def __add_distance(self,km):
#         self.odometer += km 
#         return self.odometer

#     def __subtract_fuel(self,lit):
#         self.fuel -= lit

#     def __str(self):
#         print(f'Car {self.model} {self.year} {self.fuel} {self.odometr}')




# obj1 = Car('BMW', 'X&', '2020')
# obj1.drive(600)
# obj1.drive(100)
# obj1.drive(1)

# 2. Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня
# заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 %
# заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

# class Mobile:

#     __imei = "oc"
#     __battery = 100

#     if __battery == 0:
#         raise Exception ("Телефон разряжен")

#     def listen_music(self):
#         self.__battery -= 5
#         print('Do you listen to music')

#     def see_video(self):
#         if self.__battery >= 10:
#             self.__battery -=5
#             print('You watch the video')
#         elif self.__battery <= 10:
#             print("You can't watch videos")
        
#     def battery_charging(self):
#         self.__battery = 100

#     def get_info(self):
#         print(self.__battery)


# mobile = Mobile()
# mobile.listen_music()
# mobile.see_video()
# mobile.get_info()
# mobile.battery_charging()
# mobile.get_info()


# 3. Создайте класс правильной пирамиды с основанием в виде квадрата. Создайте
# непубличные атрибуты для длины основания и ребра её грани. Создайте публичные методы
# для задания атрибутов, а также для вычисления площади и объёма.

# class Pyramide:
#     def __init__(self, a, b):
#         self.__lenght_base = a
#         self.__length_rib = b

#     def get_data(self):
#         print(f'Base: {self.__lenght_base} cm')
#         print(f'Rib: {self.__length_rib} cm')

#     def setter(self, base, rib):
#         self.__lenght_base = base
#         self.__length_rib = rib

#     def get_volume(self):
#         print(f'Volume: {self.__lenght_base ** 2 * self.__length_rib / 3}')

#     def get_area(self):
#         print(f'Area: {self.__lenght_base * self.__lenght_base}')

# obj1 = Pyramide(25, 45)
# obj1.get_data()
# obj1.get_area()
# obj1.get_volume()