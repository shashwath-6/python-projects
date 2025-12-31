import tkinter as tk
window=tk.Tk()
window.title("GUI")
window.geometry("600x600+10+10")
title=tk.Label(window,text="Registeration Form",font=("Arial",20,"bold"))
title.grid(row=0, column=0, columnspan=1,)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)

#name
name_label=tk.Label(window,text="Name",font=("Arial",15,"bold"))
name_label.grid(row=1,column=0,sticky="W")
name=tk.Entry(window,width=30)
name.grid(row=1,column=0,padx=100,pady=0,sticky="W")

#date of birth
dob_label=tk.LabelFrame(window,text="Date of Birth",font=("Arial",15,"bold"))
dob_label.grid(row=2,column=0,sticky="E")

date=tk.Spinbox(dob_label,width=15,from_=0,to=31)
month=tk.Spinbox(dob_label,width=15,from_=0,to=12)
year=tk.Spinbox(dob_label,width=15,from_=1947,to=2023)
date.grid(row=0,column=0,sticky="W")
tk.Label(dob_label,text=":").grid(row=0,column=1,sticky="W")
month.grid(row=0,column=2,sticky="W")
tk.Label(dob_label,text=":").grid(row=0,column=3,sticky="W")
year.grid(row=0,column=4,sticky="W")

#gender

option_frame=tk.LabelFrame(window,text="Gender")
option_frame.grid(row=1,column=3,sticky="W")
gender = tk.IntVar()
gender.set(3)  # Default value (none selected)

# Create Radiobuttons for gender
gender_male = tk.Radiobutton(option_frame, text="Male", value=1, variable=gender)
gender_female = tk.Radiobutton(option_frame, text="Female", value=2, variable=gender)
gender_other = tk.Radiobutton(option_frame, text="Other", value=3, variable=gender)

# Place the Radiobuttons in the grid
gender_male.grid(row=0, column=0, sticky="W", padx=10, pady=5)
gender_female.grid(row=1, column=0, sticky="W", padx=10, pady=5)
gender_other.grid(row=2, column=0, sticky="W", padx=10, pady=5)
print(gender.get())
print(name.get())
window.mainloop()
