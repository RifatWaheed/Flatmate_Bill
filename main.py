from fpdf import FPDF

class Bill:
    def __init__(self,amount,period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self,name,days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self,bill,flatmate2):
        weight= self.days_in_house/(self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount*weight
        return to_pay


class PdfReport:
    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1,flatmate2,bill):

        # Insert title
        pdf=FPDF(orientation='P',unit='pt',format='A4')
        pdf.add_page()
        pdf.set_font(family='Times', size=24,style='B')
        pdf.cell(w=0, h=80 , txt="Flatmates Bills",border=1,align='C',ln=2)
        pdf.cell(w=0, h=80, txt="", align='C', ln=2)

        # Insert period label and its value
        pdf.cell(w=100, h=100, txt="Period:", border=1, align='C')
        pdf.cell(w=150, h=100, txt=bill.period, border=1, align='C',ln=1)

        # Name and due amount of the first flatmate
        pdf.cell(w=100, h=100, txt="1. " + flatmate1.name+' ', border=1)
        pdf.cell(w=150, h=100, txt= str(flatmate1.pays(bill,flatmate2)), border=1, ln=1)

        pdf.output(self.filename)


the_bill = Bill(amount=120 , period= "April 2022")

john = Flatmate(name='John',days_in_house=20)
marry = Flatmate(name='Marry',days_in_house=25)

print(john.pays(bill=the_bill,flatmate2=marry))
print(marry.pays(bill=the_bill,flatmate2=john))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john,flatmate2=marry,bill=the_bill)