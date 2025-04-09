from lib.includes_todo import *

# test - to do pass

def test_includes_todo():
    result = includes_todo("Walk dog #TODO")
    assert result == True

#test to do fail

def test_does_not_include_todo():
    result = includes_todo("Walk dog")
    assert result == False