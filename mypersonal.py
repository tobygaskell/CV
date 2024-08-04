import streamlit as st
import utils

def main(): 
    '''
    '''
    cycling, gaming, hiking, rugby, scouts, boardgames = st.columns(6)
    running, football, travelling, movies, tv, tech = st.columns(6)
    path = 'Rugby.png'
    with cycling:
        if st.button('Cycling', use_container_width=True):
            path = 'cycling.png'

    with gaming: 
        if st.button('Gaming', use_container_width=True):
            path = 'Gaming.png'
        
    with hiking:
        if st.button('Hiking', use_container_width=True):
            path = 'Hiking.png'
    
    with rugby: 
        if st.button('Rugby', use_container_width=True):
            path = 'Rugby.png'
        
    with scouts:
        if st.button('Scouts', use_container_width=True):
            path = 'Scouts.png'

    with boardgames:
        if st.button('Board Games', use_container_width=True):
            path = 'Board Games.png'

    with running: 
        if st.button('Running', use_container_width=True):
            path = 'Running.png'
        
    with football:
        if st.button('Football', use_container_width=True):
            path = 'Football.png'
    
    with travelling: 
        if st.button('Travelling', use_container_width=True):
            path = 'Travelling.png'
        
    with movies:
        if st.button('Movies', use_container_width=True):
            path = 'Movies.png'

    with tv: 
        if st.button('TV', use_container_width=True):
            path = 'Tv.png'
        
    with tech:
        if st.button('Technology', use_container_width=True):
            path = 'Technology.png'

    st.markdown('---')

    st.text(' ')
    left, middle, right = st.columns(3)

    with middle:
        st.image('images/{}'.format(path))
    
   