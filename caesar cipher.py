print("CAESAR CIPHER")
alpha = ('abcdefghijklomnpqrstuvwxyz')
s = input("\nTEXT: ").strip()
n = int(input("KEY: "))
res = ''
for c in s:
    res += alpha[(alpha.index(c) + n) % len(alpha)]
print('CIPHERTEXT: ' + res + '')
input("\nPRESS THE 'ENTER' TO EXIT")
