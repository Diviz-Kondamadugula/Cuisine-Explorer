# Cuisine Explorer

Cuisine Explorer is a Streamlit application that leverages OpenAI's GPT models via the LangChain library to generate unique restaurant names and corresponding menu items based on user-selected cuisines.

## Features

- **Cuisine Selection**: Users can choose from a variety of cuisines, including Indian, Italian, Mexican, and more, to explore potential restaurant concepts.
- **Dynamic Content Generation**: Generates a restaurant name and a list of menu items tailored to the selected cuisine.
- **User-friendly Interface**: Built with Streamlit, the application offers a clean and interactive UI for users to engage with.

## Setup

To run this project, you need Python 3.6 or later.

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourgithubusername/cuisine-explorer.git
cd cuisine-explorer
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include:
- `streamlit`
- `openai`
- `langchain-community`

### Configuration

Before running the application, you need to set up your OpenAI API key. This project uses a `secret_key.py` file to manage the API key securely.

1. Obtain an API key from [OpenAI](https://openai.com/).
2. Create a `secret_key.py` file in the project root with the following content:

```python
openapi_key = 'your_openai_api_key_here'
```

Replace `'your_openai_api_key_here'` with your actual OpenAI API key.

## Running the Application

To start the Streamlit application, run:

```bash
streamlit run main.py
```

Navigate to the URL provided by Streamlit in your web browser to use the application.

## Usage

- Use the sidebar to select a cuisine.
- Click the "Generate Restaurant Name and Menu" button.
- Explore the generated restaurant name and menu items.

## Contributing

Contributions to the Cuisine Explorer are welcome! Please refer to the contributing guidelines for more information.
