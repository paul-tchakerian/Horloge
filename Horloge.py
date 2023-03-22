from tkinter import *
from tkinter.ttk import *
import datetime
import platform
try:
        import winsound
        type='windows'
except:
        import os
        type='other'
window = Tk()
window.title("Clock")
window.geometry('500x250')
stopwatch_counter_num = 66600
stopwatch_running = False
timer_counter_num = 66600
timer_running = False

# je créer une fonction qui va controler l'heure et la date et les afficher dans les labels
def clock():
        date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
        date,time1 = date_time.split()
        time2,time3 = time1.split('/')
        hour,minutes,seconds =  time2.split(':')
        if int(hour) > 11 and int(hour) < 24:
                time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
        else:
                time = time2 + ' ' + time3
        time_label.config(text = time)
        date_label.config(text= date)
        time_label.after(1000, clock)

# je créer une fonction qui est appelé par le bouton "set alarm" qui va récupérer l'heure entré dans l'entry et la comparer à l'heure actuelle
def alarm():
        main_time = datetime.datetime.now().strftime("%H:%M %p")
        alarm_time = get_alarm_time_entry.get()
        alarm_time1,alarm_time2 = alarm_time.split(' ')
        alarm_hour, alarm_minutes = alarm_time1.split(':')
        main_time1,main_time2 = main_time.split(' ')
        main_hour1, main_minutes = main_time1.split(':')
        if main_time2 == 'PM':
                main_hour = str(int(main_hour1) - 12)
        else:
                main_hour = main_hour1
        if int(alarm_hour) == int(main_hour) and int(alarm_minutes) == int(main_minutes) and main_time2 == alarm_time2:
                for i in range(3):
                        alarm_status_label.config(text='Time Is Up')
                        if platform.system() == 'Windows':
                                winsound.Beep(5000,1000)
                        elif platform.system() == 'Darwin':
                                os.system('say Time is Up')
                        elif platform.system() == 'Linux':
                                os.system('beep -f 5000')
                get_alarm_time_entry.config(state='enabled')
                set_alarm_button.config(state='enabled')
                get_alarm_time_entry.delete(0,END)
                alarm_status_label.config(text = '')
        else:
                alarm_status_label.config(text='Alarm Has Started')
                get_alarm_time_entry.config(state='disabled')
                set_alarm_button.config(state='disabled')
        alarm_status_label.after(1000, alarm)


def change_time_format(mode="24"):
    heures = heures
    minutes = minutes
    secondes = secondes
    if mode == "24":
        hour_str = "{:02d}:{:02d}:{:02d}".format(heures, minutes, secondes)
    elif mode == "12":
            if heures > 12:
                hour_str = "{:02d}:{:02d}:{:02d} PM".format(heures - 12, minutes, secondes)
            else:
                hour_str = "{:02d}:{:02d}:{:02d} AM".format(heures, minutes, secondes)
            if heures == 0:
                hour_str = "{:02d}:{:02d}:{:02d} AM".format(12, minutes, secondes)
    else:
        raise ValueError("Mode d'affichage non-valide. Veuillez choisir entre 12 et 24.")

    return hour_str

stopwatch_counter_num = 66600
stopwatch_running = False

def stopwatch_counter(label):
        def count():
                if stopwatch_running:
                        global stopwatch_counter_num
                        if stopwatch_counter_num==66600:
                                display="Starting..."
                        else:
                                tt = datetime.datetime.fromtimestamp(stopwatch_counter_num) 
                                string = tt.strftime("%H:%M:%S") 
                                display=string 
                        label.config(text=display)
                        label.after(1000, count)
                        stopwatch_counter_num += 1
        count()
def stopwatch(work):
        if work == 'start':
                global stopwatch_running
                stopwatch_running=True
                stopwatch_start.config(state='disabled')
                stopwatch_stop.config(state='enabled')
                stopwatch_reset.config(state='enabled')
                stopwatch_counter(stopwatch_label)
        elif work == 'stop':
                stopwatch_running=False
                stopwatch_start.config(state='enabled')
                stopwatch_stop.config(state='disabled')
                stopwatch_reset.config(state='enabled')
        elif work == 'reset':
                global stopwatch_counter_num
                stopwatch_running=False
                stopwatch_counter_num=66600
                stopwatch_label.config(text='Stopwatch')
                stopwatch_start.config(state='enabled')
                stopwatch_stop.config(state='disabled')
                stopwatch_reset.config(state='disabled')


tabs_control = Notebook(window)
clock_tab = Frame(tabs_control)
alarm_tab = Frame(tabs_control)
stopwatch_tab = Frame(tabs_control)
timer_tab = Frame(tabs_control)
tabs_control.add(clock_tab, text="Clock")
tabs_control.add(alarm_tab, text="Alarm")
tabs_control.add(stopwatch_tab, text='Stopwatch')
tabs_control.add(timer_tab, text='Timer')
tabs_control.pack(expand = 1, fill ="both")
time_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
time_label.pack(anchor='center')
date_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
date_label.pack(anchor='s')
get_alarm_time_entry = Entry(alarm_tab, font = 'calibri 15 bold')
get_alarm_time_entry.pack(anchor='center')
alarm_instructions_label = Label(alarm_tab, font = 'calibri 10 bold', text = "Enter Alarm Time. Eg -> 01:30 PM, 01 -> Hour, 30 -> Minutes")
alarm_instructions_label.pack(anchor='s')
set_alarm_button = Button(alarm_tab, text = "Set Alarm", command=alarm)
set_alarm_button.pack(anchor='s')
alarm_status_label = Label(alarm_tab, font = 'calibri 15 bold')
alarm_status_label.pack(anchor='s')
stopwatch_label = Label(stopwatch_tab, font='calibri 40 bold', text='Stopwatch')
stopwatch_label.pack(anchor='center')
stopwatch_start = Button(stopwatch_tab, text='Start', command=lambda:stopwatch('start'))
stopwatch_start.pack(anchor='center')
stopwatch_stop = Button(stopwatch_tab, text='Stop', state='disabled',command=lambda:stopwatch('stop'))
stopwatch_stop.pack(anchor='center')
stopwatch_reset = Button(stopwatch_tab, text='Reset', state='disabled', command=lambda:stopwatch('reset'))
stopwatch_reset.pack(anchor='center')
timer_get_entry = Entry(timer_tab, font='calibiri 15 bold')
timer_get_entry.pack(anchor='center')
timer_instructions_label = Label(timer_tab, font = 'calibri 10 bold', text = "Enter Timer Time. Eg -> 01:30:30, 01 -> Hour, 30 -> Minutes, 30 -> Seconds")
timer_instructions_label.pack(anchor='s')
timer_label = Label(timer_tab, font='calibri 40 bold', text='Timer')
timer_label.pack(anchor='center')
clock()
window.mainloop()