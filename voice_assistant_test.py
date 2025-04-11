import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour==00 and hour<12:
            speak("Wish you a beautiful Morning. Its time for your breakfast")
    elif hour>=12 and hour<18:
            speak("Good Afternoon, Pradnyesh. How's your day going")
    elif hour>=18 and hour<20:
            speak("Its time to hit the gym !")
    else:
           speak("Hey Prad..!!")

speak("Hey Pradnyesh, are you alright?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def takecommand():
       
       ''' It takes voice as input and gives output

       '''

       r=sr.Recognizer()
       with sr.Microphone() as source:
              print("Listening....")
              r.pause_threshold = 1
              audio = r.listen(source)

       try:
              print("Recognizing....")
              query = r.recognize_google(audio, language='en-in')
              print(f"User said: {query}\n")
              
       except Exception as e:
              
              print("Say that again....")
              return "None"
       return query


              
if  __name__=="main_":
       Wishme()
       while True: 
              query = takecommand().lower()

              if 'wikipedia' in query:
                     speak('Searching for result..')
                     query = query.replace("wikipedia","")
                     results= wikipedia.summary(query,sentences=2)
                     speak("According to wikipedia")
                     print(results)
                     speak(results)

              elif 'open youtube' in query:
                     webbrowser.open("youtube.com")

              elif 'open google' in query:
                     webbrowser.open("google.com")

              elif 'open instagram' in query:
                     webbrowser.open("instagram.com")

              elif 'open spotify' in query:
                     webbrowser.open("spotify.com")

              elif 'what is the time' in query:
                     strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                     speak(f"Sir, the time is {strTime}")

              

              elif 'email to Pradnyesh' in query:
                     try:
                            speak("What should I say?")
                            content = takecommand()
                            to = "pradnyesh.bhalange95@gmail.com"    
                            sendEmail(to, content)
                            speak("Email has been sent!")
                     except Exception as e:
                            print(e)
                            speak("Sorry!! I am not able to send this email")