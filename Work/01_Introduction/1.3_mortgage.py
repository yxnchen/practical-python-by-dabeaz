# 1
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, 
# Stock Investment, and Bitcoin trading corporation. 
# The interest rate is 5% and the monthly payment is $2684.11.

principal = 500000.
rate = 0.05
payment = 2684.11
total_paid = 0.

while principal > 0:
    principal = principal * (1 + rate/12) - payment
    total_paid += payment

print('#1')
print("Total paid:", round(total_paid, 4))

# 2 extra payment: Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
principal = 500000.
rate = 0.05
payment = 2684.11
total_paid = 0.
total_month = 0

while principal > 0:
    total_month += 1
    if total_month <= 12:
        principal = principal * (1 + rate/12) - payment - 1000
        total_paid += payment + 1000
    else:
        principal = principal * (1 + rate/12) - payment
        total_paid += payment
    
print('#2')
print("Total paid:", round(total_paid, 4))
print("Total month:", total_month)

# 3 Making an Extra Payment Calculator
# pays an extra $1000/month for 4 years starting after the first five years have already been paid?
principal = 500000.
rate = 0.05
payment = 2684.11
total_paid = 0.
total_month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    total_month += 1
    if total_month >= extra_payment_start_month and total_month <= extra_payment_end_month:
        principal = principal * (1 + rate/12) - payment - extra_payment
        total_paid += payment + extra_payment
    else:
        principal = principal * (1 + rate/12) - payment
        total_paid += payment
    
print('#3')
print("Total paid:", round(total_paid, 4))
print("Total month:", total_month)

# 4 Making a table
# Modify the program to print out a table showing the month, total paid so far, and the remaining principal.
principal = 500000.
rate = 0.05
payment = 2684.11
total_paid = 0.
total_month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

print('#4')
while principal > 0:
    total_month += 1
    if total_month >= extra_payment_start_month and total_month <= extra_payment_end_month:
        
        principal = principal * (1 + rate/12) - payment - extra_payment
        total_paid += payment + extra_payment
    else:
        principal = principal * (1 + rate/12) - payment
        total_paid += payment
    print(total_month, '\t', round(total_paid, 2), '\t', round(principal, 2))

print("Total paid:", round(total_paid, 4))
print("Total month:", total_month)


# 5 Bonus
# While you’re at it, fix the program to correct for the overpayment that occurs in the last month.
principal = 500000.
rate = 0.05
payment = 2684.11
total_paid = 0.
total_month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

print('#5')
while principal > 0:
    total_month += 1
    if total_month >= extra_payment_start_month and total_month <= extra_payment_end_month:
        tmp = principal * (1 + rate/12) - payment - extra_payment
        if tmp < 0:
            total_paid += (principal * (1 + rate/12))
            principal = 0.
        else:
            principal = tmp
            total_paid += payment + extra_payment
    else:
        tmp = principal * (1 + rate/12) - payment
        if tmp < 0:
            total_paid += (principal * (1 + rate/12))
            principal = 0.
        else:
            principal = tmp
            total_paid += payment
    print(total_month, '\t', round(total_paid, 2), '\t', round(principal, 2))

print("Total paid:", round(total_paid, 2))
print("Total month:", total_month)

# mistery
print(int('123'))
print(float('1.23'))
print(bool('False'))
