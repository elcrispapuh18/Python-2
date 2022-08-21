from ast import Num


def divisors(Num):
    divisors=[]
    for i in range(1,Num+1):
        if Num%i==0:
            divisors.append(i)
    return divisors

    def run ():
    Num=input("Ingrese un número: ")
    assert num.isnumeric(),"Debes ingresar un número"
    print(divisors(int(num)))
    print("Termino mi programa")


if __name__ == '__main__':
    run() 

