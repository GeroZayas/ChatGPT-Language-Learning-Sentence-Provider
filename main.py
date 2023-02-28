import os
import time
from rich import print


from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# ----------------------------------------------------------------

# TODO: save generated answers in txt file or excel or so

import openai

openai.api_key = OPENAI_API_KEY


# ----------------------------------------------------------------
def waiting_for_answer_animation():
    """This function prints a message for the user to know that the
    answer is coming and the program is running. It uses time.sleep() to
    create a simple animation of every character in the string.
    """
    wait_string = "Your answer is coming..."
    for character in wait_string:
        print(character, end="")
        time.sleep(0.1)


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

lang = input("Language: ")

for language, language_code in languages.items():
    if language_code == lang:
        lang = language

while program_run:
    num_of_phrases = input("How many sentences (hit ENTER for default = 3): ")
    if len(num_of_phrases) == 0:
        num_of_phrases = 3

    prompt = input("Insert word or phrase: \n>>> ")
    prompt += f"Act as if you were an amazing teacher of {lang} and you are teaching me this language and give me {num_of_phrases} long sentences  in {lang} with this word or phrase: '{prompt}' so I can learn it very well"

    waiting_for_answer_animation()

    response = generate_response(prompt)

    print()

    print(f"[bold yellow]{response}[/bold yellow]")

    print("-" * 60)

    user_quit = input('Hit >>> ENTER to continue or >>> "q" to quit\n\n')

    if user_quit == "q":
        print()
        break

bye_string = "\nThis program is finished now. Have a great day"

for word in bye_string.split():
    print()
    print("          " + word)
    time.sleep(0.2)

time.sleep(1)
