def main(s):
    """
    A str containing the letter "a" is given. Find the number of letters "a" in this variable.
    Args:
        s: str
    Returns:
        int: answer
    """
    ans = 0
    for i in s:
        if i=='a':
            ans+=1        
    return ans
print(main("google is a search engine"))