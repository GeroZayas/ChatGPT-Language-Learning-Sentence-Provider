from options import languages
import time


def type_of_generation() -> str:
    """
    It takes a dictionary of options and prints them out to the user.

    The user then inputs a value and the function returns the key associated with that value.

    The function is called in the main function.

    The main function then calls the appropriate function based on the user's input.

    :return: The user's choice of what to generate.
    """

    gen_opt: dict[str, str] = {
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

    user_gen_opt = input(">>> ")
    for k, v in gen_opt.items():
        if user_gen_opt == v:
            user_gen_opt: str = k

    return user_gen_opt


def ask_for_language(language) -> str:
    """
    If the language is not specified, ask the user for a language. If the language is specified,
    return the language

    :param language: The language to translate to
    :return: The language code
    """

    lang: str = input("Language: ")

    for language, language_code in languages.items():
        if language_code == lang:
            lang = language

    return lang
