def do_twice(c,l,do_twice2):
    c()
    l()
    do_twice2(c,l)
def do_twice2(c,l):
    l()
def colunas():
    print("+ - - - - + - - - - +")
def linhas():
    print("|         |         |")
    print("|         |         |")
    print("|         |         |")
    print("|         |         |")
    print("+ - - - - + - - - - +")
do_twice(colunas,linhas,do_twice2)