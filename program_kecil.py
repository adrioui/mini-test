def generate_number_string():
    result = []  # Use a list to store the modified numbers

    for number in range(100, 0, -1):  # Iterate over the numbers in reverse order
        if number % 3 == 0 and number % 5 == 0:
            result.append("FooBar")  # Append "FooBar" if divisible by both 3 and 5
        elif number % 3 == 0:
            result.append("Foo")  # Append "Foo" if divisible by 3
        elif number % 5 == 0:
            result.append("Bar")  # Append "Bar" if divisible by 5
        elif number > 1:
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                continue  # Skip prime numbers
        else:
            result.append(str(number))  # Append the number as a string

    return ", ".join(result)  # Join the modified numbers with commas

number_string = generate_number_string()  # Generate the modified number string
print(number_string)  # Print the modified numbers without new lines
