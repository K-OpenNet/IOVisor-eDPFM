hum_address = '192.168.1.2'
length = len(hum_address)
dot = []    # save dot positions fo the human readable IP address
frag = []   # save fragmented numbers of humanm readable IP addresses, each separated by a dot
i=0
while (i< length):
    if (hum_address[i] == '.'):
        dot.append(i)   # save dot positions
    i = i +1

i=0

while (i < len(dot)):   # fragment human readable IP address in between dots & switch them into binaries
    if (i==0):
        frag.append(bin(int(hum_address[:int(dot[0])])))
    else:
        frag.append(bin(int(hum_address[int(dot[i-1]+1):int(dot[i])])))
    i = i+1

frag.append(bin(int(hum_address[int(dot[i-1])+1:])))
i=0
while (i< len(dot)+1):
        frag[i] = frag[i][2:]
        frag[i] = frag[i].zfill(8)
        i = i+1

frag.reverse()  # reverse the order of the frag list
i=0
binary_ver = ''
while (i< len(dot)+1):
    binary_ver = binary_ver + frag[i]
    i = i+1

output = int(binary_ver,2)
print(output)

