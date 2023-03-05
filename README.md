# OpenAI Language Learning Assistant

This program uses the OpenAI API to generate responses for language learning purposes. The user inputs a language and a word, phrase, or verb they want to learn more about, and the program generates responses in that language. The user can choose between different types of responses depending on their learning goals, such as noun phrases, verb conjugation, and short stories.

### Required:
`OPENAI API KEY`

### Installation and Dependencies

This program requires Python 3.6 or above and the following dependencies:
* os
* time
* rich
* threading
* pyperclip
* openai
* dotenv

To install the required dependencies, run the following command in your terminal:

`pip install -r requirements.txt`

### Usage

To run the program, navigate to the directory where the program is saved and run the following command in your terminal:
`python main.py`

The program will prompt the user to select a language and the type of response they want to generate. The user inputs the desired information, and the program generates a response using the OpenAI API.

### Features

The OpenAI Language Learning Assistant has the following features:
* Language selection: The user can select from a list of supported languages, including Catalan, English, German, Spanish, Portuguese, and Italian.
* Response generation: The user can choose from several response types, including noun phrases, common collocations, long sentences, verb conjugation, and short stories.
* Verb conjugation: The program can generate conjugated verb examples for the user to learn.
* Short stories: The program can generate short stories based on the user's input to make language learning more engaging.
* Clipboard functionality: The generated response is automatically copied to the clipboard for easy access.
* Program options: The program provides options to change the language, quit the program, and view more options.

### Future Work

* Saving generated responses: A future feature could include the ability to save generated responses to a text file or Excel document.
* Additional languages: The program could support additional languages in the future.
* Improved response accuracy: The program's response accuracy could be improved by using a more powerful OpenAI API plan or by implementing a machine learning model.
