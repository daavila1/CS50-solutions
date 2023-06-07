from fpdf import FPDF

class PDF(FPDF):
    def page_title(self):
        self.set_font("helvetica", "B", 40)
        self.cell(0, 80, "CS50 Shirtificate", border = 0, align = "C")
        self.ln()


    def page_image(self):
        self.image("shirtificate.png", w = 190, x = (210 - 190)/2, y = 70) #(page.size[0] - image.width)/2


    def page_body(self, name):
        self.set_text_color(250, 250, 250)
        self.set_font("helvetica", "", 25)
        self.cell(0, 95, f"{name} took SC50", border = 0, align = "C")

    def get_dimension(self):
        self.image()

    def print_shirt(self, name):
        self.add_page(orientation = "P", format = "A4")
        self.set_margin(0)
        self.page_title()
        self.page_image()
        self.page_body(name)

pdf = PDF(unit = "mm")
pdf.print_shirt(input("Name: "))
pdf.output("shirtificate.pdf")

