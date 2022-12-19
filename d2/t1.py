import fileinput

SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

MOVES_MAP = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

WIN_MAP = {
    "X": "Z",
    "Y": "X",
    "Z": "Y",
}

def get_round_points(round, use_map):
    if use_map:
        opponent_move = MOVES_MAP[round[0]]
    else:
        opponent_move = round[0]
    my_move = round[-1]

    if opponent_move == my_move:
        return SCORES[my_move] + 3
    
    if WIN_MAP[my_move] == opponent_move:
        return SCORES[my_move] + 6

    return SCORES[my_move]

def get_proper_move(round):
    opponent_move = MOVES_MAP[round[0]]
    outcome = round[-1]
    match outcome:
        case "X":
            return opponent_move + WIN_MAP[opponent_move]
        case "Y":
            return opponent_move + opponent_move
        case "Z":
            for key, value in WIN_MAP.items():
                if value == opponent_move:
                    my_move = key
            return opponent_move + my_move

if __name__ == "__main__":
    rounds = [line.strip() for line in fileinput.input(files="d2/input/input.txt")]
    # PART 1
    score = 0
    for round in rounds:
        score += get_round_points(round, True)
    print(score)

    # PART 2
    score = 0
    for round in rounds:
        score += get_round_points(get_proper_move(round), False)
    print(score) 