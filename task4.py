motorbike_cost = 2000
loses = 10/100
while motorbike_cost >= 1000:
    cost = motorbike_cost * loses
    motorbike_cost -= cost
    print(round(motorbike_cost))