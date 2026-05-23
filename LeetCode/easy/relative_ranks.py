def findRelativeRanks(score):

    map_elements = {score[i]:i for i in range(len(score))}
    
    sorted_scores = sorted(score, reverse=True)

    map_elements_2 = {sorted_scores[i]:i + 1 for i in range(len(score))}

    

    for i in range(len(score)):
        match map_elements_2[score[i]]:
            case 1:
                score[i] = "Gold Medal"
            case 2:
                score[i] = "Silver Medal"
            case 3:
                score[i] = "Bronze Medal"
            case _:
                score[i] = map_elements_2[score[i]]

    return score


def findRelativeRanks2(score):

    sorted_scores = sorted(score, reverse=True)

    for index, val in enumerate(score):
        if sorted_scores.index(val) == 0:
            score[index] = "Gold Medal"
        elif sorted_scores.index(val) == 1:
            score[index] = "Silver Medal"
        elif sorted_scores.index(val) == 2:
            score[index] = "Bronze Medal"
        else:
            score[index] = sorted_scores.index(val) + 1


    return score

            
        

        
        
            
        
        

    


print(findRelativeRanks2([189, 100, 200]))