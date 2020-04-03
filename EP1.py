import random
pr = True
Fichas = 1000

while pr:
    Fase = 'Come out'
    def rolar_dados():
        global d1
        global d2
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)

    while Fichas >= 0 and Fase == 'Come out':
       print('\nFase: {0}'.format(Fase))
       print('Suas fichas: {0}'.format(Fichas))
       if Fichas <= 0:
           pr = False
           break       
       Aposta = input('\n Que tipo de aposta deseja fazer?\n -Pass Line Bet(plb)\n -Field(f)\n -Any Craps(ac)\n -Twelve(t)\n Assim que acabar com suas apostas digite "rolar dados"\n Digite sua resposta: ')
       if Aposta == 'plb':
           fichas_apostadas_plb = int(input('Quantas fichas deseja apostar? '))
           Fichas -= fichas_apostadas_plb
           continue
       if Aposta == 'f':
           fichas_apostadas_f = int(input('Quantas fichas deseja apostar? '))
           Fichas -= fichas_apostadas_f
           continue
       if Aposta == 'ac':
           fichas_apostadas_ac = int(input('Quantas fichas deseja apostar? '))
           Fichas -= fichas_apostadas_ac
           continue
       if Aposta == 't':
           fichas_apostadas_t = int(input('Quantas fichas deseja apostar? '))
           Fichas -= fichas_apostadas_t
           continue
             
       elif Aposta == 'rolar dados':
           rolar_dados()
           print('\nDado 1: {0}'.format(d1))
           print('Dado 2: {0}'.format(d2))
           print('Soma: {0}'.format(d1 + d2))
           if d1 + d2 == 7 or d1 + d2 == 11: 
               Fichas += 2*fichas_apostadas_plb                
           if d1 + d2 == 4 or 5 or 6 or 8 or 9 or 10:
               Fase = 'Point'
               global point
               point = d1 + d2
               plb_point = fichas_apostadas_plb
           if d1 + d2 == 3 or 4 or 9 or 10 or 11:
               Fichas += 2*fichas_apostadas_f
           if d1 + d2 == 2:
               Fichas += 3*fichas_apostadas_f
           if d1 + d2 == 12:
               Fichas += 4*fichas_apostadas_f
           if d1 + d2 == 2 or 3 or 12:
               Fichas += 8*fichas_apostadas_ac
           if d1 + d2 == 12:
               Fichas += 31*fichas_apostadas_t
           fichas_apostadas_plb = 0
           fichas_apostadas_f = 0 
           fichas_postadas_ac = 0
           fichas_apostadas_t = 0
           if Fichas == 0:
               pr = False
               break
       else:
           print('\n\n*Verifique os comandos e tente novamente*')
           
   