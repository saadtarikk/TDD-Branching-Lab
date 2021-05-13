def get_result(final_score):

    if final_score["home_score"] > final_score["away_score"]:
        return "Home win"

    elif final_score["home_score"] == final_score["away_score"]:
        return "Draw"    
    else:
        final_score["home_score"] < final_score["away_score"]
        return "Away win"

def get_results(final_scores):
    results = []
    for final_score in final_scores:
        if get_result(final_score):
            results.append(final_scores)
    return results

#     # (You could try and use a list comprehension for this)
#    

