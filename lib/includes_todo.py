# As a user
# So that I can find my tasks among all 
# my notes
# I want to check if a line from my notes 
# includes the string `#TODO`.

# Function name - includes_todo()

# Parameters - one string

# Returns - boolean

def includes_todo(string):
    if "#TODO" in string:
        return True
    return False