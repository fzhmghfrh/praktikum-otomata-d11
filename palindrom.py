def is_palindrome(s):
    # Filter: hanya huruf dan angka, semua huruf ke kecil
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    return filtered == filtered[::-1]

def main():
    print("Multi Palindrome Checker")
    input_line = input("Masukkan beberapa string (pisahkan dengan koma): ")

    strings = [s.strip() for s in input_line.split(',') if s.strip()]

    if not strings:
        print("Tidak ada string yang dimasukkan.")
        return

    for idx, s in enumerate(strings, start=1):
        result = "palindrom" if is_palindrome(s) else "bukan palindrom"
        print(f"{idx}. '{s}' → {result}")

if __name__ == "__main__":
    main()
