billing = input("What was the store's billing this month? $")
cost = input("What was the store's cost this month? $")

if billing and cost:
    profit = int(billing) - int(cost)
    print(f"The store's profit was ${profit}.00")
else:
    print('Please fill in the billing and cost correctly.')