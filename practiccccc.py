re_string = list(map(int, input("Reference string: ").split())) 
frame = int(input(" total frame: "))

memory =[""]*frame  # Frame sequence

page_fault = 0
total_hit = 0

print("Formating---")

while re_string != []:
    if " " in memory:
        x = re_string.pop(0)
        if x in memory:
            total_hit += 1
             #print("---- ")
        else:
            page_fault += 1
            i = memory.index(" ")
            memory[i] = x
        print(memory)
    else:
        x = re_string.pop(0)
        if x in memory:
            total_hit += 1
        else:
            page_fault += 1
            y = []
            for frame in memory:
                try:
                    y.append(re_string.index(frame))
                except ValueError:
                    y.append(len(re_string))
            farthest_index = y.index(max(y))
            memory[farthest_index] = x
        print(memory)

print(f"\nPage Miss: {page_fault}")
print(f"Page Hit : {total_hit}")

