import webbrowser

from fpdf import FPDF


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))


        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add icon of house
        pdf.image("download.png",w=100,h=100,x=80,y=20)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bills", border=1, align='C', ln=2)
        pdf.cell(w=0, h=80, txt="", align='C', ln=2)

        # Insert period label and its value
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=60, txt="Period:", border=0, align='C')
        pdf.cell(w=150, h=60, txt=bill.period, border=0, align='C', ln=1)

        # Name and due amount of the first flatmate1
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=60, txt=flatmate1.name + ' ', align='C', border=0)
        pdf.cell(w=150, h=60, txt=flatmate1_pay, align='C', border=0, ln=1)

        # Name and due amount of the first flatmate2
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=60, txt=flatmate2.name + ' ', align='C', border=0)
        pdf.cell(w=150, h=60, txt=flatmate2_pay, align='C', border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)
