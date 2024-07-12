# Ollama Models Chatbot with Streamlit

This repository contains a Streamlit application that leverages Ollama models to create an interactive chatbot. The chatbot responds to user queries and generates relevant text responses. This project aims to provide a seamless interface for exploring data through natural language queries.

## Features

- **Interactive Chatbot:** Engage with the chatbot to ask questions.
- **Text Responses:** The chatbot generates textual answers of the data.
- **Ollama Models Integration:** Utilizes open-source Ollama models for generating responses.
- **Streamlit Interface:** A user-friendly web interface built with Streamlit.

## Installation

### Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/PynaPavani/ollama-streamlit-chatbot.git
   cd ollama-streamlit-chatbot
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download Ollama models:**

   Follow the instructions from the [Ollama documentation](https://ollama.ai/docs) to download and set up the models.


## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Open your browser:**

   Navigate to `http://localhost:8501` to interact with the chatbot.
