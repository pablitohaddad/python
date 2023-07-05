a = 4
mensagem = "Nenhuma condição foi executada ainda"
if a == 2:
    mensagem ="Entrei no primeiro suite - a vale 2"
elif a == 3:
    mensagem = "Entrei no segundo suite - a vale 3"
elif a == 4:
    mensagem = "Entrei no terceiro suite - a vale 4"
else:
    mensagem = "Entrei no suite do else. O valor %d" % a 
print(mensagem)
