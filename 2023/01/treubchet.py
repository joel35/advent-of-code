FILE = 'sample_2.txt'

with open(FILE) as f_in:
    input = [line.strip() for line in f_in]

# part_1 = []
# for line in input:
#     digits = [char
#                 for char in line 
#                 if char.isnumeric()]

#     num = int(digits[0] + digits[-1])
#     part_1.append(num)

# print(f'Part 1: {sum(part_1)}')


part_2 = []

spelled = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

number_key = {word : i for i, word in enumerate(spelled)}
number_key.update({str(val) : val for val in range(10)})
print(number_key)



for line in input:
    print(line)

    nums = []

    buffer = []

    left = 0
    right = 1

    while left < len(line):
        chars = line[left:right]
        check = ''.join(chars)
        print(chars)

        if check in number_key:
            left = right
        
        right += 1


    
