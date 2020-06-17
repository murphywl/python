print ("VIJINER CIPHER")
m = input("\nTEXT: ").strip()
k = input("KEY: ") 
k *= len(m) // len(k) + 1  
res = ''.join([chr((ord(j) + ord(k[i])) % 26 + ord('A')) for i, j in enumerate(m)])
print('CIPHERTEXT: ' + res + '')
input("\nPRESS THE 'ENTER' TO EXIT")
