import random


class SimpleSubstitutionCipher:
    alphabet = 'абвгдежзиклмнопрстуфхцчшщыьэюя'

    def __init__(self, file_path):
        self.file_path = file_path
        self.key = self.__generate_key()
        self.content = self.encrypted_text = self.decrypted_text = None

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf8') as f:
            self.content = ''.join([line for line in f])

    def __generate_key(self):
        alphabet = SimpleSubstitutionCipher.alphabet
        alphabet_indexes = list(range(len(alphabet)))
        random.shuffle(alphabet_indexes)
        key = ''.join([alphabet[i] for i in alphabet_indexes])
        with open('./key.txt', 'w', encoding='utf8') as f:
            for i in range(len(alphabet)):
                f.write(f'{alphabet[i]} --> {key[i]}\n')
        return key

    def __helper(self, action='encrypt'):
        text = list(self.content)
        alphabet = SimpleSubstitutionCipher.alphabet
        alphabet += alphabet.lower()
        key = self.key + self.key.lower()
        if action == 'decrypt':
            text = list(self.encrypted_text)
            key, alphabet = alphabet, key
        for i in range(len(text)):
            if text[i] in alphabet:
                index_in_alphabet = alphabet.index(text[i])
                text[i] = key[index_in_alphabet]
        return ''.join(text)

    def encrypt_text(self):
        self.encrypted_text = self.__helper()

    def decrypt_text(self):
        self.decrypted_text = self.__helper('decrypt')
        print(self.decrypted_text == self.content)

    def write_file(self):
        with open('./encrypted.txt', 'w', encoding='utf8') as f:
            f.write(self.encrypted_text)


simple_substitution_cipher = SimpleSubstitutionCipher('./encrypt.txt')
simple_substitution_cipher.read_file()
simple_substitution_cipher.encrypt_text()
simple_substitution_cipher.decrypt_text()
simple_substitution_cipher.write_file()