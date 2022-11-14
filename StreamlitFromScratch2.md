# Streamlit from Scratch: Embedding images, video and audio into a Streamlit app

## Streamlit was designed to help data scientists but it not just aboutr data, the addition of media helps to communicate your ideas

![](https://www.nasa.gov/sites/default/files/styles/ubernode_alt_horiz/public/images/464487main_AS11-40-5886_full.jpg)

_Public domain image, courtesy of NASA_

In the first part of this series, _Getting Started_, we saw how to set up the Streamlit development environment and how easy it is to create a simple web app using different types of text.

This time we will look at how we can enhance our app with different media - images, video and sound - as well as learning a little bit about how to layout a Streamlit app.

We'll create two different apps, the first one carries on with our Shakespeare theme from the first part and will look like this:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/shakespearemediaapp.png)

The second moves us forward a few centuries to the moon landing of 1969 and looks like this:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/eagleapp.png)


Last time we left Hamlet, Shakespeare's tragic hero, contemplating whether or not to end his life in his famous soliloquy. We are going to expand that app with some additional material - an image, a video and an audio track - and lay it out in two columns. The result will be similar to the image above.

Incorporating these media into a Streamlit app is a straightforward task. Streamlit provides the functions ``st.image()`` to include graphics, ``st.video()`` for videos, including Youtube videos, and ``st.audio()`` for audio and they all support media in various formats.

The image is from Wikimedia and is a flyer for the play Hamlet.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/hamletflyer.png)

_Unknown source, Public domain, via Wikimedia Commons_

You include it in your Streamlit app like this:
```` Python
    st.image('https://upload.wikimedia.org/wikipedia/commons/d/df/Hamlet.jpg', 
        use_column_width=True,
        caption = "Unknown source, Public domain, via Wikimedia Commons")
````

The video is a comical sketch with a number of well-known actors who try and tell each other how the famous 'To be, or not to be...' lines should be spoken. They are then, unexpectedly, upstaged by Prince Charles.

![](https://youtu.be/sw_zDsAeqrI)

_Video courtesy of the PBS and Youtube._

```` Python
    st.video('https://youtu.be/sw_zDsAeqrI')
````

(If you are in the UK and have access to the BBC iPlayer, seek out the original and longer version of this - it's highly entertaining.)

Lastly, the audio is a musical piece by Tchaikovsky inspired by the play Hamlet

https://upload.wikimedia.org/wikipedia/commons/3/3b/Tchaikovsky-Hamlet_Op67_vs_Kosma-FeuillesMortes.ogg

_Extracted from Pyotr Ilyich Tchaikovsky's 'Hamlet Op. 67' Overture, composed in 1888. Public Domain via Wikimedia_

```` Python
st.audio("https://upload.wikimedia.org/wikipedia/commons/3/3b/Tchaikovsky-Hamlet_Op67_vs_Kosma-FeuillesMortes.ogg")
````


--- 

Thanks for reading - I hope you have found it useful. You can find a link to the code for this article on my [Github page](alanjones2.github.io) as well as links to other articles.

To keep up to date with what I am doing, you can subscribe to my occasional free newsletter [Technofile](technofile.substack.com)


### References

The various Streamlit API references used in the article can be found below.

[st.image](https://docs.streamlit.io/library/api-reference/media/st.image)

[st.audio](https://docs.streamlit.io/library/api-reference/media/st.audio)

[st.video](https://docs.streamlit.io/library/api-reference/media/st.video)

[st.markdown](https://docs.streamlit.io/library/api-reference/media/st.markdown)

[st.columns](https://docs.streamlit.io/library/api-reference/layout/st.columns)