import speech_recognition as spr 
from google_trans_new  import google_translator 
from gtts import gTTS 
import os 

recog1 = spr.Recognizer() 

mc = spr.Microphone() 


with mc as source: 
	print("Speak the password for language Translation !") 
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
	recog1.adjust_for_ambient_noise(source, duration=0.2) 
	audio = recog1.record(source,duration=4)
	MyText = recog1.recognize_google(audio) 
	MyText = MyText.lower() 


if 'hello' in MyText: 
	 
	translator = google_translator()
	

	from_lang = 'en'
	
	 
	to_lang = 'it' 
	
	with mc as source: 
		
		print("Speak any sentence...") 
		recog1.adjust_for_ambient_noise(source, duration=0.2) 
		
		 
		audio = recog1.record(source,duration=10) 
		
		 
		get_sentence = recog1.recognize_google(audio) 

		 
		try: 
			
			 
			print("Phase to be Translated :"+ get_sentence) 

			
			text_to_translate = translator.translate(get_sentence, lang_src= from_lang,lang_tgt= to_lang)
													 
													 
			
			
			text = text_to_translate

			
                        
			speak = gTTS(text=text, lang=to_lang, slow= False)
			print("resut:",text)

			 
			speak.save("captured_voice.mp3")	 
			
			 
			os.system("start captured_voice.mp3") 

		 
		except spr.UnknownValueError: 
			print("IAM UNABLE TO UNDERSTAND UR INPUT") 
			
		except spr.RequestError as e: 
			print("UNABLE TO PROVIDE THE REQUIRED OUTPUT".format(e)) 

