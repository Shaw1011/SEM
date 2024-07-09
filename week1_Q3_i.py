def calculate_ci(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    ci = amount - principal
    return ci

principal = float(input("principal amount: "))
rate = float(input("rate of interest: "))
time = int(input("number of periods: "))

ci = calculate_ci(principal, rate, time)
print(f"The compound interest is: {ci:.2f}")
