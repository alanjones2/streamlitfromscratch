import streamlit as st

st.markdown("## Some red and blue text")

st.markdown("#### Using Streamlit coloring:")
st.markdown("""This text is :red[colored red], 
            and this is **:blue[colored blue]** and bold.""")
st.markdown("""This text is :red[colored red], 
               and this is :blue[colored blue] and not bold.""")

st.markdown("#### Using HTML/CSS coloring:")
st.markdown("""This text is <span style='color:red'>colored red</span>, 
               and this is <b><span style='color:blue'>colored blue</span></b> and bold.""", 
               unsafe_allow_html=True)
st.markdown("""This text is <span style='color:red'>colored red</span>, 
               and this is <span style='color:blue'>colored blue</span> and not bold.""", 
               unsafe_allow_html=True)

st.markdown("## Comparing colors:")
# blue, green, orange, red, violet

st.markdown("""**This text is :blue[blue], 
                            :green[green], 
                            :orange[orange], 
                            :red[red], 
                            :violet[violet] 
                            using Streamlit colors.**""")

st.markdown("""**This text is <span style='color:blue'>blue</span>, 
                            <span style='color:green'>green</span>, 
                            <span style='color:orange'>orange</span>, 
                            <span style='color:red'>red</span>, 
                            <span style='color:violet'>violet</span> using HTML/CSS colors.**""", 
                            unsafe_allow_html=True)


st.markdown("## Some pink and purple text")

st.markdown("#### Using Streamlit coloring:")
st.markdown("This text is :pink[colored pink], and this is **:violet[purple-colored]** and bold.")

st.markdown("#### Using HTML/CSS coloring:")
st.markdown("This text is <span style='color:pink'>colored pink</span>, and this is **<span style='color:violet'>purple-colored</span>** and bold.", unsafe_allow_html=True)

st.markdown("---")

st.markdown("By the way, did you know you can include icons in markdown :astonished:.")
