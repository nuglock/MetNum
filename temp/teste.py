list = ['Tiago','Ivan','Henrique', 'Paulo']
nome = 'teste'
nome = input('Digite um nome: ') # Python input prompt
print(nome)
for i in range(len(list)):
    if list[i] == nome:
        print(nome,'is number',i + 1,'on the list')
        break
else:
    print(nome,'is not on the list')