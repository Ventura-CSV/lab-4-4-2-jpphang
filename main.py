def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    while True:
        user_input = int(input("Enter a number"))
        
        try:
            number = user_input
        
        except ValueError:
            print("input must be numeric")
            
        else: print(number)
        
        break
        
            

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
