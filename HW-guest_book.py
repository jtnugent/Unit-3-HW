from pathlib import Path

path = Path('guest_book.txt')

def main():
    Continue = True
    contents = ''
    while Continue:
        user_name = str(input("What's your name? "))
        contents += f"{user_name}\n"
        done = input("are you done?(yes/no) ")
        if done == "yes":
            Continue =  False
    path.write_text(contents)

main()
