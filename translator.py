#importing all the modules being used such as the translator, html retriever, html decoder and exporting to a csv file
from translate import Translator
from bs4 import BeautifulSoup
import csv
import requests

#Using csv to create a file for output and using encoding utf-8 allows for the html translations to be placed in the csv file without errors
csv_file = open('cms_scrape.csv', 'w', encoding="utf-8") 
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Orignal Text', ' ', 'Translated Text']) 

#Starting with default languages can allow us to change the language later on
startlang = "en"
lang = "en"

#This is the first interface the user is interacting with and allows for them to choose the language they want to translate from
startls = input("Enter the capital letter for the language the website you want to translate from: A.English B.French C.Chinese D.Spanish: ")

#Conditionals for choosing language they are translating from
if startls == "A" :
    
    startlang = "en"
    print("You have selected English")

elif startls == "B" :
    
    startlang = "fr"
    print("You have selected French")

elif startls == "C":
    
    startlang = "zh"
    print("You have selected Chinese")

elif startls == "D":
    
    startlang = "es"
    print("You have selected Spanish")

else:
   
    print("Error, capitilize the letter or input an valid response")

#The second interface users are interacting with that determines language they want to translate the website to
ls = input("Select a capital letter for the language to translate webpage to: A.English B.French C.Chinese D.Spanish: ")

if ls == "A" :
    
    lang = "en"
    print("You have selected English")

elif ls == "B" :
    
    lang = "fr"
    print("You have selected French")

elif ls == "C":
    
    lang = "zh"
    print("You have selected Chinese")

elif ls == "D":
   
    lang = "es"
    print("You have selected Spanish")

else:
    
    print("Error, capitilize the letter or input an valid response")

#The translator is now being set to what the user defined and the url input is asked as well
#Using requests and beautifulsoup to get the html and allowing us to find what we need for translation

translator = Translator(from_lang = startlang, to_lang = lang)
url = input("Enter the website you want to translate from: ")
source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')
space = "  "

#The actual translation is placed in this for loop that writes to a csv file with the rows of original text a space and the translated text to what the user desired.
tag = soup.body

for string in tag.strings:
    
    translation = translator.translate(string)
    
    csv_writer.writerow([string, space, translation])

#Displays a text to inform users that the url has been translated and closes the csv file, ready to be opened.
print("CSV file has been created and the url is translated!")

csv_file.close()