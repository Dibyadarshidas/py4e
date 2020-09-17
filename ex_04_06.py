def computepay(hours, rate):
    print('In computepay', hours, rate)
    if hours > 40:
        reg = hours * rate
        otp = (hours-40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    print('returning', pay)
    return pay
hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))
ap = computepay(hours, rate)
print("pay", ap)