katz_deli = ["Alice", "Bob", "Charlie"]

def line():
    pass
    if not katz_deli:
       print("The line is currently empty.")
    else:
        current_line = "The line is currently: "
        current_line += ''.join([f" {index + 1}. {name}" for index, name in enumerate(katz_deli)])
        print(current_line)
