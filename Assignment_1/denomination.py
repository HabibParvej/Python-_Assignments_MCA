

amt=int(input("Enter Amount: "))
hundreds=amt//100
fifties=(amt%100)//50
tens=(amt%100)%50//10
print("No. of 100s: ",hundreds)
print("No. of 50s: ",fifties)
print("No. of 10s: ",tens)