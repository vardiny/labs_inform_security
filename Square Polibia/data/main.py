import random


class PolybiusSquare:
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    def __init__(self, file_path):
        self.file_path = file_path
        self.key = self.__generate_key()
        self.content = self.encrypted_text = self.decrypted_text = None

    def read_file(self):
        alphabet = PolybiusSquare.alphabet
        with open(self.file_path, 'r', encoding='utf8') as f:
            self.content = ''.join([line for line in f]).upper()
        self.content = list(self.content)
        for i in range(len(self.content)):
            if self.content[i] == 'J':
                self.content[i] = 'I'
        self.content = list(filter(lambda s: s in alphabet + ' ', ''.join(self.content)))
        self.content = ''.join(self.content)

    def __generate_key(self):
        alphabet = PolybiusSquare.alphabet
        alphabet_indexes = list(range(len(alphabet)))
        random.shuffle(alphabet_indexes)
        key = ''.join([alphabet[i] for i in alphabet_indexes])
        key = [list(key[i:i+5]) for i in range(0, len(key), 5)]
        with open('./keyFile.txt', 'w', encoding='utf8') as f:
            for i in range(len(key)):
                for j in range(len(key[i])):
                    f.write(f'{key[i][j]} - {i}, {j}\n')
        return key

    def __get_word_coordinates(self, word):
        coordinates = []
        for i in list(word):
            for row in range(len(self.key)):
                if i in self.key[row]:
                    column = self.key[row].index(i)
                    coordinates.append([row, column])
        return coordinates

    def __encrypt_word(self, word):
        coordinates = self.__get_word_coordinates(word)
        coordinates = [*[i[0] for i in coordinates], *[i[1] for i in coordinates]]
        coordinates = [[coordinates[i], coordinates[i+1]] for i in range(0, len(coordinates), 2)]
        return ''.join([self.key[i][j] for i, j in coordinates])

    def __decrypt_word(self, word):
        coordinates = self.__get_word_coordinates(word)
        coordinates = ' '.join([' '.join([str(j) for j in i]) for i in coordinates])
        coordinates = list(map(int, coordinates.split()))
        half_length = len(coordinates) // 2
        coordinates = list(zip(coordinates[:half_length], coordinates[half_length:]))
        return ''.join([self.key[i][j] for i, j in coordinates])

    def encrypt_text(self):
        self.encrypted_text = ' '.join([self.__encrypt_word(i) for i in self.content.split()])

    def decrypt_text(self):
        self.decrypted_text = ' '.join([self.__decrypt_word(i) for i in self.encrypted_text.split()])
        print(self.decrypted_text == self.content)

    def write_file(self):
        with open('./encrypted.txt', 'w', encoding='utf8') as f:
            f.write(self.encrypted_text)


polybius_square = PolybiusSquare('./encrypt.txt')
polybius_square.read_file()
polybius_square.encrypt_text()
polybius_square.decrypt_text()
polybius_square.write_file()