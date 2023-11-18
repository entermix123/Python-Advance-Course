def palindrome(word, star_idx, end_idx=-1):         # create function, set start_idx, and set end idx as -1

    if star_idx == len(word)//2:                    # is current index middle of the word?
        return f'{word} is a palindrome'            # if it is, the word is palindrome

    if word[star_idx] != word[end_idx]:             # is letter of current start index is same as letter of end index?
        return f'{word} is not a palindrome'        # if it is not, the word is not a palindrome

    # use palindrome function to change start and end index of the letters in the word, used as a recursion!
    # start to return values only when one of the 'if' conditions are true, otherwise keep adding to start and end idx
    # return result to the state who called last! That many doors you go true when enter, that many door you have to go true to exit
    return palindrome(word, star_idx + 1, end_idx - 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
