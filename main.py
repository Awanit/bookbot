def words_count(text):
    words = text.split()
    return len(words)

def main():
    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)
        count = words_count(file_contents)
        print(count)
if __name__ == "__main__":
    main()
