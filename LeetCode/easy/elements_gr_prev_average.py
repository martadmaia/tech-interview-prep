def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) > 1:
        current_sum = 0
        valid_elements = 0
        
        for i in range(1, len(responseTimes)):
            current_sum += responseTimes[i-1]
            if responseTimes[i] > current_sum / i:
                valid_elements += 1
        
        return valid_elements       
        
    return 0