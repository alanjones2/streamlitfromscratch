import streamlit as st
import pandas as pd


st.title('The Tragical Historie of Hamlet')
st.image('https://upload.wikimedia.org/wikipedia/commons/d/df/Hamlet.jpg', width=500,
          caption = "Unknown source, Public domain, via Wikimedia Commons")

st.header("Hamlet's soliloquy")
st.write("""In his speech, Hamlet considers suicide, but considers that the 
            alternative to his unhappy life might be even worse.""")

col1, col2 =  st.columns([3,2])
with col1: 
    st.text("""
    "To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune,
    Or to take arms against a sea of troubles
    And by opposing end them."
    """)
    st.caption("Hamlet by William shakespeare, Act 3, Scene 1")

with col2:
    st.video('https://youtu.be/sw_zDsAeqrI')

st.caption("""Video courtesy of the RSC and Youtube. 
              If you are in the UK and have access to the BBC iPlayer,
              seek out the original and longer version of this - it's very amusing.""")

st.write("""In the video above several famous actors jokingly discuss
         how the famous lines should be spoken, only to 
         be upstaged by Prince Charles who they seem to agree, 
         gets it right.""")

st.audio('https://upload.wikimedia.org/wikipedia/commons/3/3b/Tchaikovsky-Hamlet_Op67_vs_Kosma-FeuillesMortes.ogg')

st.caption("Extracted from Pyotr Ilyich Tchaikovsky's 'Hamlet Op. 67' Overture, composed in 1888. Public Domain via Wikimedia")