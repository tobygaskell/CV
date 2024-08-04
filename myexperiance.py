import streamlit as st
import utils


def main():
    '''
    '''
    # company_choice = st.selectbox('Role', ['Security Data Engineer (Schroders)', 'Trainee (Kubrick)', 'Bike Mechanic (Never Mind the Bike Shops)' ])
    st.caption('Company')
    schroders, kubrick, nmtbs = st.columns(3)

    if 'company_choice' not in st.session_state:
        st.session_state['company_choice'] = 'Schroders'

    if 'role_choice' not in st.session_state:
        st.session_state['role_choice'] = 'Sec DE'

    if 'project_choice' not in st.session_state:
        st.session_state['project_choice'] = 'Risk Metrics'

    with schroders:
        if st.button('Schroders', use_container_width=True, type = 'primary' if st.session_state['company_choice'] == 'Schroders' else 'secondary'):
            st.session_state['company_choice'] = 'Schroders'
            st.rerun()
    with kubrick:
        if st.button('Kubrick', use_container_width=True, type = 'primary' if st.session_state['company_choice'] == 'Kubrick' else 'secondary'):
            st.session_state['company_choice']  = 'Kubrick'
            st.rerun()
    with nmtbs:
        if st.button('Never Mind the Bike Shop', use_container_width=True, type = 'primary' if st.session_state['company_choice'] == 'nmtbs' else 'secondary'):
            st.session_state['company_choice']  = 'nmtbs'
            st.rerun()
    
    # st.markdown('---')

    if st.session_state['company_choice']:
        if st.session_state['company_choice']  == 'Schroders': 
            st.caption('Job Role')
            left, right = st.columns(2)
            # st.session_state['role_choice'] = 'Sec DE'

            with left: 
                if st.button('Security Data Engineer', use_container_width=True, type = 'primary' if st.session_state['role_choice'] == 'Sec DE' else 'secondary'):
                    st.session_state['role_choice']  = 'Sec DE'
                    st.rerun()
                
            
            with right: 
                if st.button('Platform Data Engineer', use_container_width=True, type = 'primary' if st.session_state['role_choice'] == 'Plat DE' else 'secondary'):
                    st.session_state['role_choice']  = 'Plat DE'
                    st.rerun()

            st.caption('Project')
            if st.session_state['role_choice']  == 'Sec DE':
                far_left, right, far_right = st.columns(3)
                # st.session_state['project_choice'] = 'Risk Metrics'
                with far_left:
                    if st.button('Risk Metrics', use_container_width=True, type = 'primary' if st.session_state['project_choice'] == 'Risk Metrics' else 'secondary'):
                        st.session_state['project_choice'] = 'Risk Metrics'
                        st.rerun()
                with right:
                    if st.button('ML Phishing prediction Model', use_container_width=True, type = 'primary' if st.session_state['project_choice'] == 'ML Phishing Prediction Model' else 'secondary'):
                        st.session_state['project_choice'] = 'ML Phishing Prediction Model'
                        st.rerun()
                with far_right:
                    if st.button('Data Insights', use_container_width=True, type = 'primary' if st.session_state['project_choice'] == 'Data Insights' else 'secondary'):
                        st.session_state['project_choice'] = 'Data Insights'
                        st.rerun()

            if st.session_state['role_choice']  == 'Plat DE':
                left, middle = st.columns(2)

                # st.session_state['project_choice'] = 'Cloud Migration'


                with left:
                    if st.button('Cloud Migration', use_container_width=True, type = 'primary' if st.session_state['project_choice'] == 'Cloud Migration' else 'secondary'):
                        st.session_state['project_choice'] = 'Cloud Migration'
                        st.rerun()
                with middle:
                    if st.button('Cloud Data Quality Monitoring', use_container_width=True, type = 'primary' if st.session_state['project_choice'] == 'Cloud Data Quality Monitoring' else 'secondary'):
                        st.session_state['project_choice'] = 'Cloud Data Quality Monitoring'
                        st.rerun()


            # project_choice = st.radio('Project', ['Risk Metrics', 
            #                                       'Cloud Migration', 
            #                                       'Cloud Data Quality Monitoring', 
            #                                       'ML Phishing Prediction Model', 
            #                                       'Data Insights'], label_visibility = 'collapsed', horizontal=True)

            if st.session_state['project_choice'] == 'Risk Metrics':
                with st.container(border = True):
                    utils.color_text('''!-!Lead engineer|-| on building two end to end security metrics solutions. 
        One mapping on to the industry leading !-!MITRE ATT&CK|-| framework and the other 
        used to monitor the companies !-!risk|-| position. This work included designing and building the back ends which consists
        of two normalised databases, two full python engines used to !-!automatically|-| 
        run and update risk metrics using data from a vast number of different data 
        sources held in !-!snowflake|-|. As well as working with the business stakeholders to design, build and implement 
        an interactive !-!front end|-| and work flow - which is used across multiple teams to 
        input risk values and commentary. This automated solution has reduced the BAU work for our team dramtically|-|
        as well as driving forward the !-!quality of risk|-| insights we generate.''') 

            if st.session_state['project_choice'] == 'Cloud Migration':
                with st.container(border = True):
                    utils.color_text('''Part of the team responsible for pioneering the migration of the security 
        data strategy from the on prem solution to the cloud. Which was the first of 
        it's kind within Schroders. I engineered a vast number of large machine generated security data sources 
        which can ingest multiple billion rows a day. I had to consider solutions to batched, micro batched as well as streamed data 
        sets from a variety of different sources - as well as complex unstructured data
        sets which required custom solutions. As part of the cloud solution we intergrated and became familiar with a number 
        of different cloud platforms - including Snowflake, AWS, Streamlit, Azure and 
        Team City.''') 

            if st.session_state['project_choice'] == 'Cloud Data Quality Monitoring':
                with st.container(border = True):
                    utils.color_text('''Lead Engineer on building from the ground up a data quality monitoring solution 
        for our cloud data. 
        This work consisted of building a scalable solution which implemented a number of 
        checks across our data - including volume and quality monitoring - then alerting 
        the team via a messaging process when things went wrong. 
        Figuring out how to dynamically identify what consisted a "normal" volume 
        ingestion for each unique dataset was something i am especially proud of. 
        ''') 

            if st.session_state['project_choice'] == 'ML Phishing Prediction Model':
                with st.container(border = True):
                    utils.color_text('''Built and deployed a predictive model which used a regression machine learning 
        algorithm, to identify the likelihood of a reported emails being a phishing 
        email. This used a number of different natural language processes and built features to 
        get results showing accuracy and precision scores of 97% and 98% respectively. Once deployed this was used 
        to prioritise security incidents based on our prediction - saving our SOC over 4 hours a week''')

            if st.session_state['project_choice'] == 'Data Insights':
                with st.container(border = True):
                    utils.color_text('''Generating data dashboards for use across the wider team is bread and butter 
        in this role. During my time I have lost count at the number I have built. Some of the most useful 
        however have included dashboards generating insights for our SOC showing length of time taken to 
        handle a security incident showing areas needed for improvement and Security tool coverage 
        dashboards used by multiple teams operationally to ensure we have adequate estate coverage. ''')

            st.markdown('###### Period in Role - 3 Years (2020-2023)')

        if st.session_state['company_choice']  == 'Kubrick': 
            st.caption('Job Role')
            st.button('Trainee Data Engineer', use_container_width=True, type = 'primary')
            st.caption('Project')
            st.button('Training', use_container_width=True, type = 'primary')
            with st.container(border = True):
                utils.color_text('''Trained for 4 months where I was taught and assessed on technologies such as 
                            SQL, Python, ML, Tableau and Big Data. This programme gave me the skills and technical 
                         understanding needed to quickly become an excellent data engineer.''')
            
            st.markdown('###### Period in Role- 4 Months (2020)')

        if st.session_state['company_choice']  == 'nmtbs': 
            st.caption('Job Role')
            left, right = st.columns(2)
            with left:
                if st.button('Bike Mechanic', use_container_width=True, type = 'primary' if st.session_state['role_choice'] == 'bike_mechanic' else 'secondary'):
                    st.session_state['role_choice'] = 'bike_mechanic'
                    st.rerun()
            with right:
                if st.button('Online Sales Manager', use_container_width=True, type = 'primary' if st.session_state['role_choice'] == 'ebay' else 'secondary'):
                    st.session_state['role_choice'] = 'ebay'
                    st.rerun()

            if st.session_state['role_choice'] == 'bike_mechanic':
                st.caption('Project')
                st.button('Fix Bikes', use_container_width=True, type = 'primary')
                with st.container(border = True):
                    utils.color_text('''Self taught bike mechanic responsible for mending bikes as well
            as engaging with customers and suppliers.''')
            if st.session_state['role_choice'] == 'ebay':
                st.caption('Project')
                st.button('Manage Online Store', use_container_width=True, type = 'primary')
                with st.container(border=True):
                    utils.color_text('''!-!Created|-| and !-!maintained|-| a system for stock control of more than !-!4,000|-| products, improving !-!efficiency|-| of the online retail business.''')

                
            st.markdown('###### Period in Role- 18 Months (2018-2019)')

    else:
        st.write('⬆️ Please pick a company to view ⬆️')
