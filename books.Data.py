import pickle

def createFile():
    file = open("books.dat","ab")
    Title = input("Enter title: ").lower()
    Id = int(input("Enter book number: "))
    Category = input("Enter book category: ").lower()
    Author = input("Enter author: ").lower()
   
    
    record = [Title, Id, Category, Author]
    pickle.dump(record, file)
    # file.close()

def countRec(Author):
    file = open("books.dat","rb")
    count = 0
    try:
        while True:
            record = pickle.load(file)
            if record[2]==Author:
                count+=1
    except EOFError:
        pass
    return count
    # file.close()

#To test working of functions
def testProgram():
    while True:
        createFile()
        choice = input("Add more record (y/n)? ")
        if choice in 'n':
            break
#     Author = input('Enter author name to search: ')
#     n = countRec(Author)
#     print("No of books are",n)

testProgram()    