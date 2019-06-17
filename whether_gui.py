from tkinter import * 
import whether
import speech_recognition as sr
import urllib.request
import json
from PIL import Image,ImageTk
from gtts import gTTS
from pygame import mixer
import requests
from io import BytesIO
import time
class Whether:
    

    def get_whether(self):
       
        mixer.init()
        mixer.music.load('wait.mp3')
        mixer.music.play()
        time.sleep(1)
        
        
        try:
            data = whether.get()
            data_ = json.loads(data[0])
            datai = data[1]
            sound = gTTS("We have founded a city similar to"+str(datai)+
                         "current temprature of"+str(datai)+"is"+str(int(data_["current"]["temp_c"]))+"degree celcius")
            sound.save('sol.mp3')
            mixer.init()
            mixer.music.load('sol.mp3')
            mixer.music.play()
            
            self.city_name.set(data_["location"]["name"])
            self.count_name.set(data_["location"]["country"])
            self.city_time.set(data_["location"]["localtime"])
            self.tempc.set(data_["current"]["temp_c"])
            self.tempf.set(data_["current"]["temp_f"])
            self.humidity.set(data_["current"]["humidity"])
            img_url = 'http:'+data_["current"]["condition"]["icon"]
            response = requests.get(img_url)
            img_data = response.content
            
            self.image = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))       
            self.whether = Label(text="image",image=self.image)

            self.whether.place(x=450,y=250)
            self.text = Label(text=data_["current"]["condition"]["text"],font=('',12))
            self.text.place(x=450,y=310)
            

        except Exception as e:
        
            mixer.music.load('error.mp3')
            mixer.music.play()
                
                
            
            print("no result",e)

        
        
            

        

    def __init__ (self):
        
        self.main = Tk()
        self.mainFrame = Frame(self.main,height=650,width=600)
        self.main.geometry('600x550')
        #self.main.call('wm', 'iconphoto', Tk._w, ImageTk.PhotoImage(Image.open('logo.ico')))
        

        self.label = Label(text="Whether Station",font=('',30),fg="red")
        self.label.place(x=150,y=50)

        self.city_name = StringVar(self.main)
        self.count_name = StringVar(self.main)
        self.city_time = StringVar(self.main)
        self.tempc = StringVar(self.main)
        self.tempf = StringVar(self.main)
        self.humidity = StringVar(self.main)

        # self.whether = Label(text="image",font=('',12))
        # self.whether.place(x=450,y=310)

        self.label = Label(text="Press the search button.",font=('',18))
        self.label.place(x=10,y=150)

        self.btn = Button(text = "Click Me!",font=('',15),bg='orange',command=self.get_whether)
        self.btn.place(x = 320,y=150)

        self.frame = Frame(self.mainFrame,height=500,width=780)

        self.label = Label(self.frame,text = "City Name",font=('',15))
        self.label.grid(row=0,column=0,pady=10)


        self.entry = Entry(self.frame,font=('',15),textvariable = self.city_name)
        self.entry.grid(row=0,column=1)

        self.label = Label(self.frame,text = "Country Name",font=('',15))
        self.label.grid(row=1,column=0,pady=10)

        self.entry = Entry(self.frame,font=('',15), textvariable = self.count_name)
        self.entry.grid(row=1,column=1)

        self.label = Label(self.frame,text = "City Time",font=('',15))
        self.label.grid(row=2,column=0,pady=10)

        self.entry = Entry(self.frame,font=('',15), textvariable = self.city_time)
        self.entry.grid(row=2,column=1)

        self.label = Label(self.frame,text = "Temp (Celcius)",font=('',15))
        self.label.grid(row=3,column=0,pady=10)

        self.entry = Entry(self.frame,font=('',15), textvariable = self.tempc)
        self.entry.grid(row=3,column=1)

        self.label = Label(self.frame,text = "Temp (Ferh)",font=('',15)) 
        self.label.grid(row=4,column=0,pady=10)

        self.entry = Entry(self.frame,font=('',15), textvariable = self.tempf)
        self.entry.grid(row=4,column=1)

        self.label = Label(self.frame,text = "Humidity",font=('',15) )
        self.label.grid(row=5,column=0,pady=10)

        self.entry = Entry(self.frame,font=('',15), textvariable = self.humidity)
        self.entry.grid(row=5,column=1)





        self.frame.place(x=50,y=210)
        self.mainFrame.place(x=0,y=0)


y = Whether()




