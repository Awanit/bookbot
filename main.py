def main():
    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)
if __name__ == "__main__":
    main()
