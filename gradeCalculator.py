def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you
    try:
        hrs = float(input("Enter score:"))
        
    except ValueError:

        try:
            ival = int(hrs)
        except:
            ival = -1
        
        if ival < 0:
            print("Bad score")
        
            

    if hrs > 1:

        print("Bad score")
    else:
        if hrs >= .9:
                print("A")

        elif hrs >= .8:
                print("B")

        elif hrs >= .7:
                print("C")
            
        elif hrs >= .6:
                print("D")
            
        elif hrs < .6:
                print("F")
        

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
