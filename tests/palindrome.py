def make_palindrome(s):
    if s == s[::-1]:
        return s
    if s[0] == s[-1]:
        return s[0] + make_palindrome(s[1:-1]) + s[-1]
    else:
        s1 = s[0] + make_palindrome(s[1:]) + s[0]
        s2 = s[-1] + make_palindrome(s[:-1]) + s[-1]
        if len(s1) > len(s2):
            return s2
        else:
            return s1




    
# This implementation first checks if the input string is already a palindrome

# Otherwise, it checks if the first and last characters of the string are equal. 
# If they are, it recursively calls the function on the substring between the first and last characters, 
# and concatenates the first and last characters to the result.


# If they are not equal, it recursively calls the function on two substrings: 
# one that starts from the second character of the string, 
# and one that ends at the second to last character of the string. 
# It then concatenates the first character of the string to the result of the first recursive call, 
# and concatenates the last character of the string to the result of the second recursive call. 
# Finally, it returns the shorter of the two resulting strings.










def test_make_palindrome_solution():
    assert make_palindrome('abcdc') == 'abcdcba'
    assert make_palindrome('ababab') == 'abababa'
    assert make_palindrome('bccaaac') == 'bccaaaccb'
