#Global scope
x='global x'

def function():
    #Local scope
    x='local x'

function()
print(x)