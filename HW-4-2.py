def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (yes/no) ")
        if correct == 'yes':
            print(f"Welcome back, {username}!")
            return

    username = get_new_username(path)
    print(f"We'll remember you when you come back, {username}!")