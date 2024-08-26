
# 🗨️ Streamlit Chat Application with Ollama

This Streamlit application provides an interactive chat interface that allows users to interact with different AI models powered by Ollama. It offers a simple and user-friendly experience, making it easy to explore conversational AI.

## ✨ Features

- **🎛️ Model Selection**: Users can select from various available Ollama models via a dropdown menu.
- **💬 Chat Interface**: An intuitive chat interface enables users to input messages and receive responses from the chosen model.
- **📝 Chat History**: *(Currently commented out in the code)* Optional feature to display and clear chat history.
- **📱 Responsive UI**: Designed to be responsive, ensuring a seamless experience across different devices.

## ⚙️ Requirements

- 🐍 Python 3.x
- 🌐 Streamlit
- 🔑 Ollama API credentials (if required for model access)

## 🛠️ Setup

1. **📥 Clone the repository**:

   ```bash
   git clone https://github.com/Deepanshu291/Ollama-streamlit.git
   cd Ollama-streamlit
   ```

2. **📦 Install dependencies**: Ensure Python is installed, then install the necessary packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **🔧 Configure Ollama API**:

   If Ollama requires an API key or authentication token, configure it in the `get_res` function or within the `ollama.initialize()` method as needed.

## 🚀 Usage

1. **▶️ Run the Streamlit app**:

   ```bash
   streamlit run main.py
   ```

   This command starts the Streamlit development server and opens the app in your default web browser.

2. **💻 Interact with the Application**:

   - Use the sidebar to select a model from the dropdown list.
   - Enter your message in the chat input box and press Enter or click Send.
   - The selected model will generate and display a response based on your input.

3. **🧹 Clear Chat History** *(if enabled)*:

   - Click the "Clear History" button to clear the chat history.

## 📋 Additional Notes

- 📶 Ensure a stable internet connection for accessing Ollama models and receiving responses.
- 🛠️ You can customize the application by adding features like persistent chat history, more model options, or UI/UX enhancements.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---