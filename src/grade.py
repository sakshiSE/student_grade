def main():
    marks=[]
    print("enter the marks for the 5 subjects :")

    for i in range(5):
       marks.append(int(input("enter the marks:")))

    total=0
    for m in marks:
        total=total+m

    average=total/5
    result=grades(average)

    print("Average : ",average)
    print("Grade : ",result) 

def grades(average):
    if average >=90 :
        return "A+"

    elif average >= 75:
        return "A" 

    elif average >= 60: 
        return "B"
        
    elif average >= 50:
        return "C"
        
    else :
        return "Fail"







if __name__ =="__main__":
    main()