import assembly

def convert_to_string(L):
    string_result = ""
    for element in L:
        string_result += element +" "
    return string_result

def convert_assembly_file(file_path):
    result = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            hex_code = assembly.assemble_line(line)
            if hex_code:
                result.append(hex_code)
    result = convert_to_string(result)
    return result

def write_to_file(file_path):
    with open(file_path, "w") as fw:
        fw.write("v2.0 raw\n" + result)


# ------- To change -------
result = convert_assembly_file("assembly_test.txt")
print("v2.0 raw")
print(result)
write_to_file("test.txt")

# Résultat : 2005 2103 1842 0053 1e5b 9301 9c01 42a3 d0f9