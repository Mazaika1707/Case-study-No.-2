import datetime
from PIL import Image, ImageDraw, ImageFont
import numpy as np

 #1
print('Пожалуйста, укажите, когда вы родились, введите только числа!')
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))
TODAY = datetime.date.today()


#2
week_days=["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
week_num=datetime.date(year,month,day).weekday()
print(week_days[week_num])

#3
if year % 4 != 0:
    print('Високосный год.')

elif year % 100 == 0:
    if year % 400 == 0:
        print('Високосный год.')
    else:
        print('Год не високосный.')
else:
    print('Високосный год.')

 #4
print(f'ваш возрост - {TODAY.year - year - ((TODAY.month, TODAY.day) < (month, day))} !')

#5
day = str(day) 
month = str (month)
year = str (year)
text = (day + '  ' + month + '  ' + year)
myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getbbox(text)[2:]
img = Image.new("1",size,"black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ','*'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
print( "\n".join(strings))
