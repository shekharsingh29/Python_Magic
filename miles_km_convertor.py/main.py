import tkinter

from numpy import NaN

window = tkinter.Tk()
window.minsize(600,600)
window.title("Mile to KM convertor")
window.config(background="blue",padx=50,pady=50)

# Miles Input 
miles_text = tkinter.Entry(insertbackground="cyan",insertborderwidth=2,width=20)
miles_text.focus()
miles_text.place(x=100,y=110)


# Miles label
miles_label = tkinter.Label(borderwidth=2,highlightbackground="green",foreground="red",text="MILES", font=('Arial', 24, 'bold'))
miles_label.place(x=300, y=100)


# Labels for KM field
km = 0
km_label = tkinter.Label(borderwidth=2,highlightbackground='green',foreground="red",text=f"Is equal to :      {km}       KM", font=("Arial",24, "bold"))
km_label.place(x=50, y=180)




# Button logic
def calculate_km():
    if (miles_text.get()!=None or miles_text.get()!='') and int(miles_text.get()) != NaN:
        km = 1.60934 * int(miles_text.get())
        km_label['text']=f"Is equal to :      {km}       KM"


calculate_btn = tkinter.Button(command=calculate_km,activebackground="green",borderwidth=2,bg="yellow", foreground="black",padx=20, pady=20, width=20, justify='center', text='CALCULATE', font=('Arial', 24, 'bold'))
calculate_btn.place(x=25, y=250)



window.mainloop()