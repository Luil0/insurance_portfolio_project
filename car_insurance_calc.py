# importing datetime
import datetime
from sqlite3 import Timestamp
from types import NoneType
from dateutil.relativedelta import relativedelta

# input loan info

def monthly_payments():
    monthly_payment = float(input("What is your monthly payment: "))
    total_loan_amnt = float(input("What is your total loan amount: "))
    interest_rate = float(input("What is your intrest rate if none type 0: "))
    print( intrest_payments(total_loan_amnt, interest_rate, monthly_payment), date_paid(total_loan_amnt, monthly_payment, interest_rate))

# returns number of payments needed to payoff loan

def intrest_payments(loan_amnt, intrest_rate, monthly_pay):
    intrest_loan = loan_amnt * (intrest_rate / 100)
    intrest_loan_amnt = loan_amnt + intrest_loan
    total_num_pay = float(intrest_loan_amnt/monthly_pay)
    return "you have " + str(total_num_pay) + " payments left" + "\n"+ "Your total loan amount with interest would be " + str(int(intrest_loan_amnt))

# returns last day of payment 
def date_paid(loan_amnt, payment, int_rate):
    int_loan = (loan_amnt * (int_rate / 100)) + loan_amnt
    num_payment = int(int_loan/payment)
    years = float(num_payment/12)
    date_now = datetime.datetime.now()
    #new_thing
    yearto_days = years * 365
    daysto_hours = int((yearto_days % 1 ) * 24)
    future_date = date_now + datetime.timedelta(days=int(yearto_days), hours=daysto_hours)
    print(yearto_days, daysto_hours)
    return "\n" + "Your final payment would be " + str(future_date.date())


monthly_payments()






