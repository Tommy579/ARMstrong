import re

# Convertit R0 en 0, R7 en 7
def parse_register(reg_str):
    return int(reg_str.upper().replace('R', ''))

# Convertit '#5' en 5, et '#0xA' en 10
def parse_immediate(imm_str):
    imm_str = imm_str.strip()

    # Enlever le #
    if imm_str.startswith('#'):
        imm_str = imm_str[1:]

    if imm_str.lower().startswith('0x'): # Pour l'hexa (0x)
        return int(imm_str, 16)

    return int(imm_str)


def assemble_line(line):
    # Nettoyage : enlever les commentaires (;) et espaces inutiles
    line = line.split(';')[0].strip()
    if not line: return None
    clean_line = line.replace('[', ' ').replace(']', ' ').replace('SP', ' ')

    # Séparation par virgules ou espaces
    parts = re.split(r'[,\s]+', clean_line.strip())
    mnemonic = parts[0].upper()

    machine_code = 0


# ------- AUTO GENERATED ------------
    # ------- LSLS -------
    if mnemonic == 'LSLS':
        if len(parts) == 4:
            rd = parse_register(parts[1])
            rm = parse_register(parts[2])
            imm5 = parse_immediate(parts[3])
            opcode = 0b0

            machine_code = (opcode << 11) | (imm5 << 6) | (rm << 3) | rd
        else:
            rm = parse_register(parts[2])
            rdn = parse_register(parts[1])
            opcode = 0b100000010

            machine_code = (opcode << 6) | (rm << 3) | rdn

    # ------- LSRS -------
    elif mnemonic == 'LSRS':
        if len(parts) == 4 :
            rd = parse_register(parts[1])
            rm = parse_register(parts[2])
            imm5 = parse_immediate(parts[3])
            opcode = 0b1

            machine_code = (opcode << 11) | (imm5 << 6) | (rm << 3) | rd

        else:
            rm = parse_register(parts[2])
            rdn = parse_register(parts[1])
            opcode = 0b100000011

            machine_code = (opcode << 6) | (rm << 3) | rdn


    # ------- ASRS -------
    elif mnemonic == 'ASRS':
        rd = parse_register(parts[1])
        rm = parse_register(parts[2])
        imm5 = parse_immediate(parts[3])
        opcode = 0b10

        machine_code = (opcode << 11) | (imm5 << 6) | (rm << 3) | rd


    # ------- ADDS -------
    elif mnemonic == 'ADDS':
        if len(parts) == 4:
            if 'R' in parts[3].upper():
                rd = parse_register(parts[1])
                rn = parse_register(parts[2])
                rm = parse_register(parts[3])
                opcode = 0b1100

                machine_code = (opcode << 9) | (rm << 6) | (rn << 3) | rd
            elif '#' in parts[3].upper():
                imm3 = parse_immediate(parts[3])
                rn = parse_register(parts[2])
                rd = parse_register(parts[1])
                opcode = 0b1110

                machine_code = (opcode << 9) | (imm3 << 6) | (rn << 3) | rd
            else:
                print("error : ADDS")
        else:
            print("error : ADDS")


    # ------- SUBS -------
    elif mnemonic == 'SUBS':
        if len(parts) == 4:
            if 'R' in parts[3].upper():
                rm = parse_register(parts[3])
                rn = parse_register(parts[2])
                rd = parse_register(parts[1])
                opcode = 0b1101

                machine_code = (opcode << 9) | (rm << 6) | (rn << 3) | rd
            elif '#' in parts[3].upper():
                imm3 = parse_immediate(parts[3])
                rn = parse_register(parts[2])
                rd = parse_register(parts[1])
                opcode = 0b1111

                machine_code = (opcode << 9) | (imm3 << 6) | (rn << 3) | rd
            else:
                print("error : SUBS")
        else:
            print("error : SUBS")


    # ------- MOVS -------
    elif mnemonic == 'MOVS':
        rd = parse_register(parts[1])
        imm8 = parse_immediate(parts[2])
        opcode = 0b100

        machine_code = (opcode << 11) | (rd << 8) | imm8


    # ------- ANDS -------
    elif mnemonic == 'ANDS':
        rm = parse_register(parts[2])
        rdn = parse_register(parts[1])
        opcode = 0b100000000

        machine_code = (opcode << 6) | (rm << 3) | rdn


    # ------- EORS -------
    elif mnemonic == 'EORS':
        rm = parse_register(parts[2])
        rdn = parse_register(parts[1])
        opcode = 0b100000001

        machine_code = (opcode << 6) | (rm << 3) | rdn


    # ------- ASRS -------
    elif mnemonic == 'ASRS':
        rm = parse_register(parts[2])
        rdn = parse_register(parts[1])
        opcode = 0b100000100

        machine_code = (opcode << 6) | (rm << 3) | rdn


    # ------- ADCS -------
    elif mnemonic == 'ADCS':
        rm = parse_register(parts[2])
        rdn = parse_register(parts[1])
        opcode = 0b100000101

        machine_code = (opcode << 6) | (rm << 3) | rdn


    # ------- SBCS -------
    elif mnemonic == 'SBCS':
        rm = parse_register(parts[2])
        rdn = parse_register(parts[1])
        opcode = 0b100000110

        machine_code = (opcode << 6) | (rm << 3) | rdn


    # ------- RORS -------
    elif mnemonic == 'RORS':
        rm = parse_register(parts[2])
        rdn = parse_register(parts[1])
        opcode = 0b100000111

        machine_code = (opcode << 6) | (rm << 3) | rdn


    # ------- TST -------
    elif mnemonic == 'TST':
        rm = parse_register(parts[2])
        rn = parse_register(parts[1])
        opcode = 0b100001000

        machine_code = (opcode << 6) | (rm << 3) | rn


    # ------- RSBS -------
    elif mnemonic == 'RSBS':
        rn = parse_register(parts[2])
        rdn = parse_register(parts[1])
        opcode = 0b100001001

        machine_code = (opcode << 6) | (rn << 3) | rdn


    # ------- CMP -------
    elif mnemonic == 'CMP':
        rm = parse_register(parts[2])
        rn = parse_register(parts[1])
        opcode = 0b100001010

        machine_code = (opcode << 6) | (rm << 3) | rn


    # ------- CMN -------
    elif mnemonic == 'CMN':
        rm = parse_register(parts[2])
        rn = parse_register(parts[1])
        opcode = 0b100001011

        machine_code = (opcode << 6) | (rm << 3) | rn


    # ------- ORRS -------
    elif mnemonic == 'ORRS':
        rm = parse_register(parts[2])
        rdn = parse_register(parts[1])
        opcode = 0b100001100

        machine_code = (opcode << 6) | (rm << 3) | rdn


    # ------- MULS -------
    elif mnemonic == 'MULS':
        rn = parse_register(parts[2])
        rdm = parse_register(parts[1])
        opcode = 0b100001101

        machine_code = (opcode << 6) | (rn << 3) | rdm


    # ------- BICS -------
    elif mnemonic == 'BICS':
        rm = parse_register(parts[2])
        rdn = parse_register(parts[1])
        opcode = 0b100001110

        machine_code = (opcode << 6) | (rm << 3) | rdn


    # ------- MVNS -------
    elif mnemonic == 'MVNS':
        rm = parse_register(parts[2])
        rd = parse_register(parts[1])
        opcode = 0b100001111

        machine_code = (opcode << 6) | (rm << 3) | rd


    # ------- STR -------
    elif mnemonic == 'STR':
        rt = parse_register(parts[1])
        imm8 = parse_immediate(parts[2])
        opcode = 0b10010

        machine_code = (opcode << 11) | (rt << 8) | ((imm8 >> 2) & 0xFF)


    # ------- LDR -------
    elif mnemonic == 'LDR':
        rt = parse_register(parts[1])
        imm8 = parse_immediate(parts[2])
        opcode = 0b10011

        machine_code = (opcode << 11) | (rt << 8) | ((imm8 >> 2) & 0xFF)


    # ------- ADD -------
    elif mnemonic == 'ADD':
        imm7 = parse_immediate(parts[1])
        opcode = 0b101100000

        machine_code = (opcode << 7) | imm7


    # ------- SUB -------
    elif mnemonic == 'SUB':
        imm7 = parse_immediate(parts[1])
        opcode = 0b101100001

        machine_code = (opcode << 7) | imm7


    # ------- BEQ -------
    elif mnemonic == 'BEQ':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11010000

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BNE -------
    elif mnemonic == 'BNE':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11010001

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BCS -------
    elif mnemonic == 'BCS':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11010010

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BCC -------
    elif mnemonic == 'BCC':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11010011

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BMI -------
    elif mnemonic == 'BMI':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11010100

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BPL -------
    elif mnemonic == 'BPL':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11010101

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BVS -------
    elif mnemonic == 'BVS':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11010110

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BVC -------
    elif mnemonic == 'BVC':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11010111

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BHI -------
    elif mnemonic == 'BHI':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11011000

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BLS -------
    elif mnemonic == 'BLS':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11011001

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BGE -------
    elif mnemonic == 'BGE':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11011010

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BLT -------
    elif mnemonic == 'BLT':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11011011

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BGT -------
    elif mnemonic == 'BGT':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11011100

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- BLE -------
    elif mnemonic == 'BLE':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11011101

        machine_code = (opcode << 8) | (imm8 & 0xFF)


    # ------- B or BAL -------
    elif mnemonic == 'BAL' or mnemonic == 'B':
        imm8 = parse_immediate(parts[1])
        opcode = 0b11011110

        machine_code = (opcode << 8) | (imm8 & 0xFF)

    else:
        print(f"Instruction inconnue ou format incorrect : {line}")
        return None

    # Retourne le code hexadécimal formaté sur 4 chiffres (ex: '2005')
    return f"{machine_code:04x}"


# --- Programme principal ---
source_code = """
MOVS R0, #5       ; Charge 5 dans R0
MOVS R1, #3       ; Charge 3 dans R1
ADDS R2, R0, R1   ; R2 = R0 + R1
LSLS R3, R0, #1   ; R3 = R0 << 1
"""

source_code = """
; Programme de test complet pour le processeur PARM
; Teste: Arithmétique, Décalages, Mémoire, Comparaisons, Branchements

MOVS R0, #5       ; Charge 5 dans R0
MOVS R1, #3       ; Charge 3 dans R1
ADDS R2, R0, R1   ; R2 = R0 + R1 = 8
LSLS R3, R2, #1   ; R3 = R2 << 1 = 16
SUBS R3, R3, #1   ; R3 = R3 - 1 = 15
STR R3, [SP, #4]  ; Stocke 15 à l'adresse SP+4
LDR R4, [SP, #4]  ; Recharge 15 dans R4 depuis la mémoire
CMP R3, R4        ; Compare R3 (15) et R4 (15) -> Flag Z=1
BEQ -7            ; Si Egal (Z=1), saute en arrière vers SUBS (Boucle infinie)
"""

print("v2.0 raw")  # En-tête obligatoire pour Logisim
for line in source_code.strip().split('\n'):
    hex_code = assemble_line(line)
    if hex_code:
        print(hex_code, end=" ")

# Résultat : 2005 2103 1842 0053 1e5b 9301 9c01 42a3 d0f9