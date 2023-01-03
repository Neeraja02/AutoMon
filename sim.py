import tkinter as tk
from tkinter import ttk
import time
import random
import tkinter.font as tkFont
import mysql.connector

class WheelLoader(tk.Tk):

    bucket_weight = 0
    bucket_threshold = 100
    pass_count = 0
    truck_threshold = 400
    truck_payload_weight = 0
    truck_ID = 1

    mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "AtideviN@Jun14" , database = "truck")

    mycursor = mydb.cursor()

    def __init__(self):

        super().__init__()

        sql = "TRUNCATE TABLE truck_info"

        try:
           # Execute the SQL command
           self.mycursor.execute(sql)
           
           # Commit your changes in the database
           self.mydb.commit()
        except:
           # Roll back in case there is any error
           self.mydb.rollback()

        # configure the root window
        self.title('                                                STORE FEATURE TRUCK PAYLOAD SYSTEM')

        #setting window size
        width=700
        height=500

        # getting screen's width in pixels
        screenwidth = self.winfo_screenwidth()

        # getting screen's height in pixels
        screenheight = self.winfo_screenheight()

        #alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        alignstr = '%dx%d+%d+%d' % (width, height, 100 , 100)
        self.geometry(alignstr)
        self.resizable(True, True)
        self.geometry('700x500')
        self['bg'] = 'yellow'

        #Label for Truck Number
        TID_Label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=15)
        TID_Label["font"] = ft
        TID_Label["fg"] = "#333333"
        TID_Label["justify"] = "center"
        TID_Label["text"] = "Truck Number(ID)"
        TID_Label["relief"] = "raised"
        TID_Label.place(x=200,y=30,width=160,height=30)
        
        #Label for Truck Payload Weight
        TPW_Label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=15)
        TPW_Label["font"] = ft
        TPW_Label["fg"] = "#333333"
        TPW_Label["justify"] = "center"
        TPW_Label["text"] = "Truck Payload Weight"
        TPW_Label["relief"] = "raised"
        TPW_Label.place(x=50,y=100,width=200,height=30)

        #Label for Bucket Weight
        BW_Label=tk.Label(self)
        BW_Label["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=15)
        BW_Label["font"] = ft
        BW_Label["fg"] = "#333333"
        BW_Label["justify"] = "center"
        BW_Label["text"] = "Bucket Weight  "
        BW_Label["relief"] = "raised"
        BW_Label.place(x=420,y=100,width=160,height=30)

        #Label for Pass Count
        PC_Label=tk.Label(self)
        PC_Label["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=15)
        PC_Label["font"] = ft
        PC_Label["fg"] = "#333333"
        PC_Label["justify"] = "center"
        PC_Label["text"] = "Pass Count"
        PC_Label["relief"] = "raised"
        PC_Label.place(x=270,y=230,width=120,height=30)

        #Store button
        global storeButton
        storeButton=tk.Button(self)
        storeButton["activebackground"] = "#5fb878"
        storeButton["activeforeground"] = "#5fb878"
        storeButton["anchor"] = "center"
        storeButton["bg"] = "#ADD8E6"
        storeButton["disabledforeground"] = "#999999"
        ft = tkFont.Font(family='Times',size=17)
        storeButton["font"] = ft
        storeButton["fg"] = "#333333"
        storeButton["justify"] = "center"
        storeButton["text"] = "STORE"
        storeButton["relief"] = "raised"
        storeButton.place(x=280,y=390,width=90,height=40)
        storeButton["command"] = self.storeButton_command
        
        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure('TLabel', background='white', foreground='black')

    #TruckID display
        self.label_tID_display = ttk.Label(self, text="1" , font=('Digital-7', 13))  
        self.label_tID_display.pack(expand=True)
        self.label_tID_display.place(x=380,y=30,width=70,height=30)
        
    #Bucket Weight display
        self.label_bw_display = ttk.Label(self, text="0" , font=('Digital-7', 13))  
        self.label_bw_display.pack(expand=True)
        self.label_bw_display.place(x=450,y=150,width=75,height=35)

    #Truck Payload Weight Display
        self.label_tpw_display = ttk.Label(self, text="0", font=('Digital-7', 13))  
        self.label_tpw_display.pack(expand=True)
        self.label_tpw_display.place(x=80,y=150,width=85,height=35)

    #Pass Count Display
        self.label_pc_display = ttk.Label(self , text="0" , font=('Digital-7', 13))
        self.label_pc_display.pack(expand=True)
        self.label_pc_display.place(x=270,y=300,width=75,height=35)
   
    #Bucket filling simulation
        self.label_bw_display.after(1000, self.updatePC)

    def BucketFill(self):
        if self.bucket_weight < 40:
            temp = round(random.uniform(2,5),4)
            self.bucket_weight += temp
            self.bucket_weight = round(self.bucket_weight,4)
        return str(self.bucket_weight)
        
    def updatePC(self):

        self.label_bw_display.configure(text=self.BucketFill())
        
        #Pass Count Updation
        if self.bucket_weight >= 40:
            if(self.pass_count < 20):
                self.pass_count = self.pass_count + 1
                self.label_pc_display.configure(text=str(self.pass_count))
                #time.sleep(1)
                #storeButton.invoke()
                return
            else:
                self.pass_count = 0
                self.label_pc_display.configure(text=str(self.pass_count))
                #time.sleep(1)
                #storeButton.invoke()
                
            #storeButton.invoke()
        #schedule another timer
        self.label_bw_display.after(200, self.updatePC)

    #function that is called when store button is pressed
    def storeButton_command(self):
        
        totalWeight = self.truck_payload_weight + self.bucket_weight

        #Truck payload weight updation
        if(totalWeight > self.truck_threshold):
            #print("next")
            sql = "INSERT INTO TRUCK_INFO(truckID , truckPayloadWeight , passCount ) VALUES (%s , %s , %s)"
            val = (self.truck_ID , self.truck_payload_weight , self.pass_count-1)
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            self.truck_payload_weight = 0
            self.truck_ID += 1
            self.pass_count = 0
            self.label_tID_display.configure(text = str(self.truck_ID))
            self.label_pc_display.configure(text = "0")
        else:
            #print("same")
            self.truck_payload_weight = totalWeight
            self.bucket_weight = 0.0

        self.label_bw_display.configure(text=str(self.bucket_weight))
        self.truck_payload_weight = round(self.truck_payload_weight , 4)
        self.label_tpw_display.configure(text=str(self.truck_payload_weight))
        #change UI after store button is pressed
        storeButton["text"] = "STORED"
        #change UI after few seconds back to the same state
        storeButton.after(3000 , self.buttonChange)
        self.label_bw_display.after(3000, self.updatePC)
        
    def buttonChange(self):
        storeButton["text"] = "STORE"

if __name__ == "__main__":
    load = WheelLoader()
    load.mainloop()
