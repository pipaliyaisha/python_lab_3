class firstname:
    def getdata(self):
        print("isha")

class lastname:
    def retrivedata(self):
        print("pipaliya")

class fullname(firstname, lastname):
    pass
print("--full name is--")
b1 = fullname()

b1.getdata()
b1.retrivedata()