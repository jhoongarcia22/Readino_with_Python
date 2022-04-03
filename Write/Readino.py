f = open('Write.ino', 'r')
pos = (('int', 'float', 'byte', 'bool', 'constante'),
       '\t\t\t\t\t Se declara la funcion',
       '\t\t\t\t\t Se declara la funcion en loop en donde irá el programa',
       '\t Se pone un breve comentario',
       '\t\t\t\t Se declara el pin',
       '\t\t\t\t Se lee el pin',
       '\t\t\t\t\t\t Se cierra el corchete',
       '\t\t\t\t\t Se pone un delay',
       '\t\t\t\t\t\t Se realiza un salto de linea')
state=('como salida', 'como entrada', 'y se activa la resistencia de pull up',
       'en alto', 'en bajo', 'INDEFINIDO')
while(True):
    line=f.readline()
    line = line.strip(" ")

    if(line.startswith('int')):
        line = line.rstrip('\n')
        name = line.replace(" ","").replace(';','')
        name = name.strip('int')
        name = name.split(',')
        size = len(name)
        vaa = []
        var = {}
        for x in range(size):
            vaa.append([0])
            nname = str(name[x])
            nname = nname.replace(" ","").replace('=',',')
            vaa[x] = nname.split(',')
            sizevaa = len(vaa[x])
            if sizevaa == 1:
                vaa[x].insert(sizevaa, '0')
            for y in range(1):
                var.update({f'{vaa[x][y]}': f'{vaa[x][y+1]}'})

        if len(name) != 1:
            print(line,f"\t\t\t\t Se declaran {size} variables de tipo {pos[0][0]} así: ", end="")
            for x in range(size):
                for y in range(1):
                    print(vaa[x][y], end =" inicializada en -> ")
                    print(vaa[x][y+1], end =", ")
        else:
            name.insert(size, '0')         
            var.update({f'{name[0]}': f'{name[1]}'})
            print(line,f"\t\t\t\t Se declara una variable de tipo {pos[0][0]} con el nombre: ", end="")
            for x in range(size):
                for y in range(1):
                    print(vaa[x][y], end =" inicializada en -> ")
                    print(vaa[x][y+1], end =", ")
        print("")
        
    elif(line.startswith('float')):
        line = line.rstrip('\n')
        name = line.replace(" ","").replace(';','')
        name = name.strip('float')
        name = name.split(',')
        size = len(name)
        vaa = []
        var = {}
        for x in range(size):
            vaa.append([0])
            nname = str(name[x])
            nname = nname.replace(" ","").replace('=',',')
            vaa[x] = nname.split(',')
            sizevaa = len(vaa[x])
            if sizevaa == 1:
                vaa[x].insert(sizevaa, '0')
            for y in range(1):
                var.update({f'{vaa[x][y]}': f'{vaa[x][y+1]}'})

        if len(name) != 1:
            print(line,f"\t\t\t\t Se declaran {size} variables de tipo {pos[0][1]} así: ", end="")
            for x in range(size):
                for y in range(1):
                    print(vaa[x][y], end =" inicializada en -> ")
                    print(vaa[x][y+1], end =", ")
        else:
            name.insert(size, '0')         
            var.update({f'{name[0]}': f'{name[1]}'})
            print(line,f"\t\t\t\t Se declara una variable de tipo {pos[0][1]} con el nombre: ", end="")
            for x in range(size):
                for y in range(1):
                    print(vaa[x][y], end =" inicializada en -> ")
                    print(vaa[x][y+1], end =", ")
        print("")

    elif(line.startswith('byte')):
        line = line.rstrip('\n')
        name = line.replace(" ","").replace(';','')
        name = name.strip('byte')
        name = name.split(',')
        size = len(name)
        vaa = []
        var = {}
        for x in range(size):
            vaa.append([0])
            nname = str(name[x])
            nname = nname.replace(" ","").replace('=',',')
            vaa[x] = nname.split(',')
            sizevaa = len(vaa[x])
            if sizevaa == 1:
                vaa[x].insert(sizevaa, '0')
            for y in range(1):
                var.update({f'{vaa[x][y]}': f'{vaa[x][y+1]}'})

        if len(name) != 1:
            print(line,f"\t\t\t\t Se declaran {size} variables de tipo {pos[0][2]} así: ", end="")
            for x in range(size):
                for y in range(1):
                    print(vaa[x][y], end =" inicializada en -> ")
                    print(vaa[x][y+1], end =", ")
        else:
            name.insert(size, '0')         
            var.update({f'{name[0]}': f'{name[1]}'})
            print(line,f"\t\t\t\t Se declara una variable de tipo {pos[0][2]} con el nombre: ", end="")
            for x in range(size):
                for y in range(1):
                    print(vaa[x][y], end =" inicializada en -> ")
                    print(vaa[x][y+1], end =", ")
        print("")

    elif(line.startswith('bool')):
        line = line.rstrip('\n')
        name = line.replace(" ","").replace(';','')
        name = name.strip('bool')
        name = name.split(',')
        size = len(name)
        vaa = []
        var = {}
        for x in range(size):
            vaa.append([0])
            nname = str(name[x])
            nname = nname.replace(" ","").replace('=',',')
            vaa[x] = nname.split(',')
            sizevaa = len(vaa[x])
            if sizevaa == 1:
                vaa[x].insert(sizevaa, '0')
            for y in range(1):
                var.update({f'{vaa[x][y]}': f'{vaa[x][y+1]}'})

        if len(name) != 1:
            print(line,f"\t\t\t\t Se declaran {size} variables de tipo {pos[0][3]} así: ", end="")
            for x in range(size):
                for y in range(1):
                    print(vaa[x][y], end =" inicializada en -> ")
                    print(vaa[x][y+1], end =", ")
        else:
            name.insert(size, '0')         
            var.update({f'{name[0]}': f'{name[1]}'})
            print(line,f"\t\t\t\t Se declara una variable de tipo {pos[0][3]} con el nombre: ", end="")
            for x in range(size):
                for y in range(1):
                    print(vaa[x][y], end =" inicializada en -> ")
                    print(vaa[x][y+1], end =", ")
        print("")

    elif(line.startswith('#define')):
        line = line.rstrip('\n')
        name = line.replace(" ","").replace(';','')
        name = name.strip('#define')
        name = name.split(',')
        size = len(name)
        vaa = []
        var = {}
        for x in range(size):
            vaa.append([0])
            nname = str(name[x])
            nname = nname.replace(" ","").replace('=',',')
            vaa[x] = nname.split(',')
            sizevaa = len(vaa[x])
            if sizevaa == 1:
                vaa[x].insert(sizevaa, '0')
            for y in range(1):
                var.update({f'{vaa[x][y]}': f'{vaa[x][y+1]}'})

        if len(name) != 1:
            print(line,f"\t\t\t\t Se declaran {size} variables de tipo {pos[0][4]} así: ", end="")
            for x in range(size):
                for y in range(1):
                    print(vaa[x][y], end =" inicializada en -> ")
                    print(vaa[x][y+1], end =", ")
        else:
            name.insert(size, '0')         
            var.update({f'{name[0]}': f'{name[1]}'})
            print(line,f"\t\t\t\t Se declara una variable de tipo {pos[0][4]} con el nombre: ", end="")
            for x in range(size):
                for y in range(1):
                    print(vaa[x][y], end =" inicializada en -> ")
                    print(vaa[x][y+1], end =", ")
        print("")
        
    elif(line.startswith('void setup')):
        print(line.rstrip('\n'), pos[1])
    elif(line.startswith('void loop')):
        print(line.rstrip('\n'), pos[2])
    elif(line.startswith('//')):
        print(line.rstrip('\n'), pos[3])
    elif(line.startswith('pinMode')):
        p=line.rstrip('\n')
        print(p, pos[4], end = " ")
        p=p.replace(' ', '')    
        print(p[8], end = "")
        print(p[9].replace(',', ' '), end = " ")
        s= p.split(sep = ',')
        if('INPUT' in s[1]):
            print(state[1], end = " ")
            if('INPUT_PULLUP' in s[1]):
                print(state[2])
            else:
                print("")
        elif('OUTPUT' in s[1]):
            print(state[0])
        else:
            print(state[5])
    elif(line.startswith('digitalWrite')):
        p=line.rstrip('\n')
        print(p, pos[4], end = " ")
        p=p.replace(' ', '')
        print(p[13], end = "")
        print(p[14].replace(',', ' '), end = " ")
        s= p.split(sep = ',')
        if('HIGH' in s[1]):
            print(state[3])
        elif('LOW' in s[1]):
            print(state[4])
        else:
            print(state[5])
    # elif('digitalRead' in line):
    #     p = line.rstrip('\n')
    #     print(p, pos[4], end=" ")
    #     p = p.replace(' ', '')
    #     print(p[13], end="")
    #     print(p[14].replace(',', ' '), end=" ")
    #     s = p.split(sep=',')
    #     if('HIGH' in s[1]):
    #         print(state[2])
    #     elif('LOW' in s[1]):
    #         print(state[3])
    #     else:
    #         print(state[4])
    elif(line.startswith('}')):
        print(line.rstrip('\n'), pos[6])
    elif(line.startswith('delay')):
        print(line.rstrip('\n'), pos[7])
    elif(line.startswith('\n')):
        print(line.rstrip('\n'), pos[8])
    if not line:
        break
f.close()
