import argparse
from OpenAI_Language_Learning_Assistant import main

# EXAMPLE
# main(
#     language="Spanish",
#     type_generation="Noun Phrases",
#     num_phrases=10,
#     prompt="Donald Trump",
#     loop="no",
# )

parser = argparse.ArgumentParser(
    description="A program to generate questions, phrases, stories or more with based on OpenAi to learn and practice languages"
)

# define the command line arguments
parser.add_argument(
    "-l", "--language", type=str, help="choose the language to practice"
)
parser.add_argument(
    "-tg",
    "--type-generation",
    type=str,
    help="Choose between Noun Phrases, Short Story, Common Collocations, Long Sentences, Verb Conjugation and Questions",
)
parser.add_argument(
    "-n",
    "--number-phrases",
    type=int,
    help="How many phrases, question, etc. do you want?",
)
parser.add_argument("-p", "--prompt", help="What is the prompt?")
parser.add_argument(
    "-loop", default="yes", help="Choose if you want one answer or multiple ones"
)

# parse the arguments
args = parser.parse_args()

print(args)

main(
    language=args.language,
    type_generation=args.type_generation,
    num_phrases=args.number_phrases,
    prompt=args.prompt,
    loop=args.loop,
)
