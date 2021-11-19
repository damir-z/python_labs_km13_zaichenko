# ВАШ КОД ТУТ

def cons(head, tail=[]):
    tail.insert(0, head)
    return tail

def sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum(lst[1::])

# ПЕРЕВІРКА

l = cons(3,
        cons(2,
            cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')

print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')