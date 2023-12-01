import re

def star1():
    with open("input.txt") as f:
        lines = f.readlines()

    output = []
    for line in lines:
        first=''
        last=''
        found = False
        i=0
        while not found :
            f = line[i].isdigit()
            l = line[(i+1)*-1].isdigit()
            
            if len(first) == 0 and f:
                first = line[i]
                
            if len(last) == 0 and l:
                last = line[(i+1)*-1]
            
            if len(first) != 0 and len(last) != 0:
                found = True
            i+=1
        
        output.append(int(first+last))
        
    return output

def star2():
    with open("input2.txt") as f:
        lines = f.readlines()
        
    integer_indexes, integer_overall = star2_2()
            
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums = []
    for j, line in enumerate(lines):
        if any(substring in line for substring in numbers):
            numbers_to_find = [substring in line for substring in numbers]
            numbers_found = [numbers[x] for x in range(len(numbers_to_find)) if numbers_to_find[x]]
            
            high = -1
            high_str = ''
            low = 99
            low_str = ''
            for number in numbers_found:
                idxs = [x.start() for x in  re.finditer(number, line)]
                for idx in idxs:
                    if idx > high:
                        high = int(idx)
                        high_str = number
                    
                    if idx < low:
                        low = idx
                        low_str = number
                        
            high_int = high if high > max(integer_indexes[j]) else line[max(integer_indexes[j])]
            if high_int == high:
                to_pick_h = numbers.index(high_str) + 1
            else:
                to_pick_h = high_int
                
            low_int = low if low < min(integer_indexes[j]) else line[min(integer_indexes[j])]
            if low_int == low:
                to_pick_l = numbers.index(low_str) + 1
            else:
                to_pick_l = low_int
            nums.append(int(str(to_pick_l) + str(to_pick_h)))
        else:
            nums.append(integer_overall[j])
    return sum(nums)
            
            
                
    
def star2_2():
    with open("input2.txt") as f:
        lines = f.readlines()

    output = []
    indexes = []
    for line in lines:
        first=''
        firsti = ''
        last=''
        lasti = ''
        found = False
        i=0
        while not found :
            f = line[i].isdigit()
            l = line[(i+1)*-1].isdigit()
            
            if len(first) == 0 and f:
                first = line[i]
                firsti = i
                
                
            if len(last) == 0 and l:
                last = line[(i+1)*-1]
                lasti = len(line) + ((i+1)*-1)
            
            if len(first) != 0 and len(last) != 0:
                found = True
            i+=1
        
        indexes.append([int(firsti), int(lasti)])
        output.append(int(first+last))
        
    return indexes, output
print(star2())