import os
import time
from rich import print
import threading
import pyperclip
import openai

from dotenv import load_dotenv

load_dotenv()


def main():
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

    # ----------------------------------------------------------------
    # * TODOS AND IDEAS *

    # *idea: save generated answers in txt file or excel or so

    # ----------------------------------------------------------------
    openai.api_key = OPENAI_API_KEY

    # ----------------------------------------------------------------
    def waiting_for_answer_animation(stop_event):
        """This function prints a message for the user to know that the
        answer is coming and the program is running. It uses time.sleep() to
        create a simple animation of every character in the string.
        """
        counter = 0
        wait_string = "answer is coming..."
        for letter in wait_string:
            print(f"[bold red]{letter}[/bold red]", end="")
            time.sleep(0.05)
        print()

    def generate_response(prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

    languages = {
        "Catalan": "ca",
        "English": "en",
        "German": "de",
        "Spanish": "sp",
        "Portuguese": "pt",
        "Italian": "it",
    }

    print("-" * 60)

    # ----------------------------------------------------------------
    # MAIN LOOP

    def print_list_languages():
        for lang, code in languages.items():
            print(
                f"""
                {lang:<11} ->> {code}"""
            )

    print_list_languages()

    print("\nChoose your language: ")

    print()  # blank line

    def ask_for_language():
        lang = input("Language: ")

        for language, language_code in languages.items():
            if language_code == lang:
                lang = language

        return lang

    def generator_choice():
        gen_opt = {
            "Noun Phrases": "np",
            "Common Collocations": "cc",
            "Long Sentences": "ls",
            # Add verb conjugation option
            "Verb Conjugation": "vc",
            "Short Story": "ss",
        }

        print(
            """
              Select what you want to generate:
              """
        )

        for k, v in gen_opt.items():
            print("-" * 60)  # terminal separator
            print(f"For '{k}' insert '{v}'")

        print("-" * 60)  # terminal separator

        user_gen_opt = input(">>> ")
        for k, v in gen_opt.items():
            if user_gen_opt == v:
                user_gen_opt = k

        return user_gen_opt

    lang = ask_for_language()

    program_run = True

    while program_run:
        print()  # space

        gen_opt = generator_choice()

        print()  # space

        print(
            "[bold light_sea_green]Selected Language: [/bold light_sea_green]", end=""
        )
        print(f"[bold yellow]'{gen_opt}' in {lang}[/bold yellow]\n")

        num_of_phrases = int(
            input("How many sentences (default np & cc = 10, ls = 3): ") or "0"
        )

        if num_of_phrases == 0:
            if gen_opt == "Long Sentences":
                num_of_phrases = 3
            elif gen_opt == "Noun Phrases" or gen_opt == "Common Collocations":
                num_of_phrases = 10
            elif gen_opt == "Verb Conjugation":
                num_of_phrases = 6
            elif gen_opt == "Short Story":
                num_of_phrases = "Varied (short story) :)"

        print("This is num of phrases: ", num_of_phrases)

        print()  # space

        if gen_opt == "Short Story":
            user_prompt = input(
                "\nInsert words or phrases to include in the story: \n>>> "
            )
            user_prompt = user_prompt.strip().split()
            user_prompt = " ".join(user_prompt)
            print("\nMaking a story with these elements: ", user_prompt)
        else:
            user_prompt = input("\nInsert word, phrase or verb: \n>>> ")

        if user_prompt == "":
            user_prompt = "It is important to..."

        if gen_opt == "Verb Conjugation":
            tense = input("\nConjugation tense? \n>>> ")

            chat_prompt = f"Act as if you were an amazing teacher of {lang} and you are teaching me this language. Conjugate this verb: '{user_prompt}' in {tense} and give me an example medium-large sentence for each personal pronoun, please. Make sure everything you give me is in {lang}"

        elif gen_opt == "Short Story":
            chat_prompt = f"Act as if you were an amazing teacher of {lang} and an excellent storyteller and you are teaching me this language. Use these words: '{user_prompt}'and create an interesting and fun short story that includes them. Make sure everything you give me is in {lang}"

        else:
            chat_prompt = f"Act as if you were an amazing teacher of {lang} and you are teaching me this language. Now you give me {num_of_phrases} {gen_opt}  in {lang} with this word or phrase: '{user_prompt}' so I can learn it very well. Make sure everything you give me is in {lang}"

        # waiting_for_answer_animation()

        # response = generate_response(prompt)

        def response_func(stop_event):
            try:
                response = generate_response(chat_prompt)
                print()
                print(f"[bold yellow]{response}[/bold yellow]")
                print()
                stop_event.set()
                pyperclip.copy(response)
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
        # response_func()

        # print(f"[bold yellow]{response}[/bold yellow]")

        print("-" * 60)

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

    bye_string = "\nThis program is finished now. Have a great day"

    counter = 10
    for word in bye_string.split():
        print()
        print(" " * counter, f"[bold deep_sky_blue3]{word}[/bold deep_sky_blue3]")
        counter += 4
        time.sleep(0.15)

    time.sleep(1)


if __name__ == "__main__":
    main()
