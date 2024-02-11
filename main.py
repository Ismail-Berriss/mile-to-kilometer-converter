from tkinter import *


def convert():
    miles = float(mile_entry.get())
    km = round(miles * 1.6)
    result.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=30, pady=30)

mile_entry = Entry(width=10)
mile_entry.insert(END, string="0")
mile_entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

window.mainloop()
