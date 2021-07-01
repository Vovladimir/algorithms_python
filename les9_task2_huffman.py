'''
Закодируйте любую строку по алгоритму Хаффмана.
'''
from collections import Counter, deque, namedtuple
import heapq


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_frq, _count, root)] = h
        root.walk(code, "")

    return code


def huffman_decode(en, code):
    pointer = 0
    encoded_str = ''
    while pointer < len(en):
        for ch in code.keys():
            if en.startswith(code[ch], pointer):
                encoded_str += ch
                pointer += len(code[ch])
    return encoded_str

def main():
    s = input('Введите строку: ')
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print(f'{ch}:{code[ch]}')
    print(f'Кодовое предстваление строки = {encoded}')
    print(f'Проверочная декодировка. Закодированная строка = {huffman_decode(encoded, huffman_encode(s))}'\
              if s == huffman_decode(encoded, huffman_encode(s)) else 'Что-то пошло не так!')


if __name__ == "__main__":
    main()

