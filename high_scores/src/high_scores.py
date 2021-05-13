def latest(scores):
    length = len(scores)
    return scores[length - 1]

def personal_best(scores):
    best_score = 0
    for score in scores:
        if score > best_score:
            best_score = score
    return best_score

def personal_top_three(scores):
    scores.sort(reverse = True)
    return scores[0: 3]

def highest_to_lowest(scores):
    scores.sort(reverse = True)
    return scores