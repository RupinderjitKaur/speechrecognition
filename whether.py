#new code
import speech_recognition as sr
import urllib.request
def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Say Something!')
        audio = r.listen(source,timeout=1,phrase_time_limit=2)
        


        
        print ('Done!')

    try:    
        text = r.recognize_google(audio)
        city = text.split()
        print(city)
      
        city_name = '+'.join(city)
        st = "http://api.apixu.com/v1/current.json?key=e5467e944bfd427ebe841700192905&q="+city_name+""
      
        x = urllib.request.urlopen(st)
        y = str(x.read(),'utf-8')
        print(y)

        return (y,text) 
    except:
        pass

def get_forecats(days):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Say Something!')
        audio = r.listen(source,timeout=1,phrase_time_limit=2)
        


        
        print ('Done!')

    try:    
        text = r.recognize_google(audio)
        city = text.split()
        print(city)
      
        city_name = '+'.join(city)
        st = "http://api.apixu.com/v1/forecast.json?key=e5467e944bfd427ebe841700192905&q="+city_name+"&days="+str(days)+""
      
        x = urllib.request.urlopen(st)
        y = str(x.read(),'utf-8')
   

        return (y) 
    except:
        pass
