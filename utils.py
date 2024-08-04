import streamlit as st

def color_text(text, primary = 'grey', secondary= 'orange'):
    '''
    '''
    text = '<span style="color:{};opacity:0.6;">'.format(primary) + text + '</span>'

    text = text.replace('!-!', '</span><span style="color:{};opacity:1;">'.format(secondary))
    text = text.replace('|-|', '</span><span style="color:{};opacity:0.6;">'.format(primary))

    st.markdown(text, unsafe_allow_html=True)

