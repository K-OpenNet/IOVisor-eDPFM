from ast import literal_eval

INPUT_VALUE = str(134744072) # This value should be 8.8.8.8 after conversion
INPUT_VALUE2 = str(3232235777)

def decimal_to_human(input_value):
    input_value = int(input_value)
    hex_value = hex(input_value)[2:]
    print(str(hex_value) + '\n')
    pt3 = literal_eval((str('0x'+str(hex_value[-2:]))))
    pt2 = literal_eval((str('0x'+str(hex_value[-4:-2]))))
    pt1 = literal_eval((str('0x'+str(hex_value[-6:-4]))))
    pt0 = literal_eval((str('0x'+str(hex_value[-8:-6]))))
    print(str('pt0 :')  + '\n' + str(pt0) + '\n' + str('pt1 :') + str(pt1) + '\n' + str('pt2 :') + str(pt2) + '\n' + str('pt3: ') + str(pt3))
    result = str(pt0)+'.'+str(pt1)+'.'+str(pt2)+'.'+str(pt3)
    return result

print('\n\n\n')
print('first try : ')
print(decimal_to_human(INPUT_VALUE2))
print('\n')
print('second try : ')
print(decimal_to_human(INPUT_VALUE))
