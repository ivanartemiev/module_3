calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    string = {len(string), string.upper(), string.lower()}
    return string
def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() == string.lower():
            result = True
            break
        else:
            result = False
    return result
print(string_info('UnrbanLESSON'))
print(string_info('KarMAGeddon'))
print(string_info('VasiLisa'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cyCLe', ['recycling', 'cyclic']))
print(is_contains('sUn', ['Sunny', 'SUN', 'mooN']))
print(f'Количество вызовов функций: {calls}')
