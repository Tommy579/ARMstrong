import openpyxl

from excel_reader import reader

df = openpyxl.load_workbook("../PARM-table.xlsx")
df1 = df.active

instructions, values = reader(df1)
print(len(instructions))
print(len(values))
print((values))

opcodes = []
tous_operandes = []

for i in range(len(instructions)):
    opcode=0b0
    operandes=[]

    for value in values[i]:
        if value == 1 or value == 0:
            opcode = (opcode<<1) | value
        else:
            operandes.append(value)
    opcodes.append(opcode)
    tous_operandes.append(operandes)


#     # --- EORS ---
#     elif mnemonic == 'EORS':
#         rdn = parse_register(parts[1])
#         rm = parse_register(parts[2])
#         opcode = 0b0100000001
#
#         machine_code = (opcode << 6) | (rm << 3) | rdn


with open("python_instructions.txt", 'w') as f:
    for i in range(len(instructions)):
        instruction=instructions[i]
        f.write(f"# ------- {instruction} -------\n")
        f.write(f"elif mnemonic == '{instruction}':\n")
        operandes = tous_operandes[i]
        for j in range(len(operandes)):
            operande = operandes[len(operandes)-j-1]
            if len(operande) < 4:
                f.write(f"\t{operande.lower()} = parse_register(parts[{j+1}])\n")
            else:
                f.write(f"\t{operande.lower()} = parse_immediate(parts[{j + 1}])\n")
        f.write(f"\topcode = {bin(opcodes[i])} \n\n")
        f.write("\tmachine_code = ")
        f.write(f"(opcode << x) | ")
        for j in range(len(operandes)):
            operande = operandes[j]
            if j == len(operandes)-1:
                f.write(f"{operande.lower()}\n\n\n")
            else:
                f.write(f"({operande.lower()} << x) | ")

print(instructions)

print("done :)")