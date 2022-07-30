
# -----------------------------------------------------   REQUIRED MODULES   ---------------------------------------------------------------------------------------------------------------------------------------

from http import server
import sys
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import speech_recognition as sr
import pyttsx3
import pyaudio
# import pywhatkit
import datetime
import time
import wikipedia
import os
import smtplib

# -------------------------------------------------------   GLOBALLY DEFINED  --------------------------------------------------------------------------------------------------------------------------------------

Yes = ['yah','yes','s','yeah','done','ok']
No = ['not','no','dont','doesnt']

# --------------------------------------------------------   CHROME  ----------------------------------------------------------------------------------------------------------------------------------------------


def auto_chrome(searchText):

    url = 'https://www.google.com'
    drive = webdriver.Chrome(executable_path=r'D:\selenium\chromedriver.exe')   
    drive.get(url)

    drive.maximize_window()

    search = drive.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search.click()
    search.send_keys(searchText + Keys.ENTER)

    time.sleep(10)

    link = drive.find_element(By.XPATH,'/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/a/h3')
    WebDriverWait(drive,20).until(EC.element_to_be_clickable(link)).click()

    time.sleep(60)


# --------------------------------------------------------   FLIPKART    -----------------------------------------------------------------------------------------------------------------------------------------


def auto_flipkart(phno,pwd,searchText):

    url = 'https://www.flipkart.com'
    drive = webdriver.Chrome(executable_path=r'D:\selenium\chromedriver.exe')   
    drive.get(url)

    drive.maximize_window()

    time.sleep(1)

    email = drive.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input')
    email.click()
    email.send_keys(phno)

    pswd = drive.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input')
    pswd.click()
    pswd.send_keys(pwd)

    login_butt = drive.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button')
    login_butt.click()

    time.sleep(1)

    searchBar = drive.find_element(By.NAME,'q')
    searchBar.click()
    searchBar.send_keys(searchText + Keys.ENTER)

    time.sleep(60)


    

# ----------------------------------------------------------    FACEBOOK    -----------------------------------------------------------------------------------------------------------------------------------


def auto_facebook(mail,pwd):

    url = 'https://www.facebook.com'
    drive = webdriver.Chrome(executable_path=r'D:\selenium\chromedriver.exe')   
    drive.get(url)

    drive.maximize_window()

    time.sleep(1)

    name = drive.find_element_by_name('email')
    name.click()
    name.send_keys(mail)

    pswd = drive.find_element_by_name('pass')
    pswd.click()
    pswd.send_keys(pwd)

    login = drive.find_element_by_name('login')
    login.click()

    time.sleep(1)

    account = drive.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]')
    account.click()

    time.sleep(1)

    profile = drive.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[1]/a/div[1]')
    WebDriverWait(drive,10).until(EC.element_to_be_clickable(profile)).click()

    time.sleep(60)

# ---------------------------------------------------------   INSTAGRAM   --------------------------------------------------------------------------------------------------------------------------------------


def auto_instagram(mail,pwd):

    url = 'https://www.instagram.com'
    drive = webdriver.Chrome(executable_path=r'D:\selenium\chromedriver.exe')   
    drive.get(url)

    drive.maximize_window()

    time.sleep(1)

    name = drive.find_element_by_name('username')
    name.click()
    name.send_keys(mail)

    pswd = drive.find_element_by_name('password')
    pswd.click()
    pswd.send_keys(pwd)

    login = drive.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
    login.click()

    time.sleep(3)

    notnow = drive.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
    notnow.click()

    time.sleep(3)

    notnow2 = drive.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
    WebDriverWait(drive,20).until(EC.element_to_be_clickable(notnow2)).click()

    time.sleep(2)

    account = drive.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img')
    WebDriverWait(drive,20).until(EC.element_to_be_clickable(account)).click()

    time.sleep(1)

    profile = drive.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div')
    WebDriverWait(drive,20).until(EC.element_to_be_clickable(profile)).click()

    # highlights = drive.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div/div/ul/li[2]/div/div/div[1]/div/img')
    # WebDriverWait(drive,20).until(EC.element_to_be_clickable(highlights)).click()

    time.sleep(60)

#--------------------------------------------------------   YOUTUBE   -----------------------------------------------------------------------------------------------------------------------------------------


def auto_YouTube(searchText):
    
    url = 'https://www.youtube.com/'
    drive = webdriver.Chrome(executable_path=r'D:\selenium\chromedriver.exe')
    drive.get(url)

    drive.maximize_window()

    time.sleep(1)

    search = drive.find_element(By.XPATH,'/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    search.click()

    time.sleep(1)

    search.send_keys(searchText + Keys.ENTER)
    
    time.sleep(1)

    vedio = drive.find_element(By.XPATH,'/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]')
    WebDriverWait(drive,60).until(EC.element_to_be_clickable(vedio)).click()

    # time.sleep(10)

#------------------------------------------------------    WHAATS APP   -----------------------------------------------------------------------------------------------------------------------------------------------

def auto_whatsapp():

    opt = webdriver.ChromeOptions()
    opt.add_argument(r'--user-data-dir=C:\ProgramData\Microsoft\Windows\Start Menu\Programs')
    opt.add_argument('--profile-directory=Default')

    drive = webdriver.Chrome(executable_path=r'D:\selenium\chromedriver.exe',options=opt)
    drive.get('https://web.whatsapp.com/')
    time.sleep(5)

    drive.maximize_window()

    search = drive.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search.click()
    searchText = take_command().lower()
    search.send_keys(searchText + Keys.ENTER)

    time.sleep(3)

    but = drive.find_element(By.XPATH,'/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/h3')
    but.click()

    time.sleep(10)

# ----------------------------------------------------    RECOGNISING     -------------------------------------------------------------------------------------------------------------------------------------


def switch_func(s):
    if 'wikipedia' in s:
        speak('searching wikipedia...')
        search_query = s.replace('wikipedia','')
        results = wikipedia.summary(search_query,sentences = 3)
        speak('Buddy.....according to wikipedia..')
        print(results)
        speak(results)
    elif 'instagram' in s:
        mail = input('buddy! what is your instagram mail id').lower()
        password = input('buddy please tell your password').lower()
        auto_instagram(mail,password)

    elif 'chrome' in s:
        speak('what do you want to search buddy...')
        search_string1 = take_command().lower()
        auto_chrome(search_string1)

    elif 'flipkart' in s:
        phno = input('enter email or phone number:')
        password = input('enter password:')
        search = input('enter product:')
        speak('which product do you want to check buddy...')
        search_string2 = take_command().lower()
        auto_flipkart(phno,password,search_string2)  

    elif 'facebook' in s:
        mail = input('enter email or phone number:')
        password = input('enter password:')
        auto_facebook(mail,password)
    
    elif 'youtube' in s:
        speak('what do you want to search buddy...')
        search_string3 = take_command()
        auto_YouTube(search_string3)

    elif 'amazon' in s:
        webbrowser.open('amazon.in')
    
    elif 'snapdeal' in s:
        webbrowser.open('snapdeal.com')
    
    elif 'google maps' in s:
        webbrowser.open('www.googlemaps.com')

    elif 'songs' in s:
        auto_YouTube('latest telugu melody songs')
    
    elif 'whatsapp' in s:
        auto_whatsapp()

    elif 'the time' in s:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'the time is {strTime} buddy...')

    elif 'open vs code' in s:
        codePath = "C:\\Users\\kiran\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    
    elif ('buddy sleep' in com) or ('take a nap' in com) or ('go to sleep' in com):
            hour = datetime.datetime.now().hour
            if hour > 20 and hour < 24: 
                speak('ok bye buddy...good nyt...')
            else:
                speak('ok bye buddy...wake me up when you want..')
            return False
    else:
        auto_chrome(s)

#-------------------------------------------------------------------   SPEAKING   ---------------------------------------------------------------------------------------------------------------------------------

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# ----------------------------------------------------------------    LISTENING    ---------------------------------------------------------------------------------------------------------------------------------

def take_command():

    s = sr.Recognizer()
    # mic = 
    # print(mic.list_microphone_names())
    try:
        with sr.Microphone() as source:
            s.adjust_for_ambient_noise(source)
            print('i am listening buddy...')
            s.pause_threshold = 3
            s.energy_threshold = 600.4452854381937
            try:
                search_query = s.listen(source)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service")

            print('i am recognizing buddy...')
            try:
                myText = s.recognize_google(search_query,language='en-IN')
            except:
                print('error occurred while requesting to google. API unavailable')
            myText = myText.lower()
            print(f'user said:{myText}\n')

    except sr.RequestError as e:
        print('could not request results; {0}...'.format(e))

    except sr.UnknownValueError:
        print('Unknown error occurred...')

    return myText

# --------------------------------------------------------------  WISHING   --------------------------------------------------------------------------------------------------------------------------------------  

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<=6:
        speak('good morning buddy...why are you waking me up this early. do you need something..')
    elif hour>6 and hour<=12:
        speak('good morning buddy...whaats up what do you want me to do..')
    elif hour>12 and hour<=15:
        speak('good afternoon buddy...what do you want me to do....')
    else:
        speak('good evening buddy...tell me something to do...')



if __name__ == "__main__":
    print('I am awake...')
    wish_me()
    on = True
    while(on):
        com = take_command().lower()
        if not 'go to sleep' in com:
            k = switch_func(com)
            if(not k):
                engine.stop()
        else:
            engine.stop()
            print('I am sleeping...')