from flat_info import Bill, Flatmate
from pdf_report import PdfReport

amount = float(input("Enter the bill amount : "))
period = input("Enter name of the Month of bill to be prepared : ")

name1= input("Enter the name of 1st flatmate: ")
name2= input("Enter the name of 2nd flatmate: ")

days_in_house1 = int(input("How many days "+name1+" has stayed in the house ? :  "))
days_in_house2 = int(input("How many days "+name2+" has stayed in the house ? :  "))



the_bill = Bill(amount, period)

mate1 = Flatmate(name1, days_in_house1)
mate2 = Flatmate(name2, days_in_house2)

print(mate1.pays(the_bill, mate2))
print(mate2.pays(the_bill, mate1))

pdf_report = PdfReport(f"{period}.pdf")
pdf_report.generate(mate1 , mate2, the_bill)
