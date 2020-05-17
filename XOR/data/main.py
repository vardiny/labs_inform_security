class XorCipher:
    def __init__(self, file_path, key):
        self.file_path = file_path
        self.key = key
        self.content = self.encrypted_text = self.decrypted_text = None

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf8') as f:
            self.content = ''.join([line for line in f])

    def __xor_operation(self, text):
        content_codes = list(map(ord, text))
        key_codes = list(map(ord, self.key))
        key_codes_length = len(key_codes)
        new_codes = []
        for i in range(len(content_codes)):
            j = i % key_codes_length
            new_codes.append(content_codes[i] ^ key_codes[j])
        return ''.join(list(map(chr, new_codes)))

    def encrypt_text(self):
        self.encrypted_text = self.__xor_operation(self.content)

    def decrypt_text(self):
        self.decrypted_text = self.__xor_operation(self.encrypted_text)
        print(self.decrypted_text == self.content)  # для проверки

    def write_file(self):
        with open('./encrypted.txt', 'w', encoding='utf8') as f:
            f.write(self.encrypted_text)


xor_cipher = XorCipher('./encrypt.txt', input('key: '))
xor_cipher.read_file()
xor_cipher.encrypt_text()
xor_cipher.decrypt_text()
xor_cipher.write_file()