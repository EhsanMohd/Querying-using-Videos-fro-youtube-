# Querying-using-Videos-fro-youtube-
Import all the necessary packages:  
1)tkinter for creation of GUI 
2)youtube_dl for downloading of video content from youtube 
3)os for searching the file system and performing file specific operations 
4)nltk for natural language processing 
5)collections for counting most frequent words 
6)random for generating random numbers and choices 
7)urllib for performing actions with URL such as retrieving , creating URLs, etc 
8)webbrowser for searching the web 
9)speech_recognition for recognising speech and converting to text 
10)moviepy for converting media files from one format to other 
 
Steps: 
1) The elements are added using a grid on the GUI window, a label asking for input 
as URL and a textbox where the input can be provided and a button which on 
being clicked will execute the code of the module i.e. processing of the video 
provided as URL to the generation and opening of the URL in the browser  2) Using download() function of youtube_dl and passing the URL as a string 
parameter the video is downloaded as .mp3 file  3) Using glob function of glob package the paths of all .mp3 files are fetched and put 
into a list and then using os package are converted into .wav files  4) Then we delete the downloaded files of .mp3 format  5) The speech_recongition package is used to create a recognizer object with 
Recognizer class and the given .wav file acts as a source to the recognizer object 
using AudioFile() function and record() function  6) The recognize_sphinx() takes the audio source as parameter and outputs the string 
of recognized text  
13 
 
7) Then using the split() function we split the string into words and count the 
frequency of each word using counter object or Counter class and also obtain the most common ‘n’ words using the function most_common(n)  8) All the unnecessary words such as articles, conjunctions and prepositions are 
removed and the list again is appended to form and string  9) Using the stop words from English we obtain the stop words from nltk packages  10) Using pos_tag() function and word_tokenize() we obtain the three lists , one 
comprising all the nouns , other one of all the verbs and third one of all the 
question words  11) Later using exhaustive enumeration we obtain all the sentences which can be 
formed from these words obeying certain format and store them in a list  12) Using random.randint() we generate a number which chooses a given sentence 
from the list of sentences 13) Using quote() we form the hind part of the URL (search query)  14) Using webbrowser package’s get() and open() functions we append the hind part 
of the URL to a search engine such as google.com and open the complete URL 
using the path of the webbrowser.    
