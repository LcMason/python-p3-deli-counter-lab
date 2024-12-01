katz_deli = ["Alice", "Bob", "Charlie"]
# katz_deli = []

def line(katz_deli):
    pass
    if not katz_deli:
       print("The line is currently empty.")
    else:
        current_line = "The line is currently:"
        current_line += ''.join([f" {index + 1}. {name}" for index, name in enumerate(katz_deli)])
        print(current_line)


def take_a_number(katz_deli, name):
    pass
    katz_deli.append(name)
    posiiton = len(katz_deli)
    print(f"Welcome, {name}. You are number {posiiton} in line.")


def now_serving(katz_deli):
    pass
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        name = katz_deli.pop(0)
        print(f"Currently serving {name}.")
