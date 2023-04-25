# purchase plan creator

# import modules
import math

# set variables to defaults
# wage per hour in USD
wage = 15
# pay period in weeks
period = 2
# price of item in USD
price = 500
# tax withholding as a percentage of wage
withholding = 25
# allowance (how much of earned money is available to spend) as a percentage
allowance = 50
# total funds
funds = 0
# investment as a percentage of wage
investment = 33
# hours worked per week
hours = 10
# time
time = 0

# get mode
def getMode():
    mode = input("Which variable would you like to calculate?\n"+
    "Enter 'T' to calculate the time needed to make a purchase")
    if mode.toLowerCase()=="t":
        getTime()

#TODO create method for setting variables

#TODO create time calculation
def getTime(price, wage, hours, period, withholding, investment):
    paycheck = hours*period*wage - (hours*period*wage)/withholding
    net_income = paycheck-(paycheck/investment)
    time = 2*price/net_income
    rounded_time = math.ceil(time)
    print(str(rounded_time)+ " weeks")

getTime(700, 15, 10, 2, 25, 33)
