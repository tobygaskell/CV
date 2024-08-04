import streamlit as st
import pandas as pd 
def main(): 
    '''
    '''
    data = {'Skill'       : ['Python', 'SQL', 'Snowflake', 'AWS', 'DevOps', 'Hive', 
                             'Natural Language Processing', 'Tableau', 'Alteryx', 
                             'Docker', 'Mongo DB', 'Apache NiFi', 'HTML', 'Spark', 
                             'Machine Learning', 'Big Data', 'Streamlit', 'Pandas', 
                             'Problem-solving', 'Critical thinking', 'Good Communication',  
                             'Confident Presenter', 'Teamwork', 'Decision-making', 
                             'Stress management', 'Leadership'], 

            'Type'        : ['Technical', 'Technical', 'Technical', 'Technical', 'Technical', 'Technical',
                             'Technical', 'Technical', 'Technical',
                             'Technical', 'Technical', 'Technical', 'Technical', 'Technical', 
                             'Technical', 'Technical', 'Technical', 'Technical', 
                             'Soft', 'Soft', 'Soft', 
                             'Soft', 'Soft', 'Soft', 
                             'Soft', 'Soft'], 

            'Competance' : [10,10,10,7,8,5,
                            5, 4, 4, 
                            7, 4, 6, 8, 8, 
                            5, 8, 10, 10, 
                            10, 10, 8, 
                            8, 9, 10, 
                            7, 8] 
                            
                            }
    
    data = pd.DataFrame(data).sort_values('Competance', ascending=False)

    skill_type = st.radio('Pick a skill type', ['All', 'Technical', 'Soft'], label_visibility='collapsed', horizontal=True)

    if skill_type != 'All':
        data = data[data['Type'] == skill_type]

    st.dataframe(data, 
                column_config={
        "Competance": st.column_config.ProgressColumn(
            format="%f",
            min_value=0,
            max_value=10,
        ),
    }, use_container_width=True, hide_index=True, height = len(data) * 35)
    # tech_skills = ['Python', 'SQL', 'Snowflake', 'AWS', 'DevOps', 'Hive', 
    #         'Natural Language Processing', 'Tableau', 'Alteryx', 
    #         'Docker', 'Mongo DB', 'Apache NiFi', 'HTML', 'Spark', 
    #         'Machine Learning', 'Big Data', 'Streamlit', 'Pandas']

    # soft_skills = ['Problem-solving', 'Critical thinking', 'Good Communication',  
    #             'Confident Presenter', 'Teamwork', 'Decision-making', 
    #             'Stress management', 'Leadership']

    # with st.expander('See list of skills', expanded=True):
    #     left, right =  st.columns(2)
    #     with left:
    #         st.write('Technical')
    #         st.write(tech_skills)
    #     with right: 
    #         st.write('Soft')
    #         st.write(soft_skills)