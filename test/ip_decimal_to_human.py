from ast import literal_eval

INPUT_VALUE = 134744072 # This value should be 8.8.8.8 after conversion
INPUT_VALUE2 = 3232235777

def decimal_to_human(input_value):
    hex_value = hex(input_value)[2:]
    print(str(hex_value) + '\n')
    pt3 = literal_eval((str('0x'+str(hex_value[-2:]))))
    pt2 = literal_eval((str('0x'+str(hex_value[-4:-2]))))
    pt1 = literal_eval((str('0x'+str(hex_value[-6:-4]))))
    pt0 = literal_eval((str('0x'+str(hex_value[-8:-6]))))
    print(str('pt0 :')  + '\n' + str(pt0) + '\n' + str('pt1 :') + str(pt1) + '\n' + str('pt2 :') + str(pt2) + '\n' + str('pt3: ') + str(pt3))

print('\n\n\n')
print('first try : ')
decimal_to_human(INPUT_VALUE2)
print('\n')
print('second try : ')
decimal_to_human(INPUT_VALUE)
