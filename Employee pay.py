# Employee Pay
hours = float(input('Hours:'))
rate = 10.5
pay = rate * hours
if hours > 40:
    # print('Overtime')
    overtime_pay = (hours - 40.0) * (rate * 0.5)
    ot_pay = pay + overtime_pay
    print("overtime", ot_pay)
else:
    print('Regular', pay)
