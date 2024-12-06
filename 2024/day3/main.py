import re
stack = []

r = 0

with open("input3", "r", encoding="utf-8") as file:
   
    o = file.read()

    res = re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", o)
    print(res)
    on = True
    for i in res:
        mul, d, dd = i

        if d:
            on = True
        elif dd:
            on = False
        elif mul:
            m1, m2 = mul.strip("mul(").strip(")").split(",")
    
            if on:
                r += int(m1) * int(m2)
print(r)
