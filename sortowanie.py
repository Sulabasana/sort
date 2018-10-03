# import csv
# import operator
#
#
# sample = open('cities2.csv', 'r')
# csv1 = csv.reader(sample, delimiter=";")
#
# sort = sorted(csv1,key=operator.itemgetter(0))
#
# secondFile = open('sorted.csv', 'w')
# for linia in sort:
#      secondFile.write(str(linia) + '\n')
#
#
# secondFile.close()
# sample.close()


# With open
# import csv
# import operator
#
#
# with open('cities2.csv', 'r') as sample:
#     csv1 = csv.reader(sample, delimiter=";")
#     sort = sorted(csv1,key=operator.itemgetter(1))
#
#
# with open('sorted.csv', 'w') as secondFile:
#     for linia in sort:
#         print(linia)
#         #numberek = int(linia)
#         secondFile.write(str(linia) + '\n')

import csv
import operator
with open('cities3.csv', 'r') as sample:
    csv1 = csv.reader(sample, delimiter=";")
    sort = sorted(csv1,key=operator.itemgetter(0))
    numbers = [ int(x) for x in sort ]
with open('sorted.csv', 'w') as secondFile:
     for linia in numbers:
         print(linia)
         #numberek = int(linia)
         secondFile.write(str(linia) + '\n')