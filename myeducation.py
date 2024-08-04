import streamlit as st
import utils 



def main(): 
    if 'level_choice' not in st.session_state:
        st.session_state['level_choice'] = 'Uni'
    # st.caption('Pick a Level...')

    degree, alevel, gcse, infant, nursery = st.columns(5)

    with degree:
        if st.button('Degree', use_container_width=True, type = 'primary' if st.session_state['level_choice'] == 'Uni' else 'secondary'):
            st.session_state['level_choice'] = 'Uni'
            st.rerun()
    with alevel:
        if st.button('A Level', use_container_width=True, type = 'primary' if st.session_state['level_choice'] == 'College' else 'secondary'):
            st.session_state['level_choice'] = 'College'
            st.rerun()

    with gcse:
        if st.button('GCSE', use_container_width=True, type = 'primary' if st.session_state['level_choice'] == 'High School' else 'secondary'):
            st.session_state['level_choice'] = 'High School'
            st.rerun()

    with infant:
        if st.button('Infant', use_container_width=True, type = 'primary' if st.session_state['level_choice'] == 'Infant School' else 'secondary'):
            st.session_state['level_choice'] = 'Infant School'   
            st.rerun()        

    with nursery:
        if st.button('Nursery', use_container_width=True, type = 'primary' if st.session_state['level_choice'] == 'Nursery' else 'secondary'):
            st.session_state['level_choice'] = 'Nursery'    
            st.rerun()   
            

    st.markdown('---')


    if st.session_state['level_choice'] == 'Uni':
        location = 'University of York'
        period = '3 Years 2015-2018'
        results = {'Course' : ['Mathematics', 'Dissertation', 'Cryptography', 'Group Theory'],
                'Level'  : ['BSc', '3rd Year Module', '3rd Year Module', '2nd Year Module'],
                'Result' : ['2:1', '2:1', '1st','1st'], 
                'Enjoyment' :[[1,2,3,4,0], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]}
        
        bio = '''During my !-!degree|-| I specialised in pure Mathematics - studying !-!cryptography|-| in 3rd 
    year and writing my dissertation on !-!Knot Theory|-| were two of my personal highlights.'''
        display_info(location, period, results, bio)


    if st.session_state['level_choice'] == 'College':
        location = 'Xaverian College'
        period = '2 Years 2013-2015'
        results = {'Course' : ['Mathematics', 'Economics', 'PE', 'Biology'],
                'Level'  : ['A Level', 'A Level', 'A Level', 'AS Level'], 
                'Result' : ['A*', 'A', 'B','B'], 
                'Enjoyment' :[[1,2,3,4,5], [1,2,3,4,0], [1,2,3,4,5], [1,2,3,0,0]]}
        
        bio = '''Whilst studying !-!economics|-| at A-Level I was a member of a small team of students 
    who were regional !-!winners|-| of the bank of England challenge.'''
        display_info(location, period, results, bio)

    if st.session_state['level_choice'] == 'High School':
        location = 'Longdendale Community Language College'
        period = '5 Years 2008-2015'
        results = {'Course' : ['Mathematics', 'English', 'Physics', 'Biology'],
                'Level'  : ['GCSE', 'GCSE', 'GCSE', 'GCSE'],
                'Result' : ['A*', 'A', 'A','A'], 
                'Enjoyment' :[[1,2,3,4,5], [1,2,0,0,0], [1,2,3,0,0], [1,2,3,4,0]]}
        
        bio = None
        display_info(location, period, results, bio)

    # with infant:    
    if st.session_state['level_choice'] == 'Infant School':
        location = 'Stalyhill & Crawley Ridge'
        period = '6 Years 2002-2008'
        results = {'Course' : ['Mathematics', 'English', 'Science', 'PE'],
                'Level'  : ['SATs', 'SATs', 'SATs', 'N/A'],
                'Result' : ['5', '4', '5', 'Best in the Year'], 
                'Enjoyment' :[[1,2,3,4,5], [1,2,0,0,0], [1,2,3,4,0], [1,2,3,4,5]]}
        
        bio = None
        display_info(location, period, results, bio)
    
    # with nursery:
    if st.session_state['level_choice'] == 'Nursery':
        location = 'Crawley Ridge'
        period = '6 Years 2002-2008'
        results = {'Course' : ['Napping', 'Playing', 'Cut & Paste', 'Running Really Fast'],
                'Level'  : ['Pro', 'Pro', 'Intermediate', 'Beginner'],
                'Result' : ['5/5', '5/5', '5/5', '5/5'], 
                'Enjoyment' :[[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]}
        
        bio = None
        display_info(location, period, results, bio)


def display_info(location, period, results, bio):
    '''
    '''
    st.markdown('##### {}'.format(location))

    if bio: 
        with st.container(border = True):
            utils.color_text(bio, 'grey', 'orange')

    st.dataframe(results, use_container_width=True,     column_config={
        "Enjoyment": st.column_config.BarChartColumn(
            y_min=0,
            y_max=5,
        ),
    })