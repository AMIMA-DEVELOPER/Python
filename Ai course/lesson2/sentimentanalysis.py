import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}???????? WELCOME TO SENTIMENT SPY!{Style.RESET_ALL}")

user_name = input(f"{Fore.BLUE}PLEASE ENTER YOUR NAME:{Style.RESET_ALL}").strip()

if not user_name:
    user_name = "MYSTERY AGENT"

conversation_historu = []

print(f"{Fore.CYAN}HELLO AGENT!{user_name}")

print(f"Type a sentence and i wil analyze your sentences with Textblod and show you the sentiement.")

print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN},{Fore.YELLOW}'history'{Fore.CYAN},"

f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print("Please enter valid command")

        continue
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE} EXITING, BYE AGENT{user_name}! {Style.RESET_ALL}")

        break
    elif user_input.lower() == "reset":
        conversation_historu.clear()
        print(f"{Fore.CYAN} A;; chat history cleared!!")

    elif user_input.lower() == "history":
        if not conversation_historu:
            print(f"\n{Fore.YELLOW} NO CHAT HISTORY{user_name}! {Style.RESET_ALL}")

        else:
              print(f"\n{Fore.CYAN} CHAT HISTORY:{user_name}! {Style.RESET_ALL}")

              for idx, (text, polarity, sentiment_type) in enumerate(conversation_historu, start=1):
                  
                  if sentiment_type == "positive":
                    color = Fore.GREEN
                    emoji = "????"

                  elif sentiment_type == "neutral":
                    color = Fore.YELLOW
                    emoji = "????"

                  else:
                    color = Fore.RED
                    emoji = "????"

                  print(f"{idx}. {color}{emoji} {text} "

                    f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")

              continue






























































