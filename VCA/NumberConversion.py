

def bin_to_dec(digits):
    return int("".join(str(x) for x in digits), 2)


def dec_to_bin_list(integer):
    result = list()

    while integer > 0:

        result.append(integer % 2)
        integer = integer // 2

    result.reverse()

    print(result)

    return result
