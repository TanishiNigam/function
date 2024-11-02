def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def division(P,Q):
    return P/Q
print("1. add 2. subtract 3. multiply 4. divide")
variable= input("input any number from above")
P=int(input("Enter your first number"))
Q=int(input("Enter your second number"))
if variable=="1":
    print(P,"+",Q,"=",add(P,Q))
elif variable=="2":
    print(P,"-",Q,"=",subtract(P,Q))
elif variable=="3":
    print(P,"x",Q,"=",multiply(P,Q))
elif variable=="4":
    print(P,"/",Q,"=",division(P,Q))