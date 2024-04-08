from datetime import datetime
from fpdf import FPDF
import sys

# Used to get current day for each generated Cover Letter
def getDate():
    date = datetime.today()
    # Desired format Month Day, Year
    return date.strftime("%B %#d, %Y")

class PDF(FPDF):
    # For writing each line with the proper spacing I want
    def newLine(self, text):
        self.multi_cell(0, 5, text, 0, 1)
        self.ln(5)

    # Handles signoff which has different spacing from newLine()
    def signoff(self, text):
        self.multi_cell(0, 5, text, 0, 1)

    # Handles header name
    def headerName(self, text):
        self.set_font('Times', "B", 28)
        self.cell(0, 10, text, 0, 1, 'R')

    # Handles header text
    def headerText(self, text):
        self.set_font('Times', "", 12)
        self.cell(0, 6, text, 0, 1, 'R')
    
    # Handles links included in header
    def headerLink(self, text, link):
        self.set_font('Times', "U", 12)
        # Sets link to be blue
        self.set_text_color(0, 0, 255)
        self.cell(0, 6, text, 0, 1, 'R', False, link)
        # Resets color of text going forward to be black
        self.set_text_color(0, 0, 0)

def main(position):

    # Instantiation of inherited class
    pdf = PDF('P', 'mm', 'A4')

    # Set margins 25.4 mm == 1 inch
    pdf.set_margins(24.4, 25.4, 24.4)
    pdf.add_page()

    # Contact Info
    pdf.headerName("John Stroud")
    pdf.headerLink("testemail@gmail.com", "mailto:testemail@gmail.com")
    pdf.headerText("(###) ###-####")

    # Line separates header from body
    pdf.line(25.4, 50, 184.6, 50)
    pdf.ln(5)


    # Main Body
    pdf.newLine(getDate())
    pdf.newLine("Dear Hiring Manager")
    pdf.newLine("I am writing to inquire about the opening for the " + position + "position.")
    pdf.newLine("I offer a bachelors in computer science and a security based web development internship which makes me a strong candidate for this opening. "
                "The employment section of my resume highlights my career profile and demonstrates the same skills being asked of this position.")
    pdf.newLine("I would welcome the opportunity to speak with you if you feel I would be a strong candidate for this or any position in your organization.")
    pdf.newLine("Thank you for your consideration.")

    # Signoff needs different spacing than body
    pdf.signoff("Sincerely,")
    pdf.signoff("John Stroud")

    # Sends generated Cover Letter
    filename = r"Cover Letter.pdf"
    pdf.output(filename, 'F')

if __name__ == "__main__":

    # Checks for correct arguments
    n = len(sys.argv)
    if n == 1:
        print("Error: Forgot to Enter job Title")
        exit()

    # Gets the position from command line arguments
    position = ""
    for x in range(n):
        if x != 0:
            position += str(sys.argv[x] + " ")
    
    # Feeds main the position of the job
    main(position)
