from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime
from typing import Counter
from classes import text_Gui
from classes import db_backEnd


# Initialize a Tk instance and set frames
root = Tk()
frame_1 = Frame(root)
frame_1.grid(row=1, column=1)
frame_2 = Frame(root)
frame_2.grid(row=2, column=1)
frame_3 = Frame(root)
frame_3.grid(row=2, column=2)

#Frame 1 widgets
lbl_greet = Label(frame_1, text="Hello and welcome Luis!!  ", relief="raised")
lbl_greet.grid(row=1, column=1)

date_now = datetime.date.today()
date_now = str(date_now)
lbl_date_lbl = Label(frame_1, text="Todays date:   ", relief="raised")
lbl_date_lbl.grid(row=1, column=2)
lbl_date = Label(frame_1, text=date_now, )
lbl_date.grid(row=1, column=3)

#frame_2 widgets
# The wellness checklist 
lbl_well = Label(frame_1, text="Your daily wellness check: ")
lbl_well.grid(row=2, column=1)

lbl_sleep = Label(frame_2, text="Sleep by 10 pm", relief="raised")
lbl_sleep.grid(row=1, column=1)

mds_830 = StringVar()
mds_check = Checkbutton(frame_2, text="Take meds by 8:30 P.M.", command= lambda :mds_830.get(), variable=mds_830, onvalue="Complete", offvalue="Not complete")
mds_check.grid(row=2, column=1)

meltn_use = StringVar()
mltn_check = Checkbutton(frame_2, text="Did you use melatonin?", command=lambda :meltn_use.get(), variable=meltn_use, onvalue="Complete", offvalue="Not complete")
mltn_check.grid(row=3, column=1)

sleep_10pm = StringVar()
sleep_check = Checkbutton(frame_2, text="Are you in bed by 10pm?", command=lambda :sleep_10pm.get(), variable=sleep_10pm, onvalue="Complete", offvalue="Not complete")
sleep_check.grid(row=4, column=1)

lbl_blnk1 = Label(frame_2, text="       ")
lbl_blnk1.grid(row=1, column=2)

lbl_workout = Label(frame_2, text="Work out", relief="raised")
lbl_workout.grid(row=1, column=3)

wrkout_today = StringVar()
wrkout_check = Checkbutton(frame_2, text="Did you work out?", command=lambda :wrkout_today.get(), variable=wrkout_today, onvalue="Complete", offvalue="Not complete")
wrkout_check.grid(row=2, column=3)

walk_wrkout = StringVar()
walk_check = Checkbutton(frame_2, text="Did you walk +10\n minutes? ", command=lambda :walk_wrkout.get(), variable=walk_wrkout, onvalue="Complete", offvalue="Not complete")
walk_check.grid(row=3, column=3)

tai_stretch = StringVar()
tai_check = Checkbutton(frame_2, text="Did you do tai-chi?", command=lambda :tai_stretch.get(), variable=tai_stretch, onvalue="Complete", offvalue="Not complete")
tai_check.grid(row=4, column=3)
lbl_blnk2 = Label(frame_2, text="       ")
lbl_blnk2.grid(row=1, column=4)

lbl_chores = Label(frame_2, text="chores", relief="raised")
lbl_chores.grid(row=1, column=5)

corn_cut = StringVar()
corn_check = Checkbutton(frame_2, text="Did you cut the corn?", command=lambda : corn_cut.get(), variable=corn_cut, onvalue="Complete", offvalue="Not complete")
corn_check.grid(row=2, column=5)

takeout_trsh = StringVar()
trash_Check = Checkbutton(frame_2, text="Did you take out trash?", command= lambda : takeout_trsh.get(), variable=takeout_trsh, onvalue="Complete", offvalue="Not complete")
trash_Check.grid(row=3, column=5)

rem_chores = StringVar()
rem_chrs_check =Checkbutton(frame_2, text="Did you do all rem. chores?", command=rem_chores.get(), variable=rem_chores, onvalue="Complete", offvalue="Not Complete")
rem_chrs_check.grid(row=4, column=5)


#frame_3 widgets 
lbl_menu = Label(frame_3, text="==MENU==", relief="raised")
lbl_menu.pack()

def launch_alerts():
    alrt_sys = text_Gui()
    alrt_sys.gui_Txt_alrt()

launch_butt = Button(frame_3, text="=Alerts=", relief="raised", command=launch_alerts)
launch_butt.pack()

db_back = db_backEnd("a", "b", "j", "d", "e", "f", "g", "h", "i", "z", "c")
db_back.initialize_db("z")

def add_vals():
    db_back.add_vals(mds_830.get(), meltn_use.get(), sleep_10pm.get(), wrkout_today.get(), walk_wrkout.get(), tai_stretch.get(), corn_cut.get(), takeout_trsh.get(), rem_chores.get())
    messagebox.showinfo(message="Data submitted!!!")

submit_bttn = Button(frame_3, text="=Submit=", command=add_vals, relief="raised")
submit_bttn.pack()
root.mainloop()