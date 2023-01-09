# Getting Started

First, we'll look at which tools you need and how you can use them; we'll consider 2 types of installation and a couple of simple editors different editors (for experienced Pythonistas, we'll briefly mention VSCode and PyCharm, as well). Then we'll see how to create your first interactive web app in Python

## Installing Python and Streamlit

We need Python installed on our computer and, of course, Streamlit, too. We will also need an editor to create our apps and a browser to run them in.

One of the easiest ways of getting Python is to install the Anaconda distribution. Anaconda consists of a fairly up-to-date version of Python plus a whole bunch of libraries. It's a fairly big installation but by using Anaconda you will save yourself the trouble of having to manually install those libraries later. The main alternative is to install the official Python distribution from their website.

The [Python](python.org) website always contains the latest version of Python. If you download [Anaconda](anaconda.com), you may not get the latest version. But that is not necessarily a bad thing because, while it might not be the most up-to-date, you will be sure to get a version that works with all of the libraries that come with it. 

When a new version of Python is released, it can sometimes take a while for the library distributions to catch up, so while installing from [python.org](python.org) will give you the latest version, the [Anaconda](anaconda.com) version may be safer (although you can, of course, get the same older versions from [python.org](python.org), too).

So, go to the Anaconda or Python websites and download and install the version for your machine. I would not advise installing both unless you want to confuse your operating system and yourself (it _is_ possible to install both if you exercise some care but there really is not much point. If you can't decide which to choose, then maybe go for Anaconda - it's what the Streamlit folk recommend).

Whichever you choose, you will still have to install Streamlit.

From a command window (use the Anaconda one if that is what you have installed) run the command:

```` bash
pip install streamlit
````
Now you are ready to start programming.
