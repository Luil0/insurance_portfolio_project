# importing datetime
import datetime
from sqlite3 import Timestamp
from types import NoneType
from dateutil.relativedelta import relativedelta



# # input loan info
def full_loan_payments():
    while True:
      try:
         monthly_payment = float(input("What is your monthly payment: "))
         total_loan_amnt = float(input("What is your total loan amount: "))
         interest_rate = float(input("What is your APR if none type 0: "))
         break
      except ValueError:
        print("This needs to be a number!")
    print( date_paid(total_loan_amnt, monthly_payment, interest_rate), due_date(total_loan_amnt, monthly_payment, interest_rate))


# # getting intrest rate for the loan and amount of payments. 
def date_paid(loan_amnt, payment, int_rate):
  monthly_int = float((((int_rate/ 100) / 365) * 30) * loan_amnt* 100)
  loan_with_int = float(monthly_int + loan_amnt)
  amnt_payments_year = float((loan_with_int/ payment)/12)
  return "Your total loan amount including interest is " + str(round(loan_with_int, 2)) + " dollars." + "\nYou have " + str(round(amnt_payments_year, 2)) + " years left to pay the loan off."

#getting the date the loan would be paid off including interest
def due_date(loan_amnt, payment, int_rate):
    int_loan = float((((int_rate/ 100) / 365) * 30) * loan_amnt* 100) + loan_amnt
    num_payment = int(int_loan/payment)
    years = float(num_payment/12)
    date_now = datetime.datetime.now()
    yearto_days = years * 365
    future_date = date_now + datetime.timedelta(days=int(yearto_days))
    return "\n" + "the approximate date your loan will be paid off is here: " + str(future_date.date())


full_loan_payments()
