def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    while True:
        user_input = input("Enter a number:")
        
        try:
            number = float(user_input)
        
        except ValueError:
            print("Input Must Be Numeric")
            
        else: print(number)
        
        break
        
            

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
