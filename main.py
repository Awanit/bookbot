def char_count(text):
    char_dict = {}
    lower_text = text.lower()
    
    for char in lower_text:
        if char.isalpha():  # Count only letters
            # Use dict.get() to fetch the current count or default to 0
            char_dict[char] = char_dict.get(char, 0) + 1
    
    return char_dict
        
def words_count(text):
    words = text.split()
    return len(words)

def main():
    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read() 
        # Word count
    
        w_count = words_count(file_contents)
    
        # Character count
        c_count = char_count(file_contents)
    
        # Convert the dictionary to a list of tuples and sort it in place by frequency (descending order)
        sorted_char_count = list(c_count.items())
    
        # Sort in place by character count in descending order
        sorted_char_count.sort(reverse=True, key=lambda item: item[1])

        print(f"--- Begin report of {file_path} ---")
        print(f"{w_count} words found in the document\n")
    
        for char, count in sorted_char_count:
            print(f"The '{char}' character was found {count} times")
    
        print(f"--- End report ---")
if __name__ == "__main__":
    main()
