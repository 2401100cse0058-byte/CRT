def Reverse_String(s: str) -> str:
    reversed_str = ""
    
    for ch in s:
        reversed_str = ch + reversed_str
    
    return reversed_str


if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))