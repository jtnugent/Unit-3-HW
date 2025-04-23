from pathlib import Path

path = Path('guest.txt')

def main():
    user_name = str(input("What's your name? "))
    path.write_text(user_name)
    


main()
