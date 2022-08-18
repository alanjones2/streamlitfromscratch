## Streamlit from Scratch 2: Embedding images, video and audio into a Streamlit app

### Media form the Apollo 11 Moon landing as a Streamlit app

![]()

In the first part of this series we saw how to set up the Streamlit development environment and how easy it is to create a simple web app using different types of text.

This time we will look at how we can enhance our app with different media - images, video and sound.

On the morning of July 16, 1969, Apollo 11 astronauts Neil Armstrong, Buzz Aldrin and Michael Collins were about to be launched into space from the Kennedy Space Center. Their mission was to lead to one of the most famous events in history: the first Moon landing.

Here we are going to see how various media files from that mission can be incorporated into a Streamlit app.

Streamlit provides the functions ``st.image()`` to include graphics, ``st.video()`` for videos, including local or Youtube videos, and ``st.audio()`` for audio and they all support media in various formats.

_All the media we see here is in the public domain and courtesy of NASA_

The image we will use shows Apollo 11 Commander Neil Armstrong working at an equipment storage area on the lunar module during the moonwalk.

![](https://www.nasa.gov/sites/default/files/styles/ubernode_alt_horiz/public/images/464487main_AS11-40-5886_full.jpg)



You include it in your Streamlit app like this:
```` Python
    st.image('https://www.nasa.gov/sites/default/files/styles/ubernode_alt_horiz/public/images/464487main_AS11-40-5886_full.jpg',
        caption = "Public domain image, courtesy of NASA")

````

The video is of the Moon walks and is poor quality by today's standards but it _was_ originally taken in 1969!

![](https://youtu.be/sw_zDsAeqrI)

_Footage from the Apollo 11 moonwalk that was partially restored in 2009_

```` Python
    st.video('https://youtu.be/hxPbnFc7iU8')
````

Lastly, the audio is the famous "The Eagle has landed" message from Armstrong to the Houston mission base.

https://soundcloud.com/nasa/apollo-11-eagle-has-landed-1?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

_The track here is from NASA's Soundcloud channel._

The source file is shown in the ``st.audio()`` statement below.

```` Python
st.audio("https://www.nasa.gov/mp3/569462main_eagle_has_landed.mp3")
````

The entire code is only half a dozen lines and produces the app shown above.

Full code:

```` Python
import streamlit as st

st.title('The Eagle has Landed')
st.header('Media from the Apollo 11 Moon landing')

st.image('https://www.nasa.gov/sites/default/files/styles/ubernode_alt_horiz/public/images/464487main_AS11-40-5886_full.jpg')
st.video('https://youtu.be/hxPbnFc7iU8')
st.audio("https://www.nasa.gov/mp3/569462main_eagle_has_landed.mp3")
````

In the next article we will explore various ways of representing data in a Streamlit app, from data tables to visualisations using charts.

--- 

Thanks for reading - I hope you have found it useful. You can find a link to the code for this article on my [Github page](alanjones2.github.io) as well as links to other articles.

To keep up to date with what I am doing, you can subscribe to my occasional free newsletter [Technofile](technofile.substack.com)


### References

The various Streamlit API references used in the article can be found below.

[st.image](https://docs.streamlit.io/library/api-reference/media/st.image)

[st.audio](https://docs.streamlit.io/library/api-reference/media/st.audio)

[st.video](https://docs.streamlit.io/library/api-reference/media/st.video)
