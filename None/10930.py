import hashlib
t = input()
result = hashlib.sha256(t.encode())
print(result.hexdigest())