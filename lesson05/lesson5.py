# Lesson 5
print("how much money did you start with")
total = float(input())
print("what cookies did you sell")
cookies = list(input().lower())
totSold = len(cookies)
bcook = cookies.count("b")
scook = cookies.count("c")
bprofit = float((2 * bcook) - (0.75 * bcook))
sprofit = float((1.25 * scook) - (0.5 * scook))
tprofit = bprofit + sprofit
total += tprofit
print(f"You sold {totSold} cookies \nmade ${tprofit} profit \nand now have ${total} total")