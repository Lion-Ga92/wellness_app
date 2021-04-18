import os 
from twilio.rest import Client
from tkinter import *
from tkinter import ttk
import time 
import sqlite3

class Text_backend:
    
    def __init__(self, mssg_1):
        self.mssg_1 = mssg_1


    def send_text(self, mssg_1):
            self.mssg_1 = mssg_1
            # Download the helper library from https://www.twilio.com/docs/python/install
            # Your Account Sid and Auth Token from twilio.com/console   
            # and set the environment variables. See http://twil.io/secure
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body= self.mssg_1,
                                from_='+14159154317',
                                to='7078629378'
                                )

            print(message.sid)

    def send_text_greet(self):
            # Download the helper library from https://www.twilio.com/docs/python/install
            # Your Account Sid and Auth Token from twilio.com/console   
            # and set the environment variables. See http://twil.io/secure
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)

            message1 = client.messages \
                            .create(
                                body= 'Good morning: Remember to take your meds, and do your chores',
                                from_='+14159154317',
                                to='7078629378'
                                )

            print(message1.sid)

    def send_textShower(self):
            # Download the helper library from https://www.twilio.com/docs/python/install
            # Your Account Sid and Auth Token from twilio.com/console   
            # and set the environment variables. See http://twil.io/secure
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)

            message2 = client.messages \
                            .create(
                                body= 'And take a shower!',
                                from_='+14159154317',
                                to='7078629378'
                                )

            print(message2.sid)


class text_Gui:
    
    def __init__(self):
        self = self

    
    def gui_Txt_alrt(self):
        #GUI Elements of the Alert system 
        self.second = Toplevel()
        self.frame_z = Frame(self.second)
        self.frame_z.grid(row=1, column=1)
        self.frame_x = Frame(self.second)
        self.frame_x.grid(row=2, column=1)
        self.frame_y = Frame(self.second)
        self.frame_y.grid(row=3, column=1)
        self.lbl_greetZ = Label(self.frame_z, text="Welcome to the text Alert system: ", relief="raised")
        self.lbl_greetZ.grid(row=2, column=1)
        self.picker = Label(self.frame_z, text="Pick which task you wanna work on today (limit one)")
        self.picker.grid(row=3, column=1)

        msg_var = StringVar()
        self.mssg_ent = Entry(self.frame_y, textvariable=msg_var)
        self.mssg_ent.grid(row=1, column=2)

        #Due to the need to use different message, but also delete the previous message if i press another 
        # button, i went for functions and not lambdas in this program. Even though they are really similar

        def add_msg1():
            self.mssg_ent.delete(0, END)
            self.mssg_ent.insert(0, "Your chore: Do laundry")

        self.msg1_btt = Button(self.frame_x, text="Monday", command=add_msg1, relief="raised")
        self.msg1_btt.grid(row=1, column=1)

        def add_msg2():
            self.mssg_ent.delete(0, END)
            self.mssg_ent.insert(0, "Your chore: Clean living Room")

        self.msg2_btt = Button(self.frame_x, text="Tuesday", command=add_msg2, relief="raised")
        self.msg2_btt.grid(row=1, column=2)

        def add_msg3():
            self.mssg_ent.delete(0, END)
            self.mssg_ent.insert(0, "Your chore: Wash dishes")

        self.msg3_btt = Button(self.frame_x, text="Wednesday", command=add_msg3, relief="raised")
        self.msg3_btt.grid(row=1, column=3)

        def add_msg4():
            self.mssg_ent.delete(0, END)
            self.mssg_ent.insert(0, "Your chore: Clean bathroom")
            

        self.msg4_btt = Button(self.frame_x, text="Thursday", command=add_msg4, relief="raised")
        self.msg4_btt.grid(row=1, column=4)

        def add_msg5():
            self.mssg_ent.delete(0, END)
            self.mssg_ent.insert(0, "Your chore: Cook 4-All")
        
        self.msg5_btt = Button(self.frame_x, text="Friday", command=add_msg5, relief="raised")
        self.msg5_btt.grid(row=2, column=1)

        def add_msg6():
            self.mssg_ent.delete(0, END)
            self.mssg_ent.insert(0, "Your chore: Clean room")

        self.msg6_btt = Button(self.frame_x, text="Saturday", command=add_msg6, relief="raised")
        self.msg6_btt.grid(row=2, column=2)

        def add_msg7():
            self.mssg_ent.delete(0, END)
            self.mssg_ent.insert(0, "Your chore: Clean Kitchen")
            

        self.msg7_btt = Button(self.frame_x, text="Sunday", command=add_msg7, relief="raised")
        self.msg7_btt.grid(row=2, column=3)

        self.lbl_mssg = Label(self.frame_y, text="This is your message: ", relief="raised")
        self.lbl_mssg.grid(row=1, column=1)

        self.lbl_time = Label(self.frame_y, text="Delay in seconds: ", relief="raised")
        self.lbl_time.grid(row=2, column=1)
        
        self.time_ent = Entry(self.frame_y, width=20)
        self.time_ent.grid(row=2, column=2)

        # THIS WILL BE ONE CONVULUTED FUNCTION, I WILL INSTATIATE THE Text_backend and then use flow control
        # to check for which message is in mssg_ent and launch the appropriate alert

        def text_launch():
            #TO anyone reading this, i have this weird issue at least due to my lack of experience. 
            # but for somereason anytime i instantiate a class. If i have init values. It requires me to add the same number 
            # values as positional arguments. I've fallen into the bad practice of adding random one letter strings. But its wrong
            text_now = Text_backend("a")
            msssg_1 = self.mssg_ent.get()
            time_dly = self.time_ent.get()
            time_dly = int(time_dly)

            # AFAIK twilio does not permit scheduling sms texts being sent out, so i am using a hard coded way.
            # By using time.sleep() to delay the sending of the text message. Right now i am using small time frames 2-5 seconds
            # But i am hoping to put this software on an android tablet using Userland to run debian, to run the app. 
            # My hope is that with such app i can either keep this software running without crashing. 

            if msssg_1 == "Your chore: Do laundry":
                time.sleep(time_dly)
                text_now.send_text_greet()
                time.sleep(4)
                text_now.send_text(msssg_1)
                time.sleep(4)
                text_now.send_textShower()
                exit()

            elif msssg_1 == "Your chore: Clean living Room":
                time.sleep(time_dly)
                text_now.send_text_greet()
                time.sleep(time_dly)
                text_now.send_text(msssg_1)
                time.sleep(4)
                text_now.send_textShower()
                exit()

            elif msssg_1 == "Your chore: Wash dishes":
                time.sleep(time_dly)
                text_now.send_text_greet()
                time.sleep(time_dly)
                text_now.send_text(msssg_1)
                time.sleep(4)
                text_now.send_textShower()
                exit()

            elif msssg_1 == "Your chore: Clean bathroom":
                time.sleep(time_dly)
                text_now.send_text_greet()
                time.sleep(time_dly)
                text_now.send_text(msssg_1)
                time.sleep(4)
                text_now.send_textShower()
                exit()

            elif msssg_1 == "Your chore: Cook 4-All":
                time.sleep(time_dly)
                text_now.send_text_greet()
                time.sleep(time_dly)
                text_now.send_text(msssg_1)
                time.sleep(4)
                text_now.send_textShower()
                exit()

            elif msssg_1 == "Your chore: Clean room":
                time.sleep(time_dly)
                text_now.send_text_greet()
                time.sleep(time_dly)
                text_now.send_text(msssg_1)
                time.sleep(time_dly)
                text_now.send_textShower()
                exit()

            elif msssg_1 == "Your chore: Clean Kitchen":
                time.sleep(time_dly)
                text_now.send_text_greet()
                time.sleep(time_dly)
                text_now.send_text(msssg_1)
                time.sleep(time_dly)
                text_now.send_textShower()
                exit()
                
        launch_alrt_now = Button(self.frame_y, text="launch alert", command=text_launch,relief="raised")
        launch_alrt_now.grid(row=3, column=1)
        self.second.mainloop()


class db_backEnd:
    def __init__(self):
        self = self

    def initialize_db(self):
        self.j = 1

        self.conn = sqlite3.connect("well_check.db")

        self.c = self.conn.cursor()

        self.c.execute('''CREATE TABLE IF NOT EXISTS wellCheck (meds_830 TEXT, melatonin TEXT, sleep_10pm TEXT, work_Out TEXT, walk_Work TEXT, tai_chi TEXT, corn_Cut TEXT, trash TEXT, chores TEXT);''')

        self.conn.commit()

        self.j = 1    
        while self.j != 1:
            self.conn.close()

    def add_vals(self, a, b, j, d, e, f, g, h, i):
        self.c = self.conn.cursor()
        self.a = a
        self.b = b
        self.j = j
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        data_1 = (self.a, self.b, self.j, self.d, self.e, self.f, self.g, self.h, self.i)
        query = "INSERT INTO wellCheck VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
        self.c.execute(query, data_1)
        self.conn.commit()


    def db_viewer(self):
        self.conn = sqlite3.connect("well_check.db")
        my_window= Tk()
        frame_f = Frame(my_window)
        frame_f.grid(row=1, column=1)
        #frame_f labels 
        lbl_meds = Label(frame_f, text="Meds 0830      ", relief="raised")
        lbl_meds.grid(row=1, column=1)

        lbl_meltnin = Label(frame_f, text="Melatonin    ", relief="raised")
        lbl_meltnin.grid(row=1, column=2)

        lbl_sleep = Label(frame_f, text="Sleep 10pm     ", relief="raised")
        lbl_sleep.grid(row=1, column=3)

        lbl_workout = Label(frame_f, text="Workout       ", relief="raised")
        lbl_workout.grid(row=1, column=4)

        lbl_walk = Label(frame_f, text="Walk around       ", relief="raised")
        lbl_walk.grid(row=1, column=5)


        lbl_taichi = Label(frame_f, text="Tai-chi         ", relief="raised")
        lbl_taichi.grid(row=1, column=6)


        lbl_corn = Label(frame_f, text="Cut corn           ", relief="raised")
        lbl_corn.grid(row=1, column=7)

        lbl_trash = Label(frame_f, text="Trash              ", relief="raised")
        lbl_trash.grid(row=1, column=8)

        lbl_chores = Label(frame_f, text="Chore             ", relief="raised")
        lbl_chores.grid(row=1, column=9)

        frame_g = Frame(my_window)
        frame_g.grid(row=2, column=1)
        c = self.conn.cursor()
        r_set = c.execute('''SELECT * from wellCheck''')
        i = 0
        for member in r_set:
            for j in range(len(member)):
                t = Entry(frame_g, width=10)
                t.grid(row=i, column=j)
                t.insert(END, member[j])
            i = i + 1

        my_window.mainloop()
        









