from tkinter import * # the greatest way to develop GUI apps.
from translate import Translator # This package helps to translate major languages.


Root = Tk()  # Root Window created with Tk().
Root.title('Tkinter Language Translator')  # Display the title on the Root Window.

#  LanguageChoice stores the language of the text that is being translated.
LanguageChoice = StringVar()
# TranslateLanguage stores the language in which the text is to be translated
TranslateLanguage = StringVar()

LangChoices = {'Romanian', 'English', 'French', 'Spanish', 'Hindi', 'German',
               'Hungarian'}  # Create a tuple with language options.
LanguageChoice.set('Romania')
TranslateLanguage.set('Hungarian')


def Translate(): # This function is created to translate the text
    translator = Translator(from_lang=LanguageChoice.get(), to_lang=TranslateLanguage.get()) # helps to translate text
    translation = translator.translate(TextVar.get()) # TextVar contains the text that is to be translated.
    OutputVar.set(translation) # OutputVar is a variable that stores the translated text.


# Choice for input language.
LanguageChoiceMenu = OptionMenu(Root, LanguageChoice, *LangChoices)
Label(Root, text='Choose a language').grid(row=0, column=1)
LanguageChoiceMenu.grid(row=1, column=1)

# Choice in which the language is to be translated.
NewLanguageChoiceMenu = OptionMenu(Root, TranslateLanguage, *LangChoices)
Label(Root, text='Translated Language').grid(row=0, column=2)
NewLanguageChoiceMenu.grid(row=1, column=2)

# Create a Label in Tkinter.
Label(Root, text='Enter Text').grid(row=2, column=0)
TextVar = StringVar()
TextBox = Entry(Root,textvariable=TextVar).grid(row=2, column=1) # This widget helps to enter or display a single line text

Label(Root, text='Output Text').grid(row=2, column=2)
OutputVar = StringVar()
TextBox = Entry(Root, textvariable=OutputVar).grid(row=2, column=3)
# Button for calling function.
But = Button(Root, text='Translate', command=Translate, relief=GROOVE).grid(row=3, column=1, columnspan=3) #This widget creates a button.

mainloop() # It helps to run the tkinter event loop.

