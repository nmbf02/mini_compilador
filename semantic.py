# semantic.py

def validate_instruction(instr):
    instr_type = instr[0]
    params = instr[1:]

    if instr_type in ("PAPER", "PEN"):
        if not (0 <= params[0] <= 100):
            return f"Error semántico: valor de {instr_type} fuera de rango (0-100): {params[0]}"

    elif instr_type == "LINE":
        if len(params) != 4:
            return "Error semántico: LINE requiere 4 parámetros"
        for val in params:
            if val < 0:
                return f"Error semántico: coordenada negativa en LINE: {val}"

    return None  # Sin errores
