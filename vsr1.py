def convert_to(num, to_type=None):
    TYPES = {
        'bin': '{:b}',
        'oct': '{:o}',
        'hex': '{:x}'
        }
    try: 
        num = int(num)
        if to_type and to_type in TYPES.keys():
            return TYPES[to_type].format(num)
        else:
            return num
    except:
        return('Bad number')


print(convert_to(num=17, to_type='bin'))
print(convert_to(num=17, to_type='oct'))
print(convert_to(num=17, to_type='hex'))
print(convert_to(num=17, to_type='mda'))
print(convert_to(num=17))
