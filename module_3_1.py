"""
Первый вариант решения задачи с применением команды, которую мы не проходили.
И через вложенный цикл.
Также не применил изначально команду return, из-за чего выходит строка None.

"""

print('Счетчик вызовов: ')
print('----------------------------------')
calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    #print(tuple((len(string), string.upper(), string.lower())))
    result = tuple((len(string), string.upper(), string.lower()))
    count_calls()
    return result

def is_contains(string, list_to_search):
    a = list([string])
    a1 = [x.lower() for x in  a]
    b = list_to_search
    c = [x.lower() for x in  b]
    count_calls()
    for i in a1:
        for j in c:
            if i != j:
                continue
            if i == j:
                #print(True)
                result = True
                break
        else:
            #print(False)
            result = False
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('DFGhh'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
