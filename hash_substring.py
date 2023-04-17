# python3

def read_input():
    text = input()
    if 'I' in text:
       pattern = str(input("input pattern: "))
       text = str(input("input text: "))
       pattern = pattern.rstrip()
       text = text.rstrip()
    elif "F" in text:
       with open("tests/06") as file:
            pattern = file.readline()
            text = file.readline()
            pattern = pattern.rstrip()
            text = text.rstrip()
    return pattern, text
            
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    compare_pattern = ""
    hash = 0
    output = []
    j = len(pattern)
    for i in pattern:
        hash = hash + ord(i)**j*2
        j -= 1
    for a in range(len(text)):
        j = len(pattern)
        compare_pattern = text[a:a+len(pattern)]
        compare_hash = 0
        for b in compare_pattern:
            compare_hash = compare_hash + ord(b)**j*2
            j -= 1
        if hash == compare_hash:
            output.append(a)
        compare_pattern = ""


    # and return an iterable variable
    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

