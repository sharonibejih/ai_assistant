# import speech_recognition as sr
# r = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio=r.listen(source)

#         try:
#             request=r.recognize_google(audio,language='en')
#             if "astra" in request.lower():
        
#                 print('Loading your fashion assistant - ASTRA')

#             else:
#                 print("Were you trying to call Astra?")

#         except:
#             pass

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")