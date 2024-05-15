import os
from gtts import gTTS
mytext = 'Hello Everyone'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

 
myobj.save("welcome.mp3")


os.system("start welcome.mp3")