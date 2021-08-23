from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("font-colors.pdf", pagesize = LETTER)

#seting font to Times New Roman with 12-point size
canvas.setFont("Times-Roman", 12)

#draw blue text one inch from the left and ten inches from the bottom
canvas.setFillColor(blue)
canvas.drawString(1* inch, 10* inch, "Hello World!")

#saving the PDF file
canvas.save()