def capitalize_words(input_string):
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)
    return result

# Example usage:
input_string = "this is a new string"
result = capitalize_words(input_string)
print(result)
