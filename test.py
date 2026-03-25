def alphadigit():
    while True:
        s1 = input("Please enter Alpha and Numeric: ")
        for c in range(0, len(s1)):
            if (ord(s1[c]) not in range(97, 124) or ord(s1[c]) not in range(65, 92)) and not s1[c].isdigit():
                print("Invalid Alpha and Numeric")

        for c in range(0, len(s1)):
            if (ord(s1[c]) in range(97, 124) or ord(s1[c]) in range(65, 92)) and s1[c].isdigit():
                print(chr(ord(s1[c])), end="")
            break

# Main Program
alphadigit()