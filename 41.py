import csv
with open("csv4.csv", newline='') as csvfile:
 d = csv.DictReader(csvfile)
 print("ROLL NO STUDENT NAME COURSE")
 print("--------------------")
 for i in d:
  print(i['ROLLNO'], i['STUDENTNAME'],i['COURSE'])