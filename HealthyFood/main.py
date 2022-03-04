##Libs
import pandas as pd
import numpy as np
from scipy.optimize import linprog

#Coise of Diet
Choosing_Diet = int(input('Выберите диету:\n Набор массы - 1 \n Поддержание массы - 2\n Уменьшение массы 3\n '))
if Choosing_Diet == 1:
    MinLim = 'MinLimitGaining'
    MaxLim = 'MaxLimitGaining'
elif Choosing_Diet == 2:
    MinLim = 'MinLimitMaintaining'
    MaxLim = 'MaxLimitMaintaining'
elif Choosing_Diet == 3:
    MinLim = 'MinLimitSlimming'
    MaxLim = 'MaxLimitSlimming'
else:
    print('Неккоректный выбор')

##Reading data
#List of Products
Table = pd.read_excel("HealthyFoodTable.xls", nrows=9)
Names_Of_Food = list(Table['Name'])
Calory = dict(zip(Names_Of_Food, Table['Calory']))
Protein = dict(zip(Names_Of_Food, Table['Protein']))
Fats = dict(zip(Names_Of_Food, Table['Fats']))
Carbs = dict(zip(Names_Of_Food, Table['Carbs']))
Cellulose = dict(zip(Names_Of_Food, Table['Cellulose']))
Water = dict(zip(Names_Of_Food, Table['Water']))
Price = dict(zip(Names_Of_Food, Table['Price']))

#Diet's limits
Limits = pd.read_excel("FoodLimits.xls", nrows=6)
OurLimit = list(Limits['Component'])
MinLimit = dict(zip(OurLimit, Limits[MinLim]))
MaxLimit = dict(zip(OurLimit, Limits[MaxLim]))

##Solving
Obj = [Price['Eggs'], Price['Tomatoes'], Price['Cucumbers'], Price['Rice'],
       Price['Apples'], Price['Macaroni'], Price['Сhicken'], Price['Fish'],
       Price['Water']]

ArrCalory = np.array([])
ArrProtein = np.array([])
ArrFats = np.array([])
ArrCarbs = np.array([])
ArrCellulose = np.array([])
ArrWater = np.array([])
for i in list(Table['Name']):
    ArrCalory = np.append(ArrCalory, [Calory[i]])
    ArrProtein = np.append(ArrProtein, [Protein[i]])
    ArrFats = np.append(ArrFats, [Fats[i]])
    ArrCarbs = np.append(ArrCarbs, [Carbs[i]])
    ArrCellulose = np.append(ArrCellulose, [Cellulose[i]])
    ArrWater = np.append(ArrWater, [Water[i]])
Left_p = [ArrCalory, ArrProtein, ArrFats, ArrCarbs, ArrCellulose, ArrWater]

ArrMinLim = np.array([])
ArrMaxLim = np.array([])
for k in list(Limits['Component']):
    ArrMinLim = np.append(ArrMinLim, MinLimit[k])
    ArrMaxLim = np.append(ArrMaxLim, MaxLimit[k])
opt = linprog(c=Obj, A_ub=Left_p, b_ub=ArrMaxLim, A_eq=Left_p, b_eq=ArrMinLim, bounds=(0, None))

##Printing results
print(opt)
Diet = {1: 'Набор массы ', 2: 'Поддержание массы', 3: 'Уменьшение массы'}
print('Диета для:', Diet[Choosing_Diet])
DailyList = list(opt.x*100)
print(opt.fun, 'рублей')
DailyListSorted = [i if i > 1 else 0 for i in DailyList]
for i in range(len(DailyListSorted)):
    print(Names_Of_Food[i], '=>', DailyListSorted[i], 'грамм/миллилитров')