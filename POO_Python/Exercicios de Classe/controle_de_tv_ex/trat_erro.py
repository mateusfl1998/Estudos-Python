from time import sleep

def inputer(texto):
    while True:
        try:
            sleep(1)
            op = int(input(texto))
        except ValueError:
            sleep(2)
            print('Digite uma opção válida!')
        else:
            if op > 3 or op < 1:
                print('Digite uma opção válida!')
            else: 
                return op

    
        

    