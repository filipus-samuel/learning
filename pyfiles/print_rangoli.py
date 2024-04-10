inp = int(input("Input number: "))
middle = inp
start = chr(97)
end = chr(97 + inp - 1)
print(f"Create pattern using {start} to {end}")
reversed_dict = []
total_row = (inp * 2) - 1
total_col = (inp * 4) - 3
all_temp = []

for x in range(1, middle + 1):
    chars_dict = {}
    for y in range(1, x + 1):  # for 1 in range(1, 3):
        if y == x + 1 - 1:  # if 1 == 3-1
            last_char = chr(97 + middle - y)
            chars_dict[last_char] = 1
        else:
            char_nth = chr(97 + middle - y)
            chars_dict[char_nth] = 2

    temp = []
    f_ss = []
    l_ss = []
    m_ss = []
    for k, v in chars_dict.items():
        for i in range(1, v + 1):
            if v == 1:
                m_s = k
                m_ss.append(m_s)
            else:
                if i == 1:
                    f_s = f"{k}-"
                    f_ss.append(f_s)
                elif i == 2:
                    l_s = f"-{k}"
                    l_ss.insert(0, l_s)
        temp = f_ss + m_ss + l_ss
        temp_str = "".join(temp)
    if len(chars_dict) == inp:
        all_temp.append(temp_str)
    else:
        temp_str_len = len(temp_str)
        total_dash_per_side = int((total_col - temp_str_len) / 2)
        dashes = ""
        for i in range(total_dash_per_side):
            dashes += "-"
        temp_str_2 = dashes + temp_str + dashes
        all_temp.append(temp_str_2)
        reversed_dict.insert(0, temp_str_2)

for d in reversed_dict:
    all_temp.append(d)

last_product = "\n".join(all_temp)
print(last_product)
