## Streamlit from Scratch 2: Embedding images, video and audio into a Streamlit app

In the first part of this series we saw how to set up the Streamlit development environment and how easy it is to create a simple web app using different types of text.

This time we will look at how we can enhance our app with different media - images, video and sound - as well as learning a little bit about how to layout a Streamlit app.

Last time we left Hamlet, Shakespeare's tragic hero, contemplating whether or not to end his life in his famous soliloquy. We are going to expand that app with some additional material - an image, a video and an audio track - and lay it out in two columns. The result will be similar to the image above.

Incorporating these media into a Streamlit app is a straightforward task. Streamlit provides the functions ``st.image()`` to include graphics, ``st.video()`` for videos, including Youtube videos, and ``st.audio()`` for audio and they all support media in various formats.

The image is from Wikimedia and is a flyer for the play Hamlet.

![](https://upload.wikimedia.org/wikipedia/commons/d/df/Hamlet.jpg)

The video is a 




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