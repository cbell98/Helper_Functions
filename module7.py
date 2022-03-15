# Building Arrays

# Create a 2D array of size row_count x col_count. Fill the array with 0.
def make_row(col_count):
    
    row = []
    
    for j in range(col_count):
        row.append(0)
    
    return row

def solution(row_count, col_count):
    
    result = []
    
    for i in range(row_count):
        row = make_row(col_count)
        result.append(row)
    
    return result

  
# Create a 2D array of size row_count x col_count. Fill the array with 0.
# (Another way)
def solution(row_count, col_count):
    
    result = []
    
    for i in range(row_count):
        
        row = []
        
        for j in range(col_count):
            row.append(0)
            
        result.append(row)
    
    return result


# 
