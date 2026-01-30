import hashlib
import random
import string

doc = "Тут ничего нет :)"
print("Добро пожаловать в систему НЭП с безопасностью примерно как у банки с тушонкой")
choose = int(input('1 - подписать. 2 - получить доступ: '))

if choose == 1:
    print('Вы захотели подписать документ')
    privkey = random.randint(1,33)

    print(f"Ваш цезарьский ключ:{privkey}")

    hash_object = hashlib.sha256(doc.encode('utf-8'))

    hex_dig = hash_object.hexdigest()
    message = hex_dig

    print(f"Хеш текста документа:{hex_dig}")


    def caesar_hex(hex_string, shift):
        data = bytes.fromhex(hex_string)

        result = bytearray()
        for byte in data:
            new_byte = (byte + shift) % 256
            result.append(new_byte)

        return result.hex()


    original_hex = hex_dig
    shift = 3
    encrypted = caesar_hex(original_hex, shift)
    print(f"Оригинал: {original_hex}")
    print(f"Зашифровано: {encrypted}")



if choose == 2:
    key = int(input('Введите ваш ключ'))
    def caesar_hex(hex_string, shift):
        data = bytes.fromhex(hex_string)

        result = bytearray()
        for byte in data:
            new_byte = (byte + shift) % 256
            result.append(new_byte)

        return result.hex()

    encrypted = "56ec3762f8e329b8c0d0e0cec73e958ee7aea9e46b1bb08d149983c8bc79ce76"
    original_hex = encrypted
    shift = key
    encrypted2 = caesar_hex(original_hex, shift)
    print(f"Оригинал: {encrypted}")
    print(f"Зашифровано: {encrypted2}")
