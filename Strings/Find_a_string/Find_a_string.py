def count_substring(string, sub_string):

    contador = 0
    sub_size = len(sub_string)
    
    for i in range(len(string)):
        if string[i:i+sub_size] == sub_string:
            contador +=1
            
    return contador

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)