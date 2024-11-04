def main():
    s_1 = "HT859092947c87F4cff7727181C{872a2ba640}"

    s = [''] * 3
    rax_3 = len(s_1)
    index = 0
    for i in range(3):
        for j in range(i, rax_3, 3):
            s[i] += s_1[index]
            index += 1
    
    original_input = ""
    for i in range(rax_3):
        original_input += s[i % 3][i // 3]
    print(f"Flag: {original_input}")

if __name__ == "__main__":
    main()
