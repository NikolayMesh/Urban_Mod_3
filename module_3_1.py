calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(a):
    count_calls()
    return len(a), a.upper(), a.lower()


def is_contains(*args):
    count_calls()
    list_ = args[1]
    for i in list_:
        if args[0].lower() == i.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

