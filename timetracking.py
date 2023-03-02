
class Display:
    def __init__(self):
        import datetime
        import tkinter
        import time
        
        self.now_date_time = datetime.datetime.now()
        self.now_unix_time = int(time.mktime(self.now_date_time.timetuple()))

        self.text_time = f"{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}:{str(datetime.datetime.now().second).zfill(2)}"

        self.gui_start_time = datetime.datetime.now()
        self.gui_start_time_unix = int(time.mktime(self.gui_start_time.timetuple()))

        self.isKommt = False
        self.isGeht = False

        self.gui  = tkinter.Tk()
        self.gui.title("")
        self.gui.geometry("210x180")
        self.gui.bind("<Control-q>", quit)
        self.gui.bind("<Control-Q>", quit)
        self.gui.bind("<Command-q>", quit)
        self.gui.bind("<Command-Q>", quit)
        self.gui.bind("<Alt-F4>", quit)
        self.gui.resizable(False,False)
        self.gui.configure(bg="orange")

        self.current_time = datetime.datetime.now()
        self.current_time_hours = str(self.current_time.hour).zfill(2)
        self.current_time_minutes = str(self.current_time.minute).zfill(2)
        self.current_time_seconds = str(self.current_time.second).zfill(2)
        self.current_date_label_text = f"{str(self.current_time.day).zfill(2)}.{str(self.current_time.month).zfill(2)}.{str(self.current_time.year).zfill(2)}"
        self.current_time_label_text = f"{str(self.current_time.hour).zfill(2)}:{str(self.current_time.minute).zfill(2)}:{str(self.current_time.second).zfill(2)}"
        self.current_time_years = str(self.current_time.year).zfill(4)
        self.current_time_months = str(self.current_time.month).zfill(2)
        self.current_time_days = str(self.current_time.day).zfill(2)
        self.current_time_hours = str(self.current_time.hour).zfill(2)
        self.current_time_minutes = str(self.current_time.minute).zfill(2)
        self.current_time_seconds = str(self.current_time.second).zfill(2)
                
        self.current_time_label = tkinter.Label(self.gui, text = "12:00:00:", bg="blue", fg="white", font = ("Arial", 36, "bold"))
        self.current_time_label.config(text=f"{self.current_time_label_text}")
        self.current_time_label.grid(row=0, column=0, padx='5', pady='2', sticky='ew')
        self.current_time_label.config(text=f"{self.current_time_label_text}")

        self.gui.title(self.current_date_label_text)

        self.running_time_label = tkinter.Label(self.gui, text = "00:00:00", bg="white", fg="blue", font = ("Arial", 36, "bold"))
        self.running_time_label.grid(row=1, column=0, padx='2', pady='2', sticky='ew')

        self.kommt_button = tkinter.Button(self.gui, text = "KOMMT", bg="green", fg="white", width=8, height=2, command=self.kommt)
        self.kommt_button.grid(row=2, column=0, padx='2', pady='2', sticky='w')

        self.geht_button = tkinter.Button(self.gui, text = "GEHT", bg="red", fg="white", width=8, height=2, command=self.geht)
        self.geht_button.grid(row=2, column=0, padx='2', pady='2', sticky='e')
        
        self.update()
        self.gui.mainloop()

    def update(self):
        import datetime
        import time
    
        self.current_time = datetime.datetime.now()
        self.current_time_label.config(text=f"{self.current_time_label_text}")
        self.current_time_label_text = f"{str(self.current_time.hour).zfill(2)}:{str(self.current_time.minute).zfill(2)}:{str(self.current_time.second).zfill(2)}"
        
        if self.isKommt == True:
            self.current_time = datetime.datetime.now()
            self.current_time_unix = int(time.mktime(self.current_time.timetuple()))
            self.time_difference = self.current_time_unix - self.kommt_start_time_unix
            self.rest_seconds = self.time_difference
            self.diff_hours = self.rest_seconds  // (60*60)
            self.rest_seconds  = self.rest_seconds  - (self.diff_hours * 60 * 60)
            self.diff_minutes = self.rest_seconds // 60
            self.diff_seconds = self.rest_seconds - (self.diff_minutes * 60)

            self.running_time_text = f"{str(self.diff_hours).zfill(2)}:{str(self.diff_minutes).zfill(2)}:{str(self.diff_seconds).zfill(2)}"
            
            self.now_unix_time = int(time.mktime(self.now_date_time.timetuple()))
            self.running_time_label.config(fg="green", text=f"{self.running_time_text}")

        if self.isGeht == True:
            self.current_time = datetime.datetime.now()
            self.current_time_unix = int(time.mktime(self.current_time.timetuple()))
            self.time_difference = self.current_time_unix - self.geht_start_time_unix
            self.rest_seconds = self.time_difference
            self.diff_hours = self.rest_seconds  // (60*60)
            self.rest_seconds  = self.rest_seconds  - (self.diff_hours * 60 * 60)
            self.diff_minutes = self.rest_seconds // 60
            self.diff_seconds = self.rest_seconds - (self.diff_minutes * 60)

            self.running_time_text = f"{str(self.diff_hours).zfill(2)}:{str(self.diff_minutes).zfill(2)}:{str(self.diff_seconds).zfill(2)}"
            
            self.now_unix_time = int(time.mktime(self.now_date_time.timetuple()))
            self.running_time_label.config(fg="red",text=f"{self.running_time_text}")
        self.gui.after(1000, self.update)
        
        
    def kommt(self):
        import datetime
        import os
        import time
        self.isKommt = True
        self.isGeht = False
        self.kommt_start_time = datetime.datetime.now()
        self.kommt_start_time_unix = int(time.mktime(self.kommt_start_time.timetuple()))
        time_log = open(f"{os.path.basename(__file__)}_{str(self.now_date_time.year).zfill(4)}-{str(self.now_date_time.month).zfill(2)}-{str(self.now_date_time.day).zfill(2)}.log","a")
        self.kommt_button.configure(state="disabled")
        self.geht_button.configure(state="normal")
        
        try:
            time_log.write(f"Zwischenzeit in hh:mm:ss ==> {self.running_time_text}\n")
        except AttributeError:
            pass
        time_log.write(f"Kommt: {str(self.kommt_start_time.year).zfill(4)}-{str(self.kommt_start_time.month).zfill(2)}-{str(self.kommt_start_time.day).zfill(2)} {str(self.kommt_start_time.hour).zfill(2)}:{str(self.kommt_start_time.minute).zfill(2)}:{str(self.kommt_start_time.second).zfill(2)}\n")
        time_log.close()
        
    def geht(self):
        import datetime
        import os
        import time
        self.isGeht = True
        self.isKommt = False
        self.geht_start_time = datetime.datetime.now()
        self.geht_start_time_unix = int(time.mktime(self.geht_start_time.timetuple()))
        time_log = open(f"{os.path.basename(__file__)}_{str(self.now_date_time.year).zfill(4)}-{str(self.now_date_time.month).zfill(2)}-{str(self.now_date_time.day).zfill(2)}.log","a")
        self.geht_button.configure(state="disabled")
        self.kommt_button.configure(state="normal")

        try:
            time_log.write(f"Zwischenzeit in hh:mm:ss ==> {self.running_time_text}\n")
        except AttributeError:
            pass
        time_log.write(f"Geht:  {str(self.geht_start_time.year).zfill(4)}-{str(self.geht_start_time.month).zfill(2)}-{str(self.geht_start_time.day).zfill(2)} {str(self.geht_start_time.hour).zfill(2)}:{str(self.geht_start_time.minute).zfill(2)}:{str(self.geht_start_time.second).zfill(2)}\n")
        time_log.close()
        
if __name__ == '__main__':
    tt = Display()