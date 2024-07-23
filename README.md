# 🗣️ OpenAI Language Learning Assistant

This program uses the OpenAI API to generate responses for language learning purposes. The user inputs a language and a word, phrase, or verb they want to learn more about, and the program generates responses in that language. The user can choose between different types of responses depending on their learning goals, such as noun phrases, verb conjugation, and short stories.

### 📺 DEMO

<img src="./static/OpenAI Language Learning Assistant SHOW.gif" alt="GIF Video Demo of App" width="700" />

### 💪 Required:

`OPENAI API KEY`

### 💻 Installation and Dependencies

This program requires 🐍 Python 3.6 or above and the following dependencies:

- os
- time
- rich
- threading
- pyperclip
- openai
- dotenv
- pyinputplus

To install the required dependencies, run the following command in your terminal:

`pip install -r requirements.txt`

### 🧑‍💻 Usage

1.  Clone the repository to your local machine.
2.  Install the required packages using pip.
3.  Add your OpenAI API key to the `.env` file with the following name 'OPENAI_API_KEY'
4.  Open the terminal and navigate to the directory where the program is located.
5.  Run the program by typing `python main.py`.

The program will prompt the user to select a language and the type of response they want to generate. The user inputs the desired information, and the program generates a response using the OpenAI API **gpt-4o-mini**. This new model (July 2024) is much better than previous ones, and significantly cheaper. [GPT-4o mini](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/)

The output will be printed to the console and also **copied** to your **clipboard** automatically.

You can run the program multiple times and generate different types of language output.

### ➡️ Program Features

The program has the following features:

- Language selection: The user can select from a list of supported languages, including Catalan, English, German, Spanish, Portuguese, and Italian.
- Response generation: The user can choose from several response types, including noun phrases, common collocations, long sentences, verb conjugation, short story, questions, and translation.
- Number of phrases: The user can choose the number of phrases they want to generate.
- Verb conjugation: The program can generate conjugated verb examples for the user to learn.
- Short stories: The program can generate short stories based on the user's input to make language learning more engaging.
- Clipboard functionality: The generated response is automatically copied to the clipboard for easy access.
- Program options: The program provides options to change the language, quit the program, and view more options.

### 💡 Future Work

- Saving generated responses: A future feature could include the ability to save generated responses to a text file or Excel document.
- Improved response accuracy: The program's response accuracy could be improved by using a more powerful OpenAI API plan or by implementing a machine learning model.
