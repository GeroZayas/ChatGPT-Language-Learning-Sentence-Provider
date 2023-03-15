import os
import time
from rich import print
import threading
from prettytable import PrettyTable

# A module that allows you to copy text to the clipboard.
import pyperclip

import openai

# A module that allows you to validate user input.
import pyinputplus as pyip

# Loading the environment variables from the .env file.
from dotenv import load_dotenv

load_dotenv()


def main(language=None, type_generation=None, num_phrases=None, prompt=None, loop=None):
    """
    It prints out the values of the arguments passed to it

    :param language: The language to use
    :param type_generation:
    :param num_phrases: The number of phrases to generate
    :param prompt: The prompt to use for the generation
    :param loop: If True, the program will loop until the user presses Ctrl-C
    """
    if language is not None:
        print(f"Language is {language}")
    if type_generation is not None:
        print(f"Type of generation is {type_generation}")
    if num_phrases is not None:
        print(f"Number of phrases (etc.) is {num_phrases}")
    if prompt is not None:
        print(f"Prompt is {prompt}")

    # ----------------------------------------------------------------

    # Getting the value of the environment variable `OPENAI_API_KEY`
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

    openai.api_key = OPENAI_API_KEY

    # ----------------------------------------------------------------
    def waiting_for_answer_animation(stop_event):
        """
        It prints a message for the user to know that the answer is coming and the program is running. It
        uses time.sleep() to create a simple animation of every character in the string

        :param stop_event: This is the event that will be used to stop the thread
        """
        counter = 0
        wait_string = "answer is coming..."
        for letter in wait_string:
            print(f"[bold red]{letter}[/bold red]", end="")
            time.sleep(0.05)
        print()

    def generate_response(prompt):
        """
        It takes a prompt and returns a response

        :param prompt: The prompt is the text that you want to generate a response to
        :return: A string of text.
        """
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            # The maximum number of tokens that the model will generate.
            max_tokens=1000,
            # The number of completions to return.
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

    # A dictionary that contains the languages that the user can choose from.
    languages = {
        "Catalan": "ca",
        "English": "en",
        "German": "de",
        "Spanish": "sp",
        "Portuguese": "pt",
        "Italian": "it",
    }

    languages_table = PrettyTable()
    languages_table.field_names = ["Language", "Lang. Code"]

    for lang, lang_code in languages.items():
        languages_table.add_row([lang, lang_code])

    assert language is None, f"language is actually >>>> {language}"

    languages_table.align = "c"
    languages_table.padding_width = 2

    print("-" * 60)

    # ----------------------------------------------------------------

    # Printing out the languages that the user can choose from.
    if language is None:
        print(f"[yellow]{languages_table}[/yellow]")

        print("\nChoose your language: ")

    print()  # blank line

    def ask_for_language(language=language):
        """
        If the language is not specified, ask the user for a language. If the language is specified,
        return the language

        :param language: The language to translate to
        :return: The language code
        """

        lang = input("Language: ")

        # Checking if the language code is in the dictionary and if it is, it is changing the value of lang to
        # the language.
        for language, language_code in languages.items():
            if language_code == lang:
                lang = language

        return lang

    def generator_choice():
        """
        It takes a dictionary of options and prints them out to the user.

        The user then inputs a value and the function returns the key associated with that value.

        The function is called in the main function.

        The main function then calls the appropriate function based on the user's input.

        :return: The user's choice of what to generate.
        """

        # A dictionary of options for the user to choose from.
        gen_opt = {
            "Noun Phrases": "np",
            "Common Collocations": "cc",
            "Long Sentences": "ls",
            "Verb Conjugation": "vc",
            "Short Story": "ss",
            "Questions": "q",
            "Translate": "t",
        }

        print(
            """
              Select what you want to generate:
              """
        )

        for k, v in gen_opt.items():
            print("-" * 60)  # terminal separator
            print(f"For '{k}' insert '{v}'")
            time.sleep(0.1)

        print("-" * 60)  # terminal separator

        # Taking the user input and matching it to the key in the dictionary.
        user_gen_opt = input(">>> ")
        for k, v in gen_opt.items():
            if user_gen_opt == v:
                user_gen_opt = k

        return user_gen_opt

    # ----------------------------------------------------------------

    # Checking if the language is None. If it is, it will ask for the language. If it is not, it will
    # set the language to the language that was passed in.
    lang = ""
    lang = ask_for_language() if language is None else language
    # ----------------------------------------------------------------

    # Creating a loop that will run the program until the user decides to quit.
    program_run = True

    while program_run:
        print()  # space

        # Checking if the type_generation is None. If it is, it will call the generator_choice()
        # function. If it is not, it will set the gen_opt to type_generation.
        gen_opt = ""
        gen_opt = generator_choice() if type_generation is None else type_generation

        print()  # space

        print(
            "[bold light_sea_green]Selected Language: [/bold light_sea_green]", end=""
        )
        print(f"[bold yellow]'{gen_opt}' in {lang}[/bold yellow]\n")

        num_of_phrases = 0

        # Asking the user to input a number of phrases to generate.
        if num_phrases is None:
            if not gen_opt in ("Short Story", "Translate"):
                num_of_phrases = (
                    pyip.inputNum(
                        "How many sentences (default np & cc = 10, ls = 3): ",
                        blank=True,
                    )
                    or 0
                )

                if num_of_phrases == 0:
                    if gen_opt == "Long Sentences":
                        num_of_phrases = 3
                    elif gen_opt in [
                        "Common Collocations",
                        "Noun Phrases",
                        "Questions",
                    ]:
                        num_of_phrases = 10
                    elif gen_opt == "Verb Conjugation":
                        num_of_phrases = 6
                    elif gen_opt == "Short Story":
                        num_of_phrases = "Varied (short story) :)"

                print("This is num of phrases: ", num_of_phrases)

        else:
            num_of_phrases = num_phrases

        print()  # space

        user_prompt = ""

        if prompt is not None:
            user_prompt = prompt
        else:
            if gen_opt == "Short Story":
                user_prompt = input(
                    "\nInsert words or phrases to include in the story: \n>>> "
                )
                user_prompt = user_prompt.strip().split()
                user_prompt = " ".join(user_prompt)
                print("\nMaking a story with these elements: ", user_prompt)
            else:
                user_prompt = input("\nInsert word, phrase or verb: \n>>> ")

        # ----------------------------------------------------------------
        # CHANGE THE PROMPT FOR CHATGPT ACCORDING
        # TO USER TYPE OF GENERATION CHOICE

        # VERB CONJUGATION OPTION
        if gen_opt == "Verb Conjugation":
            tense = input("\nConjugation tense? \n>>> ")

            chat_prompt = f"Act as if you were an amazing teacher of {lang} and you are teaching me this language. Conjugate this verb: '{user_prompt}' in {tense} and give me an example medium-large sentence for each personal pronoun, please. Make sure everything you give me is in {lang}"

        # SHORT STORY OPTION
        elif gen_opt == "Short Story":
            chat_prompt = f"Act as if you were an amazing teacher of {lang} and an excellent storyteller and you are teaching me this language. Use these words: '{user_prompt}'and create an interesting and fun short story that includes them. Make sure everything you give me is in {lang}"

        # MAKE QUESTIONS OPTION
        elif gen_opt == "Questions":
            chat_prompt = f"Act as if you were an amazing teacher of {lang} and you are teaching me this language. Use these words: '{user_prompt}' and formulate interesting and fun questions to elicit in me varied answers and  practice conversation using those words. Make sure everything you give me is in {lang}. The questions don't have to only about learning {lang}, they could be about daily life and different topics."

        # TRANSLATE OPTION
        elif gen_opt == "Translate":
            target_lang = input("\nInsert target language\n>>> ")

            chat_prompt = f"Act as if you were an amazing teacher and translator of {lang} and you are teaching me this language. Traslate these words or phrases into {target_lang}: '{user_prompt}' and give me 2 sentences examples sentences, first in {lang} and then in {target_lang}."

        # COMMON COLLOCATIONS, NOUN PHRASES, ETC. OPTIONS
        else:
            chat_prompt = f"Act as if you were an amazing teacher of {lang} and you are teaching me this language. Now you give me {num_of_phrases} {gen_opt}  in {lang} with this word or phrase: '{user_prompt}' so I can learn it very well. Make sure everything you give me is in {lang}"

        final_response = ""

        def response_func(stop_event):
            """
            It takes a string as input, and returns a string as output

            :param stop_event: This is the event that will be used to stop the thread
            """
            try:
                response = generate_response(chat_prompt)
                print()
                print(f"[bold yellow]{response}[/bold yellow]")
                print()
                stop_event.set()
                pyperclip.copy(response)
                final_response = response
                print("Text copied to clipboard!")
            except Exception:
                print("Something went wrong!")

        # ----------------------------------------------------------------
        ###########
        # THREADS #
        ###########

        # Create a shared event to signal the first thread to stop
        stop_event = threading.Event()

        # Create threads for each function
        thread1 = threading.Thread(
            target=waiting_for_answer_animation, args=(stop_event,)
        )
        thread2 = threading.Thread(target=response_func, args=(stop_event,))

        # Start both threads
        print()  # blank line - space
        thread1.start()
        thread2.start()

        # Wait for both threads to finish before exiting
        thread1.join()
        thread2.join()
        # ----------------------------------------------------------------

        print("-" * 60)

        if loop == "no":
            program_run = False
        else:
            user_choice = input(
                'Hit >>> "ENTER" to continue or >>> "op" for more options\n\n'
            )

            if user_choice == "op":
                print(
                    """
                    Insert: "ch" to change language
                    Insert: "q" to quit program
                    """
                )
                user_choice = input(">>> ")
                if user_choice == "ch":
                    print_list_languages()
                    lang = ask_for_language()
                    program_run = True
                elif user_choice == "q":
                    program_run = False

    if loop != "no":
        bye_string = "\nThis program is finished now. Have a great day"

        counter = 10
        for word in bye_string.split():
            print()
            print(" " * counter, f"[bold deep_sky_blue3]{word}[/bold deep_sky_blue3]")
            counter += 4
            time.sleep(0.15)

        time.sleep(1)

    return str(final_response)


if __name__ == "__main__":
    main()
