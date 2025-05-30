# Demonstrates a positional-only parameter using the '/' symbol.
def greet(name, /):
    print(f"Hello {name}!")

greet("Szymon")
# greet("name=Szymon") # This would raise an error!

