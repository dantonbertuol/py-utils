import base64
import pyperclip
import pyshorteners as short
import string
import random


def icon():
    print(
        """
        PPPP   Y     Y       U     U  TTTTT  I  L      SSSS  
        P   P   Y   Y        U     U    T    I  L     S     
        PPPP      Y          U     U    T    I  L      SSS  
        P         Y           U   U     T    I  L         S 
        P         Y            UUU      T    I  LLLLL  SSSS  
        """
    )


def menu():
    print("0. Exit")
    print("1. Encode b64")
    print("2. Decode b64")
    print("3. Shorten URL")
    print("4. Generate password")
    try:
        option = int(input("Option: "))
        print("")
    except ValueError:
        print("Invalid option")
        return menu()

    return option


def b64encode(data):
    data = data.encode("utf-8")
    encoded_data = base64.b64encode(data).decode("utf-8")
    pyperclip.copy(encoded_data)  # Copia o resultado para a área de transferência
    return encoded_data


def b64decode(data):
    data = data.encode("utf-8")
    try:
        decoded_data = base64.b64decode(data).decode("utf-8")
    except Exception as e:
        decoded_data = e
    pyperclip.copy(decoded_data)  # Copia o resultado para a área de transferência
    return decoded_data


def url_shortener(data):
    shortner = short.Shortener()
    try:
        short_url = shortner.tinyurl.short(data)
        pyperclip.copy(short_url)  # Copia o resultado para a área de transferência
    except Exception as e:
        short_url = e
    return short_url


def psw_generator(size, symbols, amnt):
    chars = string.ascii_letters + string.digits
    psw: str = ""
    if symbols == "y":
        chars += string.punctuation
    for _ in range(amnt):
        temp_psw = "".join(random.choice(chars) for _ in range(size))
        psw += f"{temp_psw}\n"

    pyperclip.copy(psw)  # Copia o resultado para a área de transferência
    return psw


if __name__ == "__main__":
    icon()
    while True:
        option = menu()
        if option == 0:
            break
        elif option == 1:
            text = input("Text: ")
            print(f"Encoded text: {b64encode(text)}\n")
        elif option == 2:
            text = input("Text: ")
            print(f"Decoded text: {b64decode(text)}\n")
        elif option == 3:
            url = input("URL: ")
            print(f"Shortened URL: {url_shortener(url)}\n")
        elif option == 4:
            try:
                size = int(input("Size: "))
            except ValueError:
                print("Invalid size\n")
                continue
            with_symbols = input("Include symbols? (y/n): ")
            if with_symbols == "y" or with_symbols == "n":
                try:
                    amnt = int(input("Amount: "))
                except ValueError:
                    print("Invalid amount\n")
                    continue
                print(f"Password(s): \n{psw_generator(size, with_symbols, amnt)}\n")
            else:
                print("Invalid option\n")
        else:
            print("Invalid option")
