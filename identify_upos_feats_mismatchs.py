from msd_mapper import MSDMapper


mapper = MSDMapper()
tags = {}
for line in open('mte5-udv2.mapping'):
    line = line.strip().split('\t')
    upos = 'UposTag='+line[1]+'|'+line[3]
    if upos not in tags:
        tags[upos] = set()
    tags[upos].add(line[0])
# print(tags)
# sys.exit()
f = open('hr500k.conll.uposxpos.txt', 'w')
for line in open('hr500k.conll'):
    if line.startswith('#') or line.startswith('\n'):
        f.write(line)
        continue
    els = line.strip().split('\t')
    upos = mapper.map_word(els[1], els[2], els[4])
    upos = 'UposTag='+upos[1]+'|'+upos[2]
    # print(upos,els[8])
    if els[8] == upos:
        f.write(line)
        continue
    if els[8] not in tags:
        print('UPOS', els[4], els[8])
        f.write('UPOS!!!\t'+line)
    else:
        if els[4] not in tags[els[8]]:
            print('XPOS', els[4], els[8])
            f.write('XPOS!!!\t'+line)
        else:
            print('LAST RESORT')
            f.write(line)
f.close()
