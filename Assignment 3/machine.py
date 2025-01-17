machine=6000
earn=1000
salvage=2000
rate=0.12
bank=6000
sum=0
for t in range(1,1000):
    total_amount=(1000*t)+salvage
    sum+=total_amount
    amount_bank=bank+(bank*t*rate)
    if (total_amount>amount_bank):
        print(f"Machine becomes more profitable than bank after {t} years")
        print(f"Machine total earning amount in {t} years : ₹ {total_amount} ")
        print(f"bank gave total amount in {t} years : ₹ {amount_bank}")
        break