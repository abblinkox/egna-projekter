#uppgiften är att man ska addera två av talen i listan och se om de matchar k, i så fall ska man printa true

k = 10
numbers = [4, 6, 8, 10]

summor=[numbers[0]+numbers[1], numbers[0]+numbers[2], numbers[0]+numbers[3], numbers[1]+numbers[2], numbers[1]+numbers[3],numbers[2]+numbers[3]]
    
for summa in summor:
        if k == summa:
         print("true")
