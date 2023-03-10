import streamlit as st 

st.title("Hi I'm Toby Gaskell 👋")

st.write('📧 - Toby96@sky.com')
st.write('📞 - 07908 016 447')
st.write('🏠 - London')

st.markdown('---')

st.subheader('Profile 👨')

st.info('''I am confident, dependable and motivated - as well as eager to 
be in an environment where I am able to learn from others and contribute 
ideas. 

I specialise in ensuring engineering is completed efficiently to a 
high quality following industry standards. I pride myself on my collaboration 
skills including the ability to communicate effectively and understand 
requirements from both technical and non technical stakeholders. 

I relish the idea of working across a wide range of tools and technologies - 
as I have a thirst for all knowledge, especially widening my technical abilities. 

I am a competent programmer primarily in python with experience using other 
languages such as Java and R. I am driven, hardworking and excited by data.''')

st.markdown('---')

st.subheader('Experience ⌨️')

company_choice = st.selectbox('Role', ['Security Data Engineer (Schroders)', 'Trainee (Kubrick)', 'Bike Mechanic (Never Mind the Bike Shops)' ])

if company_choice == 'Security Data Engineer (Schroders)': 

    project_choice = st.radio('Project', ['Risk Metrics', 'Cloud Migration', 'Cloud Data Quality Monitoring', 'ML Phishing Prediction Model', 'Data Insights'], label_visibility = 'collapsed')

    if project_choice == 'Risk Metrics':
        st.info('''Lead engineer on building two end to end security metrics solutions. 
One mapping on to the industry leading MITRE ATT&CK framework and the other 
used to monitor the companies risk position. 

This work included designing and building the back ends which consists
of two normalised databases, two full python engines used to automatically 
run and update risk metrics using data from a vast number of different data 
sources held in snowflake.

As well as working with the business stakeholders to design, build and implement 
an interactive front end and work flow - which is used across multiple teams to 
input risk values and commentary.

This automated solution has reduced the BAU work for our team dramtically
as well as driving forward the quality of risk insights we generate.''') 

    if project_choice == 'Cloud Migration':
        st.info('''Part of the team responsible for pioneering the migration of the security 
data strategy from the on prem solution to the cloud. Which was the first of 
it's kind within Schroders.

I engineered a vast number of large machine generated security data sources 
which can ingest multiple billion rows a day. 

I had to consider solutions to batched, micro batched as well as streamed data 
sets from a variety of different sources - as well as complex unstructured data
sets which required custom solutions.

As part of the cloud solution we intergrated and became familiar with a number 
of different cloud platforms - including Snowflake, AWS, Streamlit, Azure and 
Team City.''') 

    if project_choice == 'Cloud Data Quality Monitoring':
        st.info('''Lead Engineer on building from the ground up a data quality monitoring solution 
for our cloud data. 

This work consisted of building a scalable solution which implemented a number of 
checks across our data - including volume and quality monitoring - then alerting 
the team via a messaging process when things went wrong. 

Figuring out how to dynamically identify what consisted a "normal" volume 
ingestion for each unique dataset was something i am especially proud of. 
''') 

    if project_choice == 'ML Phishing Prediction Model':
        st.info('''Built and deployed a predictive model which used a regression machine learning 
algorithm, to identify the likelihood of a reported emails being a phishing 
email. 

This used a number of different natural language processes and built features to 
get results showing accuracy and precision scores of 97% and 98% respectively.

Once deployed this was used to prioritise security incidents based on our 
prediction - saving our SOC over 4 hours a week''')

    if project_choice == 'Data Insights':
        st.info('''Generating data dashboards for use across the wider team is bread and butter 
in this role. During my time I have lost count at the number I have built. 

Some of the most useful however have included dashboards generating insights
for our SOC showing length of time taken to handle a security incident showing
areas needed for improvement and Security tool coverage dashboards used by 
multiple teams operationally to ensure we have adequate estate coverage. ''')

    st.markdown('###### Period in Role - 3 Years (2020-2023)')

if company_choice == 'Trainee (Kubrick)': 
    
    st.info('''Trained for 4 months where I was taught and assessed on technologies such as 
SQL, Python, ML, Tableau and Big Data. 

This programme gave me the skills and technical understanding needed to quickly 
become an excellent data engineer.''')
    st.markdown('###### Period in Role- 4 Months (2020)')

if company_choice == 'Bike Mechanic (Never Mind the Bike Shops)': 


    st.info('''Self taught bike mechanic responsible for mending bikes as well
as engaging with customers and suppliers.

Created and maintained a system for stock control of more than 4,000 products, 
improving efficiency of the online retail business.

After which I went traveling around the USA before returning to start work 
in london.''')
    st.markdown('###### Period in Role- 18 Months (2018-2019)')

st.markdown('---')

st.subheader('Education 🎓') 

level_choice = st.radio('Pick a Level', ['Degree', 'A-Level', 'GSCE'], label_visibility = 'collapsed')

if level_choice == 'Degree': 
    location = 'University of York'
    period = '3 Years 2015-2018'
    results = {'Mathematics (BSc)': '2:1', 
               'Dissertation (3rd Year Module)': '2:1', 
               'Cryptography (3rd Year Module)': '1st', 
               'Group Theory (2nd Year Module)': '1st'}
    bio = '''During my degree I specialised in pure Mathematics - studying cryptography in 3rd 
year and writing my dissertation on Knot Theory were two of my personal highlights.'''

elif level_choice == 'A-Level': 
    location = 'Xaverian College'
    period = '2 Years 2013-2015'
    results = {'Mathematics': 'A*', 
               'Economics': 'A', 
               'PE':'B', 
               'Biology (AS Level)':'B'}
    bio = '''Whilst studying economics at A-Level I was a member of a small team of students 
who were regional winners of the bank of England challenge.'''

elif level_choice == 'GSCE':     
    location = 'Longdendale CLC'
    period = '5 Years 2008-2015'
    results = {'Mathematics': 'A*', 
               'English': 'A', 
               'Physics':'A', 
               'Biology':'A'}
    bio = None

st.markdown('##### Institution - {}'.format(location))
st.markdown('###### Period - {}'.format(period))
for subject, result in results.items(): 
    left, right = st.columns(2)
    with left: 
        st.write(subject)
    with right: 
        st.write(result)
if bio: 
    st.info(bio)



st.markdown('---')

st.subheader('Skills 👏')

tech_skills = ['Python', 'SQL', 'Snowflake', 'AWS', 'DevOps', 'Hive', 
          'Natural Language Processing', 'Tableau', 'Alteryx', 
          'Docker', 'Mongo DB', 'Apache NiFi', 'HTML', 'Spark', 
          'Machine Learning', 'Big Data', 'Streamlit', 'Pandas']

soft_skills = ['Problem-solving', 'Critical thinking', 'Good Communication',  
               'Confident Presenter', 'Teamwork', 'Decision-making', 
               'Stress management', 'Leadership']

with st.expander('See list of skills'):
    left, right =  st.columns(2)
    with left:
        st.write('Technical')
        tech_skills
    with right: 
        st.write('Soft')
        
st.markdown('---')

st.subheader('Personal 🏈')

st.info('''In 2014 I was the youngest player in Nat 2 at the age of 17. 

I also played at academy level for Leicester Tigers and represented numerous 
club and county sides including my university 1st team and Cheshire (Captain).
''')

st.markdown('---')

with open('toby_cv_20220515.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read() 

st.download_button('Keep My Info', data = PDFbyte, file_name = 'TobyGaskellCV.pdf')


