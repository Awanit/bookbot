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
        print(file_contents)
        w_count = words_count(file_contents)
        print(w_count)
        c_count = char_count(file_contents)
        print(c_count)
if __name__ == "__main__":
    main()
