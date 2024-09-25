# Estilo de formatação ANSI
print('\033[0;30;41mOlá Mundo!\033[m')  # Texto preto, fundo vermelho, reset após
print('\033[4;33;44mOlá Mundo\033[m')   # Texto amarelo sublinhado, fundo azul, reset após
print('\033[1;35;43mOlá Mundo\033[m')   # Texto magenta em negrito, fundo amarelo, reset após
print('\033[30;42mOlá Mundo\033[m')     # Texto preto, fundo verde, reset após
print('\033[mOlá Mundo')                # Reseta todas as formatações
print('\033[7;30mOlá Mundo\033[m')      # Inversão de cores, reset após
