import streamlit as st
import replicate
import os

# App title
st.set_page_config(page_title="🦙💬 Llama 2 Chatbot")

# replicate credentials
with st.sidebar:
    st.title("🦙💬 Llama 2 Chatbot")
    #st.title('Hello World 👋')  
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter your Replicate API key', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter a valid API key', icon='⚠️')
        else:
            st.success('Proceed to entering your Prompt message', icon='✅')
    os.environ['REPLICATE_API_TOKEN'] = replicate_api
    
    st.subheader('Models and Parameters')
    selected_model = st.sidebar.selectbox('Select a Llama2 model', ['Llama2-&B', 'Llama2-13B'], key='selected_model')
    