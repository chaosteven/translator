Package Summary
This package translates a website and outputs the website with the translations next to the starting language.
This can used to translate a website's text that can otherwise be more difficult to translate or can be used to learn a language.
There is a few languages that are supported as of right now, such as English, French, Chinese and Spanish. 

INSTALLATION REQUIREMENTS
There are a few modules/libraries needed for the translator.py to work such as Beautifulsoup, CSV, translator, and requests.
These can be installed through command prompt using the commands

$ pip install beautifulsoup4
$ pip install translate
$ pip install csv
$ python -m pip install requests

After downloading, download translator.py with the link provided. 

After downloading all the packages, open translator.py with either any programming software or terminal to run the program using python3 project.py. 
It should prompt what language the website is in as of now and what language you want to translate it to. Afterwards, it should prompt you to input 
the url of the website that is needed to be translated. 
The program will then translate all text available to be translated into the desired language and should create a csv file with 
everything possible translated next to the original text.

CODE
The code uses multiple modules/packages to both retrieve the url from the url that was inputted by the user through the use of requests 
and then from that link retrieves the html data needed for translation with the translate module. Beautifulsoup is used for navigating through the html 
data to find the text needed to be translated and with a for loop, allows for the translation to be encoded into a csv file along with the orignal text 
next to it. Interacting with the user to make it easy to use was important to me so I used an interface that allowed for a multiple choice option for both
selections for language rather than making them type out the language. 

THOUGHTS/CHECKLIST
I was unfamiliar with htmls and web requests but with tutorials and packages it was an interesting experience. I used as many modules as necessary to get 
my program working and it only took four and I had to stop using another module becauseit has stopped working unexpectantly. There are a few variables that
I had used to make sure everything ran smoothly such as the variables for the two languages that are inputted by the user as there were errors with using 
the default autodetect function installed. I tried using good spacing for code that was different from each other and tried to keep code that was relevant
to each other closer as it made more sense for me. I also tried keeping code that was fine being at the start there to keep the rest of the code unclutered.
I had commented on aspects of the code that needed to be explained a bit and tried to keep it brief but informative.


