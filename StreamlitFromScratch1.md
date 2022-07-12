# Streamlit from Scratch, 1: Getting Started

## Which tools do you need and how to use them; and how to create your first interactive web app in Python

 Streamlit is a framework for creating simple and elegant web applications in pure Python. It's mainly aimed at Data Scientists and Analysts but can also be used as a general-purpose framework for creating web applications.
 
No knowledge of HTML or Javascript is needed. Indeed, you can create a simple web page with barely any knowledge of Python!

This is the first in a series of articles in which we will discover how Streamlit can be used to create anything from a simple text-based web page to a sophisticated, interactive dashboard with data visualizations. 

First, we look at how to get started, downloading the tools that we will need (there aren't many) and how to edit and run your first Streamlit app.


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

The [Python](python.org) website always contains the latest version of Python. If you download [Anaconda](anaconda.com), you may not get the latest version. And that is not not a bad thing because you will be sure to get a version that works with all of the libraries that come with it. 

When a new version of Python is released, it can sometimes take a while for the library distributions to catch up, so while installing from __python.org__ will give you the latest version, the Anaconda version may be the safest (although you can, of course, get older versions from __python.org__, too).

So, go to the Anaconda or Python websites and download and install the version for your machine. I would not advise installing both unless you want to confuse your operating system and yourself (it is possible to install both if you exercise some care but there is not much point. If you can't decide which to choose, go for Anaconda, it's what the Streamlit folk recommend).

Whichever you choose, you will still have to install Streamlit.

From a command window (use the Anaconda one if that is what you have installed) run the command:

````
pip install streamlit
````

## Which editor
Almost any editor is suitable for writing Streamlit apps. If you are already a Python programmer then you will already have your favourite, maybe one of the IDEs, VSCode or PyCharm, but a simple general-purpose editor such as __Sublime Text__ or __Notepad++__ is perfectly adequate, too.

When we run normal Python programs we issue the following command:

````
# This won't work with Streamlit
python myprogram.py 	
````


And IDEs such as VSCode and PyCharm assume this when running any Python programs. However, the command we need to run a Streamlit app is:

````
streamlit run myprogram.py
````

The consequence of this is that the standard 'Run' command in VSCode or PyCharm doesn't work. 

The easiest way around this is to issue the correct command in a command window which can be external to the editor, like the Anaconda prompt, or the built-in terminal window in your operating system. Alternatively, we can use a terminal window within the editor or IDE. In VSCode there is a Terminal menu option where you can open a new terminal

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/openVCSterminal.png)

 and in PyCharm, go to the Views menu and find the Terminal option in Tool Windows.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/openPyCharmterminal.png)

So, to run your program from one of these IDEs type the run command into the into the terminal window.

There is no terminal in Sublime Text as standard (although you can install one). Neither is there one in Notepad++ (although can set up a 'run' command that will appear in a menu). But with these simple editors, it might be easier just to use a separate command window.

Here are screenshots of the Sublime Text and Notepad++ editors side-by-side with an Anaconda Powershell prompt.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/sublimetext.png)

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/openPynotepadpp.png)


VSCode and Pycharm are quite sophisticated IDEs. VSCode is a general-purpose tool that can be customized with plugins in order to support many different languages. PyCharm is, if anything, more capable than VSCode but is dedicated to Python programming.

Sublime Text is simple to use, quick to download and install but not free: you can download a free trial version but are expected to pay for a license. Having said that, the trial never expires.

The Notepad++ user interface is, perhaps a little busier than Sublime but it is also a perfectly capable editor and is entirely free.

If you are already a VSCode or PyCharm user then the best bet is to carry on using these but if you don't, then Sublime Text or Notepad++ are probably an easier approach to start with.

There is one more tool that we need to run a Streamlit app and that is a browser such as Chrome, Firefox or Edge. But I assume that you have one of these already.

So, now we have all the tools, we are ready to create our first Streamlit app.

## Editing and running 'Hello Hamlet'

'Hello World' has been the traditional first program that anyone writes in any language for decades - it just displays 'Hello World' on the screen. The first time I came across it was in the book "The C Programming Language" by Briam W. Kernighan and Dennis M. Ritchie whose first edition came out in 1978 (although my copy was the second edition that was published 10 years later).

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

The first line will be familiar to a Python programmer; it imports a Python library - the Streamlit library. As you may well know a Python library is a package of code that contains useful functions that can be incorporated into a Python program. In this case, the Streamlit library incorporates all of the functionality that turns a simple Python program into a web app and provides us with a large number of functions that allows us to build that web app.

The Streamlit library is imported with the name ``st`` so that all of the functions that we use from that library are preceded with that name.

There are two Streamlit functions that we use - ``st.title()`` which formats text in a large bold font and ``st.text()`` which displays preformatted text.

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

Try changing the text and then save it. In you browser you will see that you are ivited to re-run the app.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/ScreenshotHamletChanged.png)

Click on the _Rerun_ button and you will see an updated web page that reflects the changes that you made.

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

st.caption("Hamlet by William shakespeare, Act 3, Scene 1")

st.header("Hamlet's soliloquy")
st.subheader("The famous speech from the 'Nunnery scene'")
st.write("""In the speech, Hamlet considers suicide, but considers that the 
            alternative to his unhappy life might be even worse.""")
````
You can see the result in the screenshot, below.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/hamlet2textscreenshot.png)


![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/hamlet2textscreenshotsmall.png)