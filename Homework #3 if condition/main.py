def compare(a,b,c):
    a,b,c=int(a),int(b),int(c)
    if a == b or b == c or a == c:
        return True
    return False
    
    
print(compare("2",3,2))