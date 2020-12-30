# String Split and Join

def split_and_join(line):
    # write your code here
    words = line.split(" ")
    sentence = "-".join(words)
    return sentence
    # return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
