#substituto para IFs, ELIFs e ELSEs

dia= 5

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case "1":
        print("str")
    case _:
        print("erro")

print("="*2)
n=300
m=n

print(n!=m)