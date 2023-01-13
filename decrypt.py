
all_chars = []

with open('总字符.txt', encoding='utf-8') as f:
    data = f.read()
    all_chars = data.split(' ')
    print('加载完毕：' + str(len(all_chars)))

while True:
    need_encrypt_str = input('请输入要解密的段落： ')

    decrypt_code = []
    for s in need_encrypt_str.split(' '):
        v = all_chars[int(s)]
        decrypt_code.append(v)

    print(''.join(decrypt_code))
