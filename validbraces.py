def validBraces(string):

    open_braces = ["(", "[", "{"]
    braces_dictionary = {
        "(" : ")",
        "{" : "}",
        "[" : "]"  
    }
    
    open_brace_in_string = []
    closed_brace_in_string = []

    for i in range(len(string)):
        if string[i] in open_braces:
            open_brace_in_string.append(i)
        else:
            closed_brace_in_string.append(i)
    
    if len(open_brace_in_string) == 0:
        return False
    if len(closed_brace_in_string) == 0:
        return False
    
    for i in open_brace_in_string:
        current_closing_brace = braces_dictionary[string[i]]
        for y in closed_brace_in_string:
            if string[y] == current_closing_brace:
                if y - i == 1:
                    validity = True
                    break
            else:
                validity = False
    return validity

validBraces("([{}])")