# Streamlit from Scratch: 1. Getting Started

## Which tools do you need and how to use them; and how to create your first interactive web app in Python

![](https://raw.githubusercontent.com/alanjones2/streamlitfromscratch/main/images/cover.png)


 Streamlit is a framework for creating simple and elegant web applications in pure Python. It's mainly aimed at Data Scientists and Analysts but can also be used as a general-purpose framework for creating web applications.
 
No knowledge of HTML or Javascript is needed. Indeed, you can create a simple web page with barely any knowledge of Python!

This is the first in a series of articles in which we will discover how Streamlit can be used to create anything from a simple text-based web page to a sophisticated, interactive dashboard with data visualizations. 

First, we look at how to get started, which tools we need to download (there aren't many) and how to edit and run your first Streamlit app.


## Getting started

Here is the code for a simple web page that consists only of text:

```` Python
import streamlit as st

st.title("Hamlet said…")
st.text("""
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them.
""")
````

_Listing 1 - hamlet.py_

And it looks something like this:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/hamlettextscreenshot.png)

Not particularly exciting but it shows just how easy it is to produce a simple web page. 

In this series we will go quite a lot beyond this, though, creating web applications that are interactive and include data visualizations in Pandas, Plotly and more.

But first, we need to install the tools.

## Installing Python and Streamlit

We need Python installed on our computer and, of course, Streamlit, too. We will also need an editor to create our apps and a browser to run them in.

One of the easiest ways of getting Python is to install the Anaconda distribution. Anaconda consists of a fairly up-to-date version of Python plus a whole bunch of libraries. It's a fairly big installation but by using Anaconda you will save yourself the trouble of having to manually install those libraries later. The main alternative is to install the official Python distribution from their website.

The [Python](python.org) website always contains the latest version of Python. If you download [Anaconda](anaconda.com), you may not get the latest version. But that is not a bad thing because, while it might not be the most up-to-date, you will be sure to get a version that works with all of the libraries that come with it. 

When a new version of Python is released, it can sometimes take a while for the library distributions to catch up, so while installing from [python.org](python.org) will give you the latest version, the [Anaconda](anaconda.com) version may be the safest (although you can, of course, get older versions from [python.org](python.org), too).

So, go to the Anaconda or Python websites and download and install the version for your machine. I would not advise installing both unless you want to confuse your operating system and yourself (it __is__ possible to install both if you exercise some care but there is not much point. If you can't decide which to choose, go for Anaconda - it's what the Streamlit folk recommend).

Whichever you choose, you will still have to install Streamlit.

From a command window (use the Anaconda one if that is what you have installed) run the command:

````
pip install streamlit
````

## Editors

Almost any editor is suitable for writing Streamlit apps. If you are already a Python programmer then you will already have your favourite - maybe one of the IDEs, VSCode or PyCharm - but a simple general-purpose editor such as __Sublime Text__ or __Notepad++__ is perfectly adequate, too.

When we run normal Python programs we issue the following command:

````
# This won't work with Streamlit
python myprogram.py 	
````

And IDEs such as VSCode and PyCharm assume this when running Python programs. However, the command we need to run a Streamlit app is:

````
# This how to run a Streamlit app
streamlit run myprogram.py
````

The consequence of this is that the standard 'Run' command in VSCode or PyCharm doesn't work for Streamlit apps. 

The easiest way around this is to type the correct command in a command window. This can be external to the editor, like the Anaconda prompt, or the built-in terminal window in your operating system. 

If you use a simple editor such as Sublime Text or Notepad++ this is the best approach. You can modify both of these editors to add a terminal window (Sublime) or add a commad to run your app (Notepad++) but the simplest method is to use the Anaconda Prompt (or Powershell Prompt) window, if you have installed Anaconda, or the standard terminal window for your operating system, if you've installed standard Python.

Here are screenshots of the Sublime Text and Notepad++ editors side-by-side with an Anaconda Powershell prompt.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/sublimetext.png)

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/notepadpp.png)


If you are a seasoned Python programmer, already have your favourite version of Python installed and use VSCode or PyCharm, you can use a terminal window within the your IDE. In VSCode there is a Terminal menu option where you can open a new terminal

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/openVCSterminal.png)

 and in PyCharm, go to the Views menu and find the Terminal option in Tool Windows.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/openPyCharmterminal.png)

So, to run your program from one of these IDEs type the run command into the terminal window.

_**Warning...** it's probably best to only use the built-in terminals if you are using a standard Python installation. If you have installed Anaconda, this may not work well with VSCode or PyCharm because the default terminal may not be able to find the Anaconda Python installation. There are ways around this but it's beyond our scope to go into that here. If you are using Anaconda it may be simplest to use the Anaconda prompt to run your apps no matter which editor/IDE you use._ 

## Which editor should you use

VSCode and Pycharm are quite sophisticated IDEs. VSCode is a general-purpose tool that can be customized with plugins to support many different languages. PyCharm is, if anything, more capable than VSCode but is dedicated to Python programming.

Sublime Text is simple to use, quick to download and install but not free: you can download a free trial version but are expected to pay for a license. Having said that, the trial never expires.

The Notepad++ user interface is, perhaps a little busier than Sublime but it is also a perfectly capable editor and is entirely free.

Both Sublime and Notepad++ support colour highlighting of Python code, which is nice. So too, of course, do VSCode and PyCharm.

If you are already a VSCode or PyCharm user then the best bet is to carry on using these but if you don't, then Sublime Text or Notepad++ are probably easier to start with.

There is one more tool that we need to run a Streamlit app and that is a browser such as Chrome, Firefox or Edge. But I assume that you have one of these already.

So, now we have all the tools, we are ready to create our first Streamlit app.

## Editing and running 'Hello Hamlet'

'Hello World' has been the traditional first program that anyone writes in any language for decades - it just displays 'Hello World' on the screen. The first time I came across it was in the book "The C Programming Language" by Brian W. Kernighan and Dennis M. Ritchie whose first edition came out in 1978 (although my copy was the second edition that was published 10 years later).

We've already seen our first program: it's Hamlet. But it is pretty much the equivalent of 'Hello World' as it just writes some text.

I'll repeat it here so we can run through an explanation of how it works.

```` Python
import streamlit as st

st.title("Hamlet said…")
st.text("""
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them.
""")
````

_Listing 1 - hamlet.py_

This is one of the simplest Streamlit programs you can imagine. It just writes two strings - one formatted as a title and the other as pre-formatted text.

The first line will be familiar to a Python programmer; it imports a Python library - the Streamlit library. As you may well know a Python library is a package of code that contains useful functions that can be incorporated into a Python program. In this case, the Streamlit library incorporates all of the functionality that turns a simple Python program into a web app and provides us with a large number of functions that allows us to build that web app and make it look good.

The Streamlit library is imported with the name ``st`` so that all of the functions that we use from that library are preceded with that name.

There are two Streamlit functions that we use: ``st.title()`` which formats text in a large bold font and ``st.text()`` which displays pre-formatted text.

For those unfamiliar with Python, there are four ways of quoting a string. We can use single or  double quotes like this ``'To be or not to be...'``, or ``"To be or not to be..."`` but these strings must be all on one line. Alternatively, we can use triple quotes like this:

```` Python
'''To be or not to be,
   that is the question'''
````
or

```` Python
"""To be or not to be,
   that is the question"""
````

The triple quoted strings can run over more than one line.

To run the program, type in the text exactly as you see it above and then, in a terminal, run

````
streamlit run hamlet.py
````

The terminal will respond with a message similar to this:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/strunninginterminal.png)


Your default browser will then be started with the web page that has been generated by Streamlit. (If for some reason it does not start automatically then simply cut and paste the URL given in the terminal window into the address bar of your browser.)

One of the nice things about Streamlit is that it knows when you have made a change to the code. If you edit and save your program, then the web page will display the option to re-run the app. When you do so the new version is displayed.

Try changing the text and then save it. In your browser, you will see that you are invited to re-run the app.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/ScreenshotHamletChanged.png)

Click on the _Rerun_ button and you will see an updated web page that reflects the changes that you made.

## More ways of displaying text

We have used ``st.text()`` to display Hamlet's speech but there are other ways of displaying text. Here is an expanded version of the Hamlet program.

It uses ``st.caption()`` to display a small-font caption under the quote and then uses ``st.header()``, ``st.subheader`` and ``st.write`` to display some comments about the quote.

I'm certain that you can guess what these will do. A header has a large bold font, but smaller than a title; a subheader is similar but smaller; and ``st.write`` displays 'normal' text.

One thing that you should note is that unlike ``st.text()``, ``st.write()`` does not preserve the layout of the text in a string.

````Python
import streamlit as st

st.title("Hamlet")

st.text("""
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them.
""")

st.caption("Hamlet by William Shakespeare, Act 3, Scene 1")

st.header("Hamlet's soliloquy")
st.subheader("The famous speech from the 'Nunnery scene'")
st.write("""In the speech, Hamlet considers suicide, but considers that the 
            alternative to his unhappy life might be even worse.""")
````
_Listing 2 - hamlet2.py_

You can see the result in the screenshot, below.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/hamlet2textscreenshot.png)

For completeness, we should also mention two other ways of displaying text.

For programmers there is ``st.code()``. This will display text as if it were program code. For example:

```` Python
st.code("""
if hamlet == "The Prince of Denmark":
    print("That's our man!")
else:
    print("This is an imposter")
""")
````
![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/ScreenshotCodeBlock.png)

You can see that certain words like ``if`` and ``else`` are highlighted as keywords. The block has a coloured background and, if you position your cursor over the block, you will see an icon for copying the text.

If you need to display Latex strings such as mathematical formulae then you can use ``st.latex()``, e.g.

````Python
st.latex(" \int f^{-1}(x-x_a)\,dx")
````

displays the following:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/ScreenshotLatex.png)

## A little interaction

Streamlit gives us many ways to interact with the user by using menus, buttons, sliders and more. We'll look at these in more detail later but to give you a flavour we'll Write a simple program to select a piece of Shakespeare to display.

The code below uses the value of a set of radio buttons to decide which quote to display. If 'Twelfth Night' is selected the variable ``text`` is set to one quote, otherwise, if 'Hamlet' is selected ``text`` is set to a different quote.

The function ``st.radio()`` is used to select a value. Its parameters are a string that is used as a prompt followed by a list of string values that will be used to label the radio buttons. The function returns the value of the selection.

```` Python
import streamlit as st

quote = st.radio("Select a quote from...",('Hamlet', 'Twelfth Night'))

if quote == 'Twelfth Night':
    text = """
    If music be the food of love, play on;
    Give me excess of it, that, surfeiting,
    The appetite may sicken, and so die.
    """
elif quote == "Hamlet":
    text = """
    To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune,
    Or to take arms against a sea of troubles
    And by opposing end them.
    """

st.title(quote)
st.text(text)
````
And this is what it looks like:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/ScreenshotQuotes.png)

When the user selects either 'Hamlet' or 'Twelfth Night' the entire program is re-run so that the if statement is executed and the appropriate quote is displayed.

This is an important aspect of Streamlit: whenever the user interacts with a program, it is run again from the beginning and the web page is reloaded.

## Conclusion

In this first article, we've seen how to set ourselves up to edit and run a Streamlit app and how to write an app that displays different types of text. As a bonus, and as a taste of things to come, we've also looked at some simple user interaction that allows the user to change the behaviour of the program.

In future articles we will see more ways of interacting with the user, how to display images and graphs, how to design and lay out a Streamlit app using columns and containers and much more.

Thanks for reading - I hope you have found it useful. You can find a link to the code for this article on my [Github page](alanjones2.github.io) as well as links to other articles.

To keep up to date with what I am doing, you can subscribe to my occasional free newsletter [Technofile](technofile.substack.com)