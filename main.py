import smtplib
import speech_recognition as sr
import pyttsx3
from playsound import playsound
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

# email book
email_book = {
    'pc': 'chkaraborty.pinaki@gmail.com',
    'acl': 'mail4dhacl@gmail.com',
    'freelance': 'freelancer4pc@gmail.com',
    'aditya': 'adityasardar743504@gmail.com',
    'rajendra': 'rajhalder779716@gmail.com'
}


# talk method for play audio from text
def talk(text):
    # rate = engine.getProperty('rate')
    # engine.setProperty('rate', rate - 30)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


# listening value from user
def get_info():
    try:
        playsound('get.mp3')
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


# welcome message
def welcome_msg():
    print('Welcome to mailbot. I send your mail very securely, you only share mail address and message.')
    print('--------------------------------------------------------------------------------------------')
    talk('Welcome to mailbot. I send your mail very securely, you only share mail address and message.')


# get email information
def get_email_info():
    talk('Please tell sender eamil address')
    name = get_info()
    receiver = email_book[name]
    print(receiver)
    talk('please enter subject of email')
    subject = get_info()
    talk('fine. now enter content of email')
    msg = get_info()
    check_mail_before_send(receiver, subject, msg)


def check_mail_before_send(receiver, subject, msg):
    print('if you re-enter value, please call yes otherwise anything')
    talk('if you re-enter value, please call yes otherwise anything')
    command = get_info()
    command = command.lower()
    if 'yes' in command:
        get_email_info()
    else:
        talk('email sending in under process. Please wait with us.')
        send_email(receiver, subject, msg)
        print('Thank You. See you again.')
        playsound('success.mp3')
        talk('Thanks for your waiting. your email is successfully send. Thank you for choosing mailbot')


# sending email
def send_email(receiver, subject, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('chakraborty.pinaki.dh@gmail.com', '9002250502')
    # don't forget to gmail less secure app access on of sender email account
    email = EmailMessage()
    email['From'] = 'chakraborty.pinaki.dh@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(msg)
    server.send_message(email)
    # print('Successfully send email to ' + receiver)



# ####################################################################


welcome_msg()
get_email_info()
