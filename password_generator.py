import string
import random

if __name__ == "__main__":
    string_1 = string.ascii_lowercase
    string_2 = string.ascii_uppercase
    string_3 = string.digits
    string_4 = string.punctuation

    password = int(input("Enter Password Length: "))
    string_0 = []
    string_0.extend(list(string_1))
    string_0.extend(list(string_2))
    string_0.extend(list(string_3))
    string_0.extend(list(string_4))

    print("Your Password: ", end="")
    print("".join(random.sample(string_0, password)))
