def oxford_comma(items):
    if len(items) == 1:
        print(''.join(items))
        return ''.join(items)
    elif len(items) == 2:
        return ' and '.join(items)
    elif len(items) > 2:
        print(', '.join(items[:-1]) + ', and ' + items[-1])
        return ', '.join(items[:-1]) + ', and ' + items[-1]
    
oxford_comma(['kiwi'])