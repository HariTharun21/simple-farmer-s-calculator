import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("simple farmers calculator")
root.geometry("600x400")

# Center all widgets in the middle
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(5, weight=1)

# Title Label
title_label = tk.Label(root, text="Simple Farmer's Calculator", font=("Arial", 16, "bold"), fg="green")
title_label.grid(row=0, column=1, columnspan=4, pady=10)

diff = 0
l1=tk.Label(root,text="price(rs):",fg="black")
l1.grid(row=1,column=1)
e1=tk.Entry(root)
e1.grid(row=1,column=2)
l2=tk.Label(root,text="per",fg="black")
l2.grid(row=1,column=3)
# combobox weight parameter
c1=ttk.Combobox(root,width=23)
c1["values"]=("kg","quinta","ton","45kg(bag)")
c1.set("Select Weight Parameter")
c1.grid(row=1,column=4)

#row 2
l3=tk.Label(root,text="Quantity produced",fg="black")
e2=tk.Entry(root)
l4=tk.Label(root,text="in",fg="black")
c2=ttk.Combobox(root,width=23)
c2['values']=("kg","quinta","ton","45kg(bag)")
c2.set("Select Weight Parameter")

l5=tk.Label(root,text="",fg="black")
l3.grid(row=2,column=1)
e2.grid(row=2,column=2)
l4.grid(row=2,column=3)
c2.grid(row=2,column=4)



#row 3
l6=tk.Label(root,text="Farming land",fg="black")
e3=tk.Entry(root)
group=tk.StringVar(value="none")
r1=tk.Radiobutton(root,text="acre",value="acre",variable=group)
r2=tk.Radiobutton(root,text="hectare",value="hectare",variable=group)
l6.grid(row=3,column=1)
e3.grid(row=3,column=2)
r1.grid(row=3,column=3)
r2.grid(row=3,column=4)

#row 4
l7=tk.Label(root,text="investment",fg="black")
e4=tk.Entry(root)
l7.grid(row=4,column=1)
e4.grid(row=4,column=2)





def check():
    global diff
    try:
        com1 = c1.get()
        com2 = c2.get()
        entry1 = float(e1.get())
        entry2 = float(e2.get())
        entry4 = float(e4.get())


        # Validate inputs
        if not e1.get() or not e2.get() or not e4.get():
            c = "Entry fields should not be empty."
        elif entry1 <= 0 or entry2 <= 0 or entry4 <= 0:
            c = "Please enter a number greater than zero."
        else:
            if com1 == com2:
                a = entry1 * entry2
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "kg" and com2 == "quinta":
                a = entry1 * (100 * entry2)
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "kg" and com2 == "ton":
                a = entry1 * 1000 * entry2
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "kg" and com2 == "45kg(bag)":
                a = entry1 * (45 * entry2)
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "quinta" and com2 == "kg":
                b = entry1 / 100
                a = b * entry2
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "quinta" and com2 == "ton":
                b = entry1 * 10
                a = b * entry2
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "quinta" and com2 == "45kg(bag)":
                b = entry1 * 100
                a = b * (45 * entry2)
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "ton" and com2 == "kg":
                b = entry1 / 1000
                a = b * entry2
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "ton" and com2 == "quinta":
                b = entry1 / 10
                a = b * entry2
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "ton" and com2 == "45kg(bag)":
                b = entry1 / 1000
                a = b * (45 * entry2)
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "45kg(bag)" and com2 == "kg":
                b = entry1 / 45
                a = b * entry2
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "45kg(bag)" and com2 == "quinta":
                b = entry1 / 45
                a = b * (100 * entry2)
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            elif com1 == "45kg(bag)" and com2 == "ton":
                b = entry1 / 45
                a = b * (1000 * entry2)
                if a >= entry4:
                    diff = a - entry4
                    c = f"Profit: {diff}"
                else:
                    diff = entry4 - a
                    c = f"Loss: {diff}"

            else:
                c = "Invalid unit conversion."
    except ValueError:
        c = "Please enter valid numeric values."

    r_label.config(text=c)

#row 5 and 6
b1 = tk.Button(root, text="check profit or loss", bg="green", fg="black", command=check)
r_label = tk.Label(root, text="")
b1.grid(row=5, column=2)
r_label.grid(row=6, column=2)


def areawise():
    try:
        a=group.get()
        com2 = c2.get()
        entry2=float(e2.get())
        entry3=float(e3.get())
        if entry3<=0:
            y="farming land must be greater than zero"
        elif not entry2 or not entry3 :
            y="please enter a number in farming land"
        elif not com2:
            y="please select the weight parameter"
        else:
            if a=="acre":
                x=entry2/entry3
                y=f"{x:.2f}{com2} produced per acre"

            elif a=="hectare":
                x=entry2/entry3
                y=f"{x:.2f}{com2} produced per hectare"
            else:
                y="please select the area"

    except ValueError:
        y="please enter valid numeric values"

    r2_label.config(text=y)
#row 7 and 8
b2=tk.Button(root,text="Quantity produced in area wise",command=areawise)
r2_label=tk.Label(root,text="")
b2.grid(row=5,column=4)
r2_label.grid(row=6,column=4)

def investment():
    try:
        a = group.get()
        entry3 = float(e3.get())
        entry4 = float(e4.get())

        if not entry3 or not entry4:
            t = "Please enter numeric values."
        else:
            if a == "acre":
                b = entry4 / entry3
                t = f"{b:.2f} Rs invested per acre."
            elif a == "hectare":
                b = entry4 / entry3
                t = f"{b:.2f} Rs invested per hectare."
            else:
                t = "Please select a valid area type."
    except ValueError:
        t = "Please enter a valid number."

    r3_label.config(text=t)

#row 9
b3=(tk.Button(root,text="investment per acre",bg="blue",fg="black",command=investment))
r3_label=tk.Label(root,text="")
b3.grid(row=7,column=2)
r3_label.grid(row=8,column=2)

def profit():
    global diff
    try:
        t=""
        a=group.get()
        entry3=float(e3.get())
        d=r_label.cget("text")
        if not entry3:
            t = "Please enter numeric values."
        elif not d:
            t="please press the check profit or loss button"
        else:
            if "Profit:" in d:
                if a == "acre":
                   b = diff/entry3
                   t = f"{b:.2f}Rs profit per acre."
                elif a == "hectare":
                    b = diff/ entry3
                    t = f"{b:.2f}Rs profit per hectare."
                else:
                    t = "Please select a valid area type."
            elif "Loss:" in d:
                if a == "acre":
                   b = diff/entry3
                   t = f"{b:.2f}Rs loss per acre."
                elif a == "hectare":
                    b = diff/ entry3
                    t = f"{b:.2f}Rs loss per hectare."

                else:
                    t = "Please select a valid area type."
    except ValueError:
        t = "Please enter a valid number."
    r4_label.config(text=t)
b4=tk.Button(root,text="profit/loss per acre",bg="yellow",fg="black",command=profit)
r4_label=tk.Label(root,text="")
b4.grid(row=7,column=4)
r4_label.grid(row=8,column=4)

root.mainloop()
