from reportlab.lib.colors import blue
from reportlab.lib.colors import green
from reportlab.lib.colors import red
from reportlab.lib.colors import orange
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("output.pdf", pagesize = LETTER)

print(" type something to be written :")
myText = input()

print(" enter the font size : ")
size = input()

#seting font to Times New Roman with 12-point size
canvas.setFont("Times-Roman", int(size))

print(" select the color :")
print(" 1. blue  2. green  3. red  4. orange")
number = input()

if number == "1":
    canvas.setFillColor(blue)
elif number == "2":
    canvas.setFillColor(green)
elif number == "3":
    canvas.setFillColor(red)
elif number == "4":
    canvas.setFillColor(orange)

#draw blue text one inch from the left and ten inches from the bottom

canvas.drawString(1* inch, 10* inch, myText)

#saving the PDF file
canvas.save()
