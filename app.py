import streamlit as st 
import myeducation
import myprofile
import myexperiance
import myskills
import mypersonal


st.set_page_config(layout='wide')

st.sidebar.title("Toby Gaskell")

with open('toby_cv_20230313.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read() 

age, phone       = st.sidebar.columns(2)
location, linked  = st.sidebar.columns(2)
email, download = st.sidebar.columns(2)

@st.experimental_dialog(' ')
def details_popup(type): 
    '''
    '''
    age_col = 'grey'
    email_col = 'grey'
    address_col = 'grey'
    linked_col = 'grey'
    phone_col = 'grey'
    age_size = '0.6'
    email_size = '0.6'
    address_size = '0.6'
    linked_size = '0.6'
    phone_size = '0.6'

    if type == 'Age':
        age_col = 'orange'
        age_size = '1'
    if type == 'Email': 
        email_col = 'orange'
        email_size = '1'
    if type == 'Phone':
        phone_col = 'orange'
        phone_size = '1'
    if type == 'Linked In':
        linked_col = 'orange'
        linked_size = '1'
    if type == 'Address':
        address_col = 'orange'
        address_size = '1'

    st.markdown('''
<h1 style= "text-align:center;color:{};opacity:0.8;"> Toby Gaskell (27)</h1>  
                
<div  style="text-align:center;"> <span style="color:{};opacity:{};"> 07908 016 447</span></div>    
<div  style="text-align:center;"> <span style="color:{};opacity:{};"> Maida Vale, London, UK </span>  </div>
<div  style="text-align:center;"> <a href="https://www.linkedin.com/in/toby-gaskell-515491184/" style="color: {};opacity:{};"> Linked In </a>  </div>
<div  style="text-align:center;"> <p style="color:{};opacity:{}; "> Toby96@sky.com </p> </div>

                '''.format(age_col,
                           phone_col, phone_size,
                           address_col, address_size,
                           linked_col, linked_size,
                           email_col, email_size
                           ), unsafe_allow_html=True)
with age: 
    if st.button('👨🏻‍🦳', use_container_width = True):
        details_popup('Age')

with email:
    if st.button('📧', use_container_width = True):
        details_popup('Email') 

with phone:
    if st.button('📞', use_container_width = True):
        details_popup('Phone') 

with linked:
    if st.button('🔗', use_container_width = True):
        details_popup('Linked In') 

with location:
    if st.button('🏠', use_container_width = True):
        details_popup('Address') 

with download:
    st.download_button('📩', data = PDFbyte, file_name = 'TobyGaskellCV.pdf', use_container_width=True)
    # st.caption('Download CV')


# profile, experiance, education, skills, personal = st.tabs(['👨 - Profile', 
#                                                             '⌨️ - Experience', 
#                                                             '🎓 - Education', 
#                                                             '👏 - Skills', 
#                                                             '🏈 - Personal'])

st.sidebar.markdown('---')

section_choice = st.sidebar.radio('Pick a Section', ['👨 - Profile', 
                                                     '⌨️ - Experience', 
                                                     '🎓 - Education', 
                                                    #  '👏 - Skills', 
                                                     '🏈 - Personal'], 
                                                     label_visibility='collapsed')


# with profile:
if section_choice == '👨 - Profile':
    myprofile.main() 
    
# with experiance:
if section_choice == '⌨️ - Experience':
    myexperiance.main()
    
# with education:
if section_choice == '🎓 - Education':
    myeducation.main()

# with skills:
# if section_choice == '👏 - Skills':
#     myskills.main()
            
# with personal:
if section_choice == '🏈 - Personal':
    mypersonal.main()