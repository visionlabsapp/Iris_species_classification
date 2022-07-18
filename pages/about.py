"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st


def app():
    """This funciton creates the home page"""
    # Add ballons animation
    st.balloons()

    # Add title to the page
    st.title('About Me')

    # Create two columns
    img_col, content_col = st.columns([1, 1])

    with img_col:
        # Add your photo here
        st.image("./images/eddiechow.png")
        pass

    with content_col:
        # cust
        st.markdown("""<br><br><br>""", unsafe_allow_html=True)
        # Add your name 
        st.markdown('''### Name: [Eddie Chow()''')
        # Add your github
        st.markdown('''### GitHub: [Eddie Chow](https://github.com/eddiecityu)''')
        # Add your linkedin
        st.markdown('''### Linkedin: [Eddie Chow](https://www.linkedin.com/in/eddie-chow-a3860464/)''')