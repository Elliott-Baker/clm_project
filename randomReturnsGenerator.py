import random
import csv

with open('randomReturns.csv', 'w', newline='') as csvfile:
    fieldnames = ['Percent Return']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(500):
        rando = random.uniform(-0.06, 0.06)
        writer.writerow({'Percent Return': rando})
        
print("Done! Check randomReturns.csv for your random returns!")