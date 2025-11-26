from datetime import date, datetime, timedelta

today = date.today()
print("Dzisiejsza data:", today)  # Dzisiejsza data: 2025-11-26
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualna godzina:", time)
# Aktualna godzina: 2025-11-26 13:56:50.355112

print(today.year)
print(today.day)
# 2025
# 26

formated_date = datetime.now().strftime("%d/%m/%Y")
print("Sformatowana data:", formated_date)  # Sformatowana data: 26/11/2025

# H:M
formated_time = datetime.now().strftime("%H:%M:%S")
print("Czas:", formated_time)  # Czas: 14:03:39
# print("Radek")

formated_time_12h = datetime.now().strftime("%I:%M:%S %p")
print("Czas:", formated_time_12h)  # Czas: 02:05:09 PM
# print("Radek")

# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print("Jutro będzie:", tomorrow)  # Jutro będzie: 2025-11-27

#  26/11/2025
object_data = datetime.now().strptime("26/11/2025", "%d/%m/%Y")
print(object_data)
print(type(object_data))
# 2025-11-26 00:00:00
# <class 'datetime.datetime'>
