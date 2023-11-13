l = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i']

l[0]#primeiro elemento
l[1] #segundo elemento
n = len[l] #tamanho da lista

l[n -1] #ultimo elemento


l[-1] #ultimo elemento ("i")
l[-2] #penultimo elemento ('h')


# slice: pegar parte da lista

#l[start:stop:step]
l[2:5] # acesso aos indices 2 e 5

l[:] # acesso todo os elementos, é p mesmo que l
l[0:] # acesso todo os elementos, é p mesmo que l, l[:]
l[1:]# acesso todo os elementos, menos o primeiro
l[:n - 1]# acesso todo os elementos, menos p ultimo

#append adiciona no final da lista

l.append(n)
