# BMI Calculator
# by Ryan
# Python 3.9 using Geany Editor
# Windows 10
# BMI = weight (kilograms) / height (meters) ** 2

import tkinter
# toolkit interface
root = tkinter.Tk()
# root.geometry("300x150") // OPTIONAL
root.title("BMI Calculator")

# Create Function(s)
def calculate_bmi():
	weight = float(entry_weight.get())
	height = float(entry_height.get())
	bmi = round(weight / (height ** 2), 2)
	label_result['text'] = f"BMI: {bmi}"

# Create GUI (Graphical User Interface)
label_weight = tkinter.Label(root, text="WEIGHT (KG): ")
label_weight.grid(column=0, row=0)

entry_weight = tkinter.Entry(root)
entry_weight.grid(column=1, row=0)

label_height = tkinter.Label(root, text="HEIGHT (M): ")
label_height.grid(column=0, row=1)

entry_height = tkinter.Entry(root)
entry_height.grid(column=1, row=1)

button_calculate = tkinter.Button(root, text="Calculate", command=calculate_bmi)
button_calculate.grid(column=0, row=2)


label_result = tkinter.Label(root, text="BMI: ")
label_result.grid(column=1, row=2)

root.mainloop()
