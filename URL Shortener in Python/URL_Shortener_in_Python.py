
from tkinter import *
import pyshorteners
import pyperclip

# Defining the title of the application all while taking tow entries.
root_variable = Tk()
root_variable.title("SHORTNER FOR URL PURPOSES")
root_variable.configure(bg= "green")
url = StringVar()
URL_sort = StringVar()

def urlshort():
    URLsort = url.get()
    generateUrl = pyshorteners.Shortener().tinyurl.short(URL_sort)
    URLsort.set(generateUrl)
def copy():
    generateUrl = URL_sort.get()
    pyerclip.copy(generateUrl)

Label(root_variable, text = "APPLICATION URL SHORTENER", font= "Arial").pack(pady=10)

# Entry one will be what will the main Url paste as the input.
Entry(root_variable,text=url).pack(pady=5)
Button(root_variable, text = "Generate the URL", command=urlshort).pack(pady=5)

# Entry two, will ne the sorted Url on display.
Entry(root_variable,text=URL_sort).pack(pady=5)
Button(root_variable,text="Copy URL", command=copy).pack(pady=5)

