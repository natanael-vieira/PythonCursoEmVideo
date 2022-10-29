from time import sleep

print('========== MAIOR NÚMERO ==========\n')

def maior(* num):
    sleep(2.0)
    for v in num:
        print(v, end=' ', flush=True)
        sleep(0.3)
    print(f'Ao todo foram digitados {len(num)} números')
    sleep(0.3)
    print(f'O maior número digitado foi: {max(num) if len(num) !=0 else "0"}\n')
    print('=' * 40)
    print()


#Programa Principal
maior(2, 9, 15, 3, 8)
maior(2)
maior(21, 19, 15, 33, 88)
maior(15, 13, 18)
maior()
