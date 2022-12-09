
isDebug = False
test = "default"

print("loaded util")

def debugPrint(str):
    if(isDebug):
        print(str)

def count(dict_in, value):
    if value in dict_in:
        dict_in[value] += 1
    else: 
        dict_in[value] = 1
        
    return dict_in
    
def toCountDict(list_in):
    result = {}
    for item in list_in:
        count(result, item)
        
    return result