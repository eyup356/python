from gtts import gTTS
import os
text = input("Please input any words (Turkish): ")
language = "tr"
speech = gTTS(text=text,lang=language,slow=False)
speech.save("text.mp3")
os.system("start text.mp3")
