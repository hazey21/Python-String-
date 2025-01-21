#Function to authorize a valid code
def valid_codes(code):
    #Intializing valid code characteristics
    length = len(code) >=10
    thedigit = code[3:7].isdigit()
    uppercase = code[9].isupper() 
    
    return length and thedigit and uppercase

#Function to authorize a restricted code
def restricted_code(code): 
    return code[9] == "R" and int(code[3 : 7]) >=2000        
    
def main():
    #Intialize lists
    valid_list = []
    invalid_list = []
    restricted_list = []
    
    try: 
        #Opening file and read all lines. 
        with open("A3 Codes.txt", "r") as infile:
            lines = infile.readlines()
    
        #Stripping the codes and added them to the appropriate lists
        for ch in lines:
            code = ch.strip()
            if valid_codes(code):
                valid_list.append(code)
                if restricted_code(code): 
                    restricted_list.append(code)
            else: 
                invalid_list.append(code)
                
        #Printing results of valid list
        if valid_list: 
            print("Valid Code(s) are: ")
            for code in valid_list: 
                print(code)
        
        #Printing results of invalid list
        if invalid_list: 
            print("\nInvalid Code(s) are: ")
            for code in invalid_list:
                print(code)
            
        #Printing results of restricted list
        if restricted_list: 
            print("\nInvalid Restricted Code(s) are: ")
            for code in restricted_list:
                print(code)
    
    #Catch error of FileNotFoundError
    except FileNotFoundError:
        print("The file was not found")

#Call the main function
if __name__ == "__main__":
     main()        