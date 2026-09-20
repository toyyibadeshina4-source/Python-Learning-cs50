import csv
with open("security_log.csv") as file:
 reader = csv.DictReader(file)
 for row in reader:
  text = row["Notes"]
 name = row["Employee"]
 if "credit card" in name:
  print("⚠ALERT!Data Leak Found")
  print(name + " accidentally typed a credit card number")
 else:
  print("Your credit card is save. Beware of Hackers")