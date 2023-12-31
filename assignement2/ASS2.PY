def read_file(file_name):
   
    with open (file_name,'r') as file:
        content=file.read()
        print(content)
    return content

    raise NotImplementedError()

def read_file_into_list(file_name):
   
    with open (file_name,'r') as file:
        content=file.readlines()
        
        return content

    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
   
    contents1=file_contents.split("\n")[0]
    
    with open(output_filename,'w') as file:
       file.writelines(contents1)
    return

    raise NotImplementedError()


def read_even_numbered_lines(file_name):
  
    with open (file_name,'r') as file:
        content=file.readlines()
        
        f_new=[]
        for i in range (1, len(content),2):
            f_new.append(content[i])
    return f_new


    raise NotImplementedError()

def read_file_in_reverse(file_name):
   
    with open (file_name,'r') as file:
        content=file.readlines()
  
        f_new=[]
        for i in reversed(range (len(content))):
            f_new.append(content[i])
    return f_new


    raise NotImplementedError()


def main():
    file_contents = read_file("pppt.txt")
    print(read_file_into_list("pppt.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("pppt.txt"))
    print(read_file_in_reverse("pppt.txt"))

if __name__ == "__main__":
    main()