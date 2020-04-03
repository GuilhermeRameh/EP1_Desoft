import random
pr = True
Fichas = 1000
craps = [2, 3, 12]
to_point = [4, 5, 6, 8, 9, 10]
to_field = [3, 4, 9, 10, 11]

while pr:
    Fase = 'Come out'
    def rolar_dados():
        global d1
        global d2
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        return (d1, d2)
    fichas_apostadas_plb = 0
    fichas_apostadas_f = 0
    fichas_apostadas_ac = 0
    fichas_apostadas_t = 0
    f_point = 0
    ac_point = 0
    t_point = 0
    while Fichas >= 0 and Fase == 'Come out':
       print('\nFase: {0}'.format(Fase))
       print('Suas fichas: {0}'.format(Fichas))
       if Fichas <= 0 and fichas_apostadas_plb == 0 and fichas_apostadas_f == 0 and fichas_apostadas_ac == 0 and fichas_apostadas_t == 0:
           pr = False
           break       
       Aposta = input('\n Que tipo de aposta deseja fazer?\n -Pass Line Bet(plb)\n -Field(f)\n -Any Craps(ac)\n -Twelve(t)\n Assim que acabar com suas apostas digite "rolar dados"\n Se deseja sair digite "quit"\n Digite sua resposta: ')
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
       elif Aposta == 'quit':
           pr = False
           break

             
       elif Aposta == 'rolar dados':
           rolar_dados()
           print('\nDado 1: {0}'.format(d1))
           print('Dado 2: {0}'.format(d2))
           print('Soma: {0}'.format(d1 + d2))
           if d1 + d2 == 7 or d1 + d2 == 11: 
               Fichas += 2*fichas_apostadas_plb                
           if d1 + d2 in to_point:
               Fase = 'Point'
               global point
               point = d1 + d2
               plb_point = fichas_apostadas_plb
           if d1 + d2 in to_field:
               Fichas += 2*fichas_apostadas_f
           if d1 + d2 == 2:
               Fichas += 3*fichas_apostadas_f
           if d1 + d2 == 12:
               Fichas += 4*fichas_apostadas_f
           if d1 + d2 in craps:
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
                              
    while Fichas >= 0 and Fase == 'Point':
        print('\nFase: {0}'.format(Fase))
        print('Suas fichas: {0}'.format(Fichas))
        print('Point: {0}'.format(point))
        if Fichas <= 0 and plb_point == 0 and f_point == 0 and ac_point == 0 and t_point == 0:
            pr = False
            break        
        ApostaP = input('\n Que tipo de aposta deseja fazer?\n Pass Line Bet tem {0} fichas apostadas\n -Field(f)\n -Any Craps(ac)\n -Twelve(t)\n Assim que acabar com suas apostas digite "rolar dados"\n Se deseja sair digite "quit"\n Digite sua resposta: '.format(plb_point))
        if ApostaP == 'f':
           f_point = int(input('Quantas fichas deseja apostar? '))
           Fichas -= f_point
           continue
        if ApostaP == 'ac':
           ac_point = int(input('Quantas fichas deseja apostar? '))
           Fichas -= ac_point
           continue
        if ApostaP == 't':
           t_point = int(input('Quantas fichas deseja apostar? '))
           Fichas -= t_point
           continue
        elif ApostaP == 'quit':
            pr = False
            break
           
        elif ApostaP == 'rolar dados':
           rolar_dados()
           print('\nDado 1: {0}'.format(d1))
           print('Dado 2: {0}'.format(d2))
           print('Soma: {0}'.format(d1 + d2))
           if d1 + d2 == 7:
               Fase = 'Come out'
           if d1 + d2 == point:
               Fichas += 2*plb_point
               Fase = 'Come out'
           if d1 + d2 in to_field:
               Fichas += 2*f_point
           if d1 + d2 == 2:
               Fichas += 3*f_point
           if d1 + d2 == 12:
               Fichas += 4*f_point
           if d1 + d2 in craps:
               Fichas += 8*ac_point
           if d1 + d2 == 12:
               Fichas += 31*t_point
           f_point = 0 
           ac_point = 0
           t_point = 0
        else:
           print('\n\n*Verifique os comandos e tente novamente*')

if Fichas <= 0:
    print('Desculpe, mas suas fichas acabaram')
else:
    print('Saiu com {0} fichas!'.format(Fichas))