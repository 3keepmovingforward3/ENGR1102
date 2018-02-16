from task import books_collections

books = ['Calculus','History','Circuits','the adventures of tom sawyer']
ans = ["I have my Calculus book.","I have my History book.","I have my Circuits book.","I don't have that book."]
for i in range(len(books)):
    if books_collections(books[i])==ans[i]:
        print("Test Case " + str(i) +" Passed")