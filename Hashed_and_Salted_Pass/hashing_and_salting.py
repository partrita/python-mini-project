import hashlib
import secrets


def hashing(password: str, salt: bytes) -> str:
    """Derive a password hash using a slow, salted password KDF."""
    derived_key = hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=2**14,
        r=8,
        p=1,
    )
    return derived_key.hex()


def salting(length: int = 16) -> bytes:
    return secrets.token_bytes(length)


if __name__ == "__main__":
    salt = salting()
    password = input("Enter your password\n")
    secure_password = f"{salt.hex()}${hashing(password, salt)}"
    print("Password hashed successfully.")
