#import all the necessary packages 
from __future__ import unicode_literals
import youtube_dl
from tkinter import *
from tkinter import messagebox
from os import listdir
import os
from moviepy.editor import *
import speech_recognition as sr
from collections import Counter
import nltk
from os import path
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
import random
from urllib.request import urlretrieve
from urllib.parse import quote
import webbrowser as wb
root = Tk()
root.title("Relevant Sentence Formation")
l1=Label(root,font=('Comic Sans MS',18),text="Enter a YouTube URL")
l1.grid(row=0,column=0)
e1=Entry(root,width=30,font=('Times New Roman', 18))
e1.grid(row=0,column=1)
e1.insert(0, "")

def myClick():
    
    
    
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    #str1 = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    #str1 = 'https://www.youtube.com/watch?v=t2-ees0O6_U'
    #str1 = 'https://www.youtube.com/watch?v=pmXwGQmWmBA'
    #str1 = 'https://www.youtube.com/watch?v=nTSl4DuwJVk'
    str1 = e1.get()
    #print(e1.get()) 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([str1])

#after downloading the video
#search for file with .mp4/.m4a extension
    
    import os
    import glob
# files                                                                         
    lst = glob.glob("*.mp3")
    #print(lst)
 
    for file in lst:
# convert wav to mp3
    	os.system(f"""ffmpeg -i {file} -acodec pcm_u8 -ar 22050 {file[:-4]}.wav""")    
#remove the mp3 files present already
    #for file in lst:
     #   os.remove(file)
#D:\6th Semester\Mini Project\codes\InOurTime-20070621-CommonSensePhilosophy.wav
    import os
    from pydub import AudioSegment

   # path = "the path to the audio files"

#Change working directory

    #os.chdir(path)

   #audio_files = os.listdir()
# You dont need the number of files in the folder, just iterate over them directly using:
    for file in os.listdir():
    #spliting the file into the name and the extension
        name, ext = os.path.splitext(file)
        #print(name)
        if ext == ".mp3":
           mp3_sound = AudioSegment.from_mp3(file)
           #rename them using the old name + ".wav"
           mp3_sound.export("{0}.wav".format(name), format="wav")
# obtain path to "english.wav" in the same folder as this script
    lst1 = glob.glob("*.wav")
    #print(lst1)
    str3 = ""
    
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), str(lst1[0]))
    print("processing the file")
# use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
    try:
        #print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        string1 = r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    print("file is processed and now to be split")
    split_it = string1.split() 
  
# Pass the split_it list to instance of Counter class.

    global counter1
    counter1 = Counter(split_it) 
    for file in os.listdir():
    #spliting the file into the name and the extension
        name, ext = os.path.splitext(file)
        print(name)
        if ext == ".mp3" or ext==".wav":
            os.remove(file)
# most_common() produces k frequently encountered 
# input values and their respective counts. 
    most_occur = counter1.most_common(15)
    list1 = []
    for i in range(15):
        list1.append(most_occur[i][0])
    print("most frequent words are"+str(list1)) 
    for i in list1:
        if(i=='the' or i=='an' or i=='h.' or i == 'i.' or  i=='be' or i=='a' or i=='are' or i=='in' or i=='and' or i =='.' or i =='for' ):
            list1.remove(i)
    #print(list1)
    def converttostr(input_seq, seperator):
   # Join all the strings in list
       final_str = seperator.join(input_seq)
       return final_str
    seperator = ' '
    string1 = converttostr(list1,seperator)
    #print(string1)
    stop_words = set(stopwords.words('english'))
    tokenized = sent_tokenize(string1)
    tag = nltk.pos_tag(tokenized)
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp  = nltk.RegexpParser(grammar)
    result = cp.parse(tag)
    #print("hello")
    tokens = nltk.word_tokenize(string1)
    text = nltk.Text(tokens)
    string1 = string1+" what is was were"
    print(string1)
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(string1)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    #print(nouns)
    is_verb = lambda pos: pos[:2] == 'VB'
    tokenized = nltk.word_tokenize(string1)
    verbs = [word for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)]
    #print(verbs)
    is_q = lambda pos: (pos[:2] == 'WDT' or pos[:2] == 'WP' or pos[:2] == 'WRB') 
    tokenized = nltk.word_tokenize(string1)
    q = [word for (word, pos) in nltk.pos_tag(tokenized) if is_q(pos)]
    #print(q)
    print(string1)
    st = []
    for noun in nouns:
        for verb in verbs:
            for i in q:
                st.append(i+" "+verb+" "+noun)
    #print(st)
    st_correct = []
    
    r = random.randint(0,len(st))
    qstr = quote(st[r])
    thing = urlretrieve("https://www.duckduckgo.com/?q=" + qstr)
    print("opening in browser")
    import webbrowser as wb
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    wb.get(chrome_path).open("https://www.google.com/?q=" + qstr)

myButton = Button(root,font=('Calibri',16),text="Click here", command=myClick)
myButton.grid(row=2,column=1)
root.mainloop()

