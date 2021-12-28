

with open("14.txt", "r") as f:
    content = f.read()

template = content.split("\n")[0]

instructionText = content.split("\n")[2:]

instructions = {}

for i in instructionText:
    key = i[0:2]
    value = i[6]
    instructions[key] = value

def insert(char, index, string):
    return string[0:index] + char + string[index:]

def step(polymer):
    additives = ""
    for i in range(len(polymer)-1):
        code = polymer[i:i+2]
        additives += instructions[code]

    for index, additive in enumerate(additives):
        polymer = insert(additive, (index*2)+1, polymer)

    return polymer

for x in range(40):
    print(x)
    template = step(template)
    print(template)
    if x == 9: 
        part_1_template = template
        break # TODO don't break after optimizing

part_2_template = template

part_1_most_common = max(part_1_template, key = template.count)
part_1_least_common = min(part_1_template, key = template.count)

part_2_most_common = max(part_2_template, key = template.count)
part_2_least_common = min(part_2_template, key = template.count)

print("Part 1:", template.count(part_1_most_common) - template.count(part_1_least_common))
print("Part 2:", template.count(part_2_most_common) - template.count(part_2_least_common))