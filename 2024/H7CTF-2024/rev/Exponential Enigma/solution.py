import math

def tetra(arg1, arg2):
    result = arg1
    for i in range(arg2 - 1):
        zmm0_1 = math.pow(arg1, result)
        if zmm0_1 >= 9.2233720368547758e+18:
            result = (zmm0_1 - 9.2233720368547758e+18) ^ 0x8000000000000000
        else:
            result = zmm0_1
    return int(result)

def main():
    var_38 = []
    
    for i in range(1, 5):
        rax_3 = tetra(2, i)
        rdx_1 = rax_3 // 19
        var_38.append(rax_3 - (((rdx_1 << 3) + rdx_1) * 2 + rdx_1))

    for value in var_38:
        print(int(value)) 

    output = "4a335351447f273d6461726637312164336222303b35213667302835376271343a37753530306d"
    
    output_bytes = bytes.fromhex(output)
    var_4c = 0

    while var_4c < len(output_bytes):
        temp0_1 = var_4c >> 30 
        temp1_1 = var_4c & 3    
        rdx_5 = (temp0_1 >> 30) 
        
        xor_value = (var_38[(temp1_1 + rdx_5) % 4]) & 0xFF
        result_char = chr(xor_value ^ output_bytes[var_4c])

        print(result_char, end='')
        var_4c += 1

    print()

if __name__ == "__main__":
    main()
