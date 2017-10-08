from ScratchPri import Priority
from SunderingClaws import Node
from bitstring import Bits

def rec_build_encoding_table(node, encoding_table, encoding):
    if node.is_leaf():
        encoding_table[node.value] = encoding
    else:
        rec_build_encoding_table(node.child2, encoding_table, encoding + '0')
        rec_build_encoding_table(node.child1, encoding_table, encoding + '1')

def table(str):
    frequency_table = {}
    for chr in str:
        if chr not in frequency_table:
            frequency_table[chr] = 1
        else:
            cur_freq = frequency_table[chr]
            frequency_table[chr] = cur_freq + 1
    return frequency_table

def rec_decode_str(encode_str, idx, decode_str, node):

    if node.is_leaf():
        return idx, decode_str + node.value
    else:
        next_encode_chr = encode_str[idx]
        if next_encode_chr == '0':
            next_node = node.child2
        else:
            next_node = node.child1
        return rec_decode_str(encode_str, idx+1, decode_str, next_node)


def main():
    q = Priority()

    string = "3"

    bytes = string.encode("utf-8")

    bit_string = Bits(bytes=bytes)

    print(bit_string.bin)

    frequency_table = table(string)


    for chr, freq in frequency_table.items():
        q.push(freq, Node(freq, None, chr))

    huffman_tree = None
    while True:
        freq1, node1 = q.pop()
        freq2, node2 = q.pop()
        if node2 is None:
            huffman_tree = node1
            break

        new_freq = freq1+freq2
        new_node = Node(new_freq, None, None)
        new_node.child1 = node1
        new_node.child2 = node2
        q.push(new_freq, new_node)
    encoding_table = {}
    rec_build_encoding_table(huffman_tree, encoding_table, "")

    encode_str = ""
    for chr in string:
        encode_chr = encoding_table[chr]
        encode_str += encode_chr
    print(encode_str)
    decode_str = ""
    idx = 0
    while idx < len(encode_str):
        idx, decode_str = rec_decode_str(encode_str,
                                        idx,
                                        decode_str,
                                        huffman_tree)
    print(decode_str)




if __name__ == "__main__":
    main()