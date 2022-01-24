def project():
    file1 = input("Enter your first file name")
    file2 = input("Enter your second file name")

    mighty=open(file1,'r')
    data_mighty =mighty.read()
    
    Justy=open(file2,'r')
    data_Justy =Justy.read()

    mighty=open(file1,'w')
    mighty.write(data_Justy)

    Justy=open(file2,'w')
    Justy.write(data_mighty)
    
