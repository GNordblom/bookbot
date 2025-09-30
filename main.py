import sys
from stats import word_count
from stats import char_count
from stats import list_conv

def main():
    try:
       sys.argv[1] != None
    except Exception as e:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

    #text = get_book_text('books/frankenstein.txt')
    #print(text)
    book_path = sys.argv[1]
    num_word = word_count(book_path)
    #print(f"Found {num_word} total words")
    chars = char_count(book_path)
    #print(chars)
    conv_list= list_conv(chars)
    #print(conv_list[1]["char"])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")
    for i in range(0, len(conv_list)):
      if conv_list[i]["char"].isalpha() == True:
        print(f"{conv_list[i]["char"]}: {conv_list[i]["num"]}")
    print("============= END ===============")
main()