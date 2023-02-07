from fpdf import FPDF


class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return round(to_pay, 2)


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(flatmate1.pays(bill, flatmate2))
        flatmate2_pay = str(flatmate2.pays(bill, flatmate2))

        # Insert title
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add icon at top

        pdf.image("download.png",w=100,h=100,x=80,y=20)

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bills", border=1, align='C', ln=2)
        pdf.cell(w=0, h=80, txt="", align='C', ln=2)

        # Insert period label and its value
        pdf.cell(w=100, h=60, txt="Period:", border=1, align='C')
        pdf.cell(w=150, h=60, txt=bill.period, border=1, align='C', ln=1)

        # Name and due amount of the first flatmate1
        pdf.cell(w=100, h=60, txt=flatmate1.name + ' ', align='C', border=1)
        pdf.cell(w=150, h=60, txt=flatmate1_pay, align='C', border=1, ln=1)

        # Name and due amount of the first flatmate2
        pdf.cell(w=100, h=60, txt=flatmate2.name + ' ', align='C', border=1)
        pdf.cell(w=150, h=60, txt=flatmate2_pay, align='C', border=1, ln=1)

        pdf.output(self.filename)


the_bill = Bill(amount=120, period="April 2022")

john = Flatmate(name='John', days_in_house=20)
marry = Flatmate(name='Marry', days_in_house=25)

print(john.pays(bill=the_bill, flatmate2=marry))
print(marry.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
