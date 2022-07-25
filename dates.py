from datetime import datetime
import pytz

#this module returns the computer date
#my_time = datetime.datetime.now()
my_time = datetime.now()
print(my_time)

#this module returns the computer day
my_time1 = datetime.today()
print(my_time1)

#introduce into all parts of format today

print(f'Year: {my_time1.year}')
print(f'Month: {my_time1.month}')
print(f'Day: {my_time1.day}')

"""
format table:
%Y = Year
%m = month
%d = day
%H = Hour
%M = Minute
%S = Second
"""

# practice bellow 
# wiki list of tz
my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {my_str}')

my_str = my_datetime.strftime('Estamos en el año %Y')
print(f'Formato Random: {my_str}')

#time zones
bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogota: ", bogota_date.strftime("%d/%m/%Y ,%H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("CDMX: ", mexico_date.strftime("%d/%m/%Y ,%H:%M:%S"))

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone)
print("caracas: ", caracas_date.strftime("%d/%m/%Y ,%H:%M:%S"))