from pprint import pprint

list_dict = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(16)]

pprint(list_dict)
