multiplo = input().split()
A = int(multiplo[0])
B = int(multiplo[1])
if A > B:
    if A % B == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if A < B:
    if B % A == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if A == B:
    print('Sao Multiplos')