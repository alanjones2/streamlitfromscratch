import streamlit as st
import pandas as pd

st.title("Hamlet's soliloquy")
st.header("The famous speech from the 'Nunnery scene'")
st.write("""In the speech, Hamlet considers suicide, but considers that the 
            alternative to his unhappy life might be even worse.""")


#col1, col2 =  st.columns([3,2])
st.text("""
"To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them."
""")
st.caption("Hamlet by William shakespeare, Act 3, Scene 1")

st.video('https://youtu.be/sw_zDsAeqrI')
st.caption("""Video courtesy of the RSC and Youtube. 
                If you are in the UK and have access to the BBC iPlayer,
                seek out the original and longer version of this - it's very funny.""")

st.write("""In the video above several famous actors jokingly discuss
         how the famous lines should be spoken, only to 
         be upstaged by Prince Charles who they seem to agree, 
         gets it right.""")