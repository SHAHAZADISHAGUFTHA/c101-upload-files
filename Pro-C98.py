def swapFilesData():
    filename = input("Enter Your 1st File Name:-")
    filename = input("Enter Your 2nd File Name:-")
    with open("sample2.txt",'r') as a :
        data_a = a.read()
        
    with open("sample1.txt",'r') as b :
        data_b = b.read()
       
    with open("sample2.txt",'w') as c :
        c.write(data_b)
    with open("sample1.txt",'w') as d :
        d.write(data_a)

swapFilesData()