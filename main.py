import streamlit as st 
import ollama 



#Sample Example
def get_res(user_input,selected_model):
    res = ollama.chat(model=selected_model,messages=[
    {
        'role':'user',
        'content': user_input
    }
    ])
    return res


stb = st.sidebar
with stb:
    st.title("📝 Phi-3 and Ollama with Streamlit")
    st.subheader("📌Building Interactive AI Applications 🔍")
    st.divider()
    models = ollama.list()['models']
    model_names = [model['name'] for model in models]

# Streamlit app
    st.title('Select Ollama Model')
    selected_model = st.selectbox('Choose a model', model_names)

    st.divider()
    # st.title("chat history")
    # if 'chat' not in st.session_state:
    #     st.session_state.chat = []
    
    # for i,chat  in enumerate(st.session_state.chat):
    #     st.write(f"{i+1}. {chat}")
    
    btn = st.button("clear History")
    if btn: 
        st.session_state.clear()



st.title(f"💬{selected_model} with Ollama📝")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    # if not openai_api_key:
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()

    # client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    # st.session_state.chat.append(prompt)
    st.chat_message("user").write(prompt)
    with st.spinner('Wait for it...'):
        response = get_res(prompt,selected_model)
    st.success('Done!')    
    # response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response['message']['content']
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
   