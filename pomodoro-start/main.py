import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
turns =1
work_sec = WORK_MIN*60
sh_break_sec = SHORT_BREAK_MIN*60
lo_break_sec = LONG_BREAK_MIN*60
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_mechanism():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text,text="00:00")
    activity.config(text="WORK",foreground=GREEN)
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_mechanism():
    global turns
    if turns%2 == 0:
        activity.config(text="SHORT BREAK",foreground=PINK)
        

    elif turns%2 ==1 and turns < 8:
        activity.config(text="WORK")
        new_text = '✔'*math.floor(turns/2)
        check_label.config(text=new_text)
    else:
        activity.config(text="LONG BREAK")
        check_label.config(text='✔')

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_mechanism():

    global work_sec, sh_break_sec, lo_break_sec, turns, rep
    if turns % 2 ==1 and turns < 8:
        # logic for working time
        minutes = math.floor(work_sec/60)
        seconds = work_sec % 60
        canvas.itemconfig(canvas_text,text=f'{minutes}:{seconds}')
        work_sec -= 1
        if work_sec == 0:
            turns +=1
            timer_mechanism()
            work_sec = WORK_MIN*60
            
     
    elif turns % 2 == 0:
        # logic for short break
        minutes = math.floor(sh_break_sec/60)
        seconds = sh_break_sec % 60
        canvas.itemconfig(canvas_text,text=f'{minutes}:{seconds}')
        sh_break_sec -= 1
        if sh_break_sec == 0:
            turns +=1
            timer_mechanism()
            sh_break_sec = SHORT_BREAK_MIN*60
            
    else:
        # logic for long break
        minutes = math.floor(lo_break_sec/60)
        seconds = lo_break_sec % 60
        canvas.itemconfig(canvas_text,text=f'{minutes}:{seconds}')
        lo_break_sec -= 1
        if lo_break_sec == 0:
            turns =1
            timer_mechanism()
            lo_break_sec = LONG_BREAK_MIN*60
            
    global timer
    timer = window.after(1000,countdown_mechanism)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("POMODORO")
window.config(padx=20,pady=20,background=YELLOW)

# Activity status
activity = tkinter.Label(text="WORK",foreground=GREEN,font=(FONT_NAME,30,'bold'))
activity.pack()

canvas = tkinter.Canvas(width=600,height=600,bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(300,300,image=tomato_img)
canvas_text = canvas.create_text(300,310,text="00:00",fill='white',font=(FONT_NAME,35,'bold'))
canvas.pack()


# create button 
start_button = tkinter.Button(command=countdown_mechanism,activebackground=GREEN,borderwidth=2,bg=RED, foreground="black", justify='center', text='START', font=('Arial', 20, 'bold'))
start_button.place(x=150,y=500)

# reset button
reset_button = tkinter.Button(command=reset_mechanism,activebackground=GREEN,borderwidth=2,bg=RED, foreground="black", justify='center', text='RESET', font=('Arial', 20, 'bold'))
reset_button.place(x=350,y=500)

# check marks
check_label = tkinter.Label(text='✔',fg=GREEN,bg=YELLOW)
check_label.place(x=300,y=580)

window.mainloop()