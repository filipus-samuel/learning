def carpet(n, m):
    middle = int((n + 1) / 2)
    mat_design = ""
    temp_list = []
    add_on = 0
    for x in range(1, middle + 1):
        if x == middle:
            welcome_pattern = "WELCOME"
            welcome_pattern_len = len(welcome_pattern)
            dash_len = int((m - welcome_pattern_len) / 2)
            dashes = ""
            for i in range(dash_len):
                dashes += "-"
            welcome_line = dashes + welcome_pattern + dashes
            mat_design += welcome_line + "\n"
        else:
            mat_pattern = ".|."

            loop = x + add_on
            for w in range(1, loop):
                mat_pattern += ".|."
            mat_pattern_len = len(mat_pattern)
            dash_len = int((m - mat_pattern_len) / 2)
            dashes = ""
            for i in range(dash_len):
                dashes += "-"
            design_line = dashes + mat_pattern + dashes
            mat_design += design_line + "\n"
            temp_list.append(design_line)
            add_on += 1

    for i in range(1, len(temp_list) + 1):
        mat_design += temp_list[len(temp_list) - i] + "\n"
    mat_design = mat_design[:-1]  # remove last \n
    return mat_design


inp = input("Input size: ").split("x")
n = int(inp[0])
m = int(inp[1])

design = carpet(n, m)
print(design)
