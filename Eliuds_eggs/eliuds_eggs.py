def egg_count(display_value):
    eggs = 0
    for v in str(bin(display_value)):
        if v == '1':
            eggs += 1
    return eggs


print(egg_count(18))