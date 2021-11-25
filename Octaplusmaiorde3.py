print('Digite três numeros, para saber')

A=int(input('digie o valor A:'))
B=int(input('digie o valor B:'))
C=int(input('digie o valor C:'))

def verifica():
    if (A>B and A>C):
        print('O valor A é o maior')
    if (B>A and B>C):
        print ('O valor B é o maior')
    if (C>A  and C>B):
        print ('o valor C é o maior')


def main():
    verifica()

main()
