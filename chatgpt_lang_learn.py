import os
import time
from rich import print
import threading


from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# ----------------------------------------------------------------

# TODO: save generated answers in txt file or excel or so

import openai

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
        time.sleep(0.1)
        # while not stop_event.is_set():
        #     for char in wait_string:
        #         if counter == 79:
        #             counter = 0
        #             print("\n")
        #         counter += 1
        #         print(char, end="")
        #         time.sleep(0.2)
        time.sleep(0.01)
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


languages = {"Catalan": "ca", "English": "en", "German": "de"}

print("-" * 60)

# ----------------------------------------------------------------
# MAIN LOOP

program_run = True

print("Choose your language: ")
for lang, code in languages.items():
    print(
        f"""
          {lang:<7} ->> {code}"""
    )

print()  # blank line


def ask_for_language():
    lang = input("Language: ")

    for language, language_code in languages.items():
        if language_code == lang:
            lang = language

    return lang


while program_run:
    lang = ask_for_language()
    num_of_phrases = input("How many sentences (hit ENTER for default = 3): ")
    if len(num_of_phrases) == 0:
        num_of_phrases = 3

    prompt = input("Insert word or phrase: \n>>> ")
    prompt += f"Act as if you were an amazing teacher of {lang} and you are teaching me this language and give me {num_of_phrases} long sentences  in {lang} with this word or phrase: '{prompt}' so I can learn it very well"

    # waiting_for_answer_animation()

    # response = generate_response(prompt)

    def response_func(stop_event):
        try:
            response = generate_response(prompt)
            print()
            print(f"[bold yellow]{response}[/bold yellow]")
            print()
            stop_event.set()
        except Exception:
            print("Something went wrong!")

    # ----------------------------------------------------------------
    ###########
    # THREADS #
    ###########

    # Create a shared event to signal the first thread to stop
    stop_event = threading.Event()

    # Create threads for each function
    thread1 = threading.Thread(target=waiting_for_answer_animation, args=(stop_event,))
    thread2 = threading.Thread(target=response_func, args=(stop_event,))

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish before exiting
    thread1.join()
    thread2.join()
    # ----------------------------------------------------------------
    # response_func()

    # print(f"[bold yellow]{response}[/bold yellow]")

    print("-" * 60)

    # FIXME: when user selects 'c' make it continue with the same language, not offer change it
    # FIXME: the whole selection thing is not working well
    user_choice = input('Hit >>> "c" to continue or >>> "h" for help\n\n')

    if user_choice == "q":
        print()
        break
    elif user_choice == "h":
        print(
            """
              Insert: "change" to change language
              Insert: "q" to quit program
              """
        )
        user_choice = input(">>> ")
        if user_choice == "change":
            program_run = True

bye_string = "\nThis program is finished now. Have a great day"

for word in bye_string.split():
    print()
    print("          " + word)
    time.sleep(0.2)

time.sleep(1)
