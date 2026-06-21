print("\tWord Frequency Analyzer")

def read_text():
    fname = input("Enter the name of the file to read: ")
    try:
        with open(fname, "r") as f:
            return f.read()
            if data == "":
                raise EmptyError
    except FileNotFoundError:
        print("File does not exist!!")
    except Exception as e:
        print("Error: ",e)
    

def clean_text(data):
    return "".join(ch for ch in data if ch.isalnum() or ch ==" " or ch == "\n")


def count_words(words):
    count = {}
    for word in words:
        count[word] = count.get(word, 0) +1
    return count

def display_count_data(words, count):
    if not words:
        print("No valid words found in the file.")
        return

    sorted_list = sorted(count.items(), key = lambda item: item[1], reverse = True)

    for word, frequency in sorted_list: 
        print(f"{word:<15}: {frequency}")

    print("Total words: ", len(words))
    print("Unique words: ", len(count))

    max_count = sorted_list[0][1]
    frequent = [word[0] for word in sorted_list if word[1] == max_count]

    print("Most frequent word:", ", ".join(frequent), f"({max_count} times)" )


def main():
    data = read_text()
    if not data:
        return
    
    cleaned_text = clean_text(data)
    words = cleaned_text.lower().split()
    counts = count_words(words)
    display_count_data(words, counts)

main()
        
