import Compression
from NumberConversion import bin_to_dec, dec_to_bin_list
import random

if __name__ == '__main__':

    bits = list()

    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(7))
    bits.append(dec_to_bin_list(4))
    bits.append(dec_to_bin_list(4))
    bits.append(dec_to_bin_list(4))
    bits.append(dec_to_bin_list(4))
    bits.append(dec_to_bin_list(2))
    bits.append(dec_to_bin_list(2))


    d = Compression.generate_codes(bits)

    for i in d:
        print(i, d[i])
