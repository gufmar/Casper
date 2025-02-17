import sys
sys.path.append(".")

from casper.utils import hash256, to_base32, to_hex
from casper.aes import AESCipher

F = AESCipher("test-password1234")

ENCRYPTED = F.encrypt("message")
DECRYPTED = F.decrypt(ENCRYPTED)

print(ENCRYPTED, DECRYPTED)
print(to_hex(to_base32(hash256(ENCRYPTED))))
