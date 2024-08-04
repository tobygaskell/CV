import streamlit as st
import myskills
import mypersonal
def main(): 
    '''
    '''
    st.caption('👋 Toby Gaskell here...')

    # left, right = st.columns(2)

    # with left:

    with st.container(border = True):
        st.markdown('''
<span style="color:gray;opacity:0.6;">I am </span>
<span style="color:orange;opacity:1;">__confident,__</span>
<span style="color:orange;opacity:1;">__dependable__</span>
<span style="color:gray;opacity:0.6;"> and </span>
<span style="color:orange;opacity:1;">__motivated__</span>
<span style="color:gray;opacity:0.6;"> professional eager to thrive in an environment where I can learn from others and contribute </span>
<span style="color:orange;opacity:1;">__innovative__</span>   
<span style="color:gray;opacity:0.6;"> ideas. </span>

<span style="color:gray;opacity:0.6;">My expertise lies in ensuring </span>
<span style="color:orange;opacity:1;">__engineering__</span>
<span style="color:gray;opacity:0.6;">projects are completed efficiently and to the </span>
<span style="color:orange;opacity:1;">__highest quality,__</span>
<span style="color:gray;opacity:0.6;"> adhering to industry standards. I pride myself on my exceptional collaboration skills,
including the ability to </span>
<span style="color:orange;opacity:1;">__communicate effectively__</span>
<span style="color:gray;opacity:0.6;"> and understand requirements from both </span>
<span style="color:orange;opacity:1;">__technical__</span>
<span style="color:gray;opacity:0.6;"> and </span>
<span style="color:orange;opacity:1;">__non-technical__</span>
<span style="color:gray;opacity:0.6;"> stakeholders.</span>
                    
<span style="color:gray;opacity:0.6;"> I am </span>
<span style="color:orange;opacity:1;">__passionate__</span>
<span style="color:gray;opacity:0.6;"> about working with a diverse range of tools and technologies, continually seeking to expand my 
technical knowledge. As a </span>
<span style="color:orange;opacity:1;">__proficient__</span>
<span style="color:gray;opacity:0.6;">programmer, I specialize in </span>
<span style="color:orange;opacity:1;">__python__</span>
<span style="color:gray;opacity:0.6;">and have experience with other languages such as </span>
<span style="color:orange;opacity:1;">__Java__</span>
<span style="color:gray;opacity:0.6;"> and </span>
<span style="color:orange;opacity:1;">__Swift.__</span>

<span style="color:gray;opacity:0.6;"> Driven and </span>
<span style="color:orange;opacity:1;">__hardworking,__</span>
<span style="color:gray;opacity:0.6;"> I am excited by the possibilities within the field of </span>
<span style="color:orange;opacity:1;">__data__</span>
<span style="color:gray;opacity:0.6;"> and technology.</span>
''', unsafe_allow_html = True)
    
    # with right: 
    #     st.caption('Personal Life')
    #     mypersonal.main()
    with st.expander('Checkout my Skills:'):
        myskills.main()


# <span style="color:orange;opacity:1;"> __confident__ </span>  