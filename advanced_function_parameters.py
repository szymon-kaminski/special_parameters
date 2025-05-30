### Demonstrates a positional-only parameter using the '/' symbol.
def greet(name, /):
    print(f"Hello {name}!")

greet("Szymon")
# greet("name=Szymon") # This would raise an error!


### Demonstrates a keyword-only parameter using the '*' symbol.
def show_age(*, age):
    print(f"You are {age} years old.")

show_age(age=35)
# show_age(35)  # This would raise an error!