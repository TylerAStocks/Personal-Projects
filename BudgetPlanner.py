#Program will be very simple, will access checking account,
#then divde balance by the amount of days left in the month
#which will then produce the amount of money I can spend per day

#First will just input my checking balance, and it does the math bits for me

import calendar
import datetime
from lxml import html
import requests





d = datetime.datetime.today()  #gets current date

dayCurrent = float(d.day)  #turns current date into an int value

daysTotal = calendar.monthrange(d.year,d.month)[1]  #gets total days this month

daysLeft = daysTotal - d.day   #calculates days left this month

balance = float(input("Enter Current Balance: ")) #Obtains user's account balance

dailyBudget = (balance/(daysLeft + 1))   #Calculates daily budget
weeklyBudget = dailyBudget * 7      #Calculates Weekly Budget
print("Daily budget is $" +str(dailyBudget))
print("Weekly Budget is $" +str(weeklyBudget))

