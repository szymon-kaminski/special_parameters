### Demonstrates a positional-only parameter using the '/' symbol.
def greet(name, /):
    print(f"Hello {name}!")

greet("Szymon")
# greet("name=Szymon") # This would raise an error!

print()
### Demonstrates a keyword-only parameter using the '*' symbol.
def show_age(*, age):
    print(f"You are {age} years old.")

show_age(age=35)
# show_age(35)  # This would raise an error!
print()

### Demonstrates arbitrary positional arguments using '*args'.
def print_numbers(*numbers):
    print("Numbers provided: ", numbers)

print_numbers(1, 2, 3, 4)
#print_numbers()  # Also valid, prints an empty tuple
print()

### Demonstrates arbitrary keyword arguments using '**kwargs'.
def print_profile(**info):
    print("Profile information:")
    for key, value in info.items():
        print(f"{key}: {value}")
    
print_profile(name="Szymon", age=35, city="Pszczyna")
