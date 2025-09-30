def word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
    return count

def char_count(path_to_file):
    char_dic = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        l_file_contents = file_contents.lower()
        char_list = list(l_file_contents)
        for char in char_list:
            if char in char_dic:
                char_dic[char] += 1
            else:
                char_dic[char] = 1
    return char_dic
 
def sort_on(items):
    return items["num"]

def list_conv(char_dic):
    list_dic = []
    for char in char_dic:
        list_dic.append({"char": char, "num": char_dic[char]})
    list_dic.sort(reverse=True, key=sort_on)
    return list_dic