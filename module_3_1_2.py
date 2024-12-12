"""
Второй вариант решения задачи.

"""

print('Счетчик вызовов: ')
print('----------------------------------')
calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    result = tuple((len(string), string.upper(), string.lower()))
    count_calls()
    return result


def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == str(string).lower():
            result = True
            break
        else:
            result = False
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('DFGhh'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)