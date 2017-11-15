from heapq import heappush, heappop

from HuffmanTree import HuffmanTree, Node
from NumberConversion import bin_to_dec


def generate_codes(list_of_bits):

    count = dict()

    for i in list_of_bits:
        if bin_to_dec(i) in count:
            count[bin_to_dec(i)] = count[bin_to_dec(i)] + 1
        else:
            count[bin_to_dec(i)] = 1

    huffman_tree = HuffmanTree()

    h = []

    for i in count:
        t = huffman_tree.add_leaf(name=i)
        heappush(h, (count[i], t))

    while len(h) >= 2:
        weight1, v1 = heappop(h)
        weight2, v2 = heappop(h)

        v3 = huffman_tree.join(v1, v2)
        heappush(h, (weight1 + weight2, v3))

    huffman_tree.generate_codes(huffman_tree.root)

    leafs = huffman_tree.get_leafs()

    result = dict()

    for leaf in leafs:
        result[leaf.name] = leaf.code

    return result



