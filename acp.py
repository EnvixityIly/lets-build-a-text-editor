from tkinter import *

window = Tk()
window.title("Simple Interest Calcularor")
window.geometry("400x300")

def calculate_interest():

    principal = float(entry_principal.get())
    years = float(entry_years.get())
    rate = float(entry_rate.get())
    interest = (principal * rate * years)/100
    result_label.config(text=f"interest: {interest:.2f}")

label_principal = Label(window,text="Principl amount:")
label_principal.pack(pady=5)

entry_principal = Entry(window)
entry_principal.pack(pady = 5)

label_years = Label(window,text="Number of years:")
label_years.pack(pady=5)

entry_years = Entry(window)
entry_years.pack(pady=5)

rate_label = Label(window,text = "interest rate: ")
rate_label.pack(pady=5)

entry_rate = Entry(window)
entry_rate.pack(pady=5)

calculate_button = Button(window, text = "Calculate", command = calculate_interest)
calculate_button.pack(pady=10)

result_label = Label(window,text = "", font = ("Arial",12))
result_label.pack(pady=10)

window.mainloop()

