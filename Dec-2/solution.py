def star_1():
    with open('input.txt') as f:
        lines = f.readlines()
    
    no_games = [x.split(':')[1].strip() for x in lines]
    all_handfalls = [x.split(';') for x in no_games]
    
    possible = []
    for i, game in enumerate(all_handfalls):
        possible_game = i + 1
        most_of_cols = {'red': 0, 'green': 0, 'blue': 0}
        max_cols = {'red': 12, 'green': 13, 'blue': 14}
        for handfall in game:
            handfull = handfall.strip()
            for colour_num in handfull.split(','):
                colour_num = colour_num.strip()
                colour = colour_num.split(' ')[1]
                num = int(colour_num.split(' ')[0])
                most_of_cols[colour] = most_of_cols.get(colour) if num < most_of_cols.get(colour) else num
        
        truths = [max_cols.get(k) < v for k,v in most_of_cols.items()]
        if not any(truths):
            possible.append(possible_game)
          
    return sum(possible)


    
def star_2():
    with open('input.txt') as f:
        lines = f.readlines()
    
    no_games = [x.split(':')[1].strip() for x in lines]
    all_handfalls = [x.split(';') for x in no_games]
    
    powers = []
    for game in all_handfalls:
        most_of_cols = {'red': 0, 'green': 0, 'blue': 0}
        for handfall in game:
            handfull = handfall.strip()
            for colour_num in handfull.split(','):
                colour_num = colour_num.strip()
                colour = colour_num.split(' ')[1]
                num = int(colour_num.split(' ')[0])
                most_of_cols[colour] = most_of_cols.get(colour) if num < most_of_cols.get(colour) else num
        
        power = 1
        for v in most_of_cols.values():
            power = power * v
        powers.append(power)
    
    return sum(powers)
    
print(star_2())