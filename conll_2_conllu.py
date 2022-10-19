f = open('hr500k.conllu', 'w')
for line in open('hr500k.conll'):
    if line.startswith('#'):
        f.write(line)
        heads = []
        dependents = []
        sent = []
    elif line.strip() == '':
        # print(heads, dependents)
        for head, dep, idx in dependents:
            sent[idx][-1].append('SRL='+heads[head]+':'+dep)
        for token in sent:
            if len(token[-1]) == 0:
                token[-1].append('_')
            f.write('\t'.join(token[:-1])+'\t'+'|'.join(token[-1])+'\n')
        f.write('\n')
    else:
        tid, token, lemma, _, xpos, _, dp, ud, upos, misc, ner = line.strip().split('\t')[:11]
        srl = line.strip().split('\t')[11:]
        l = list(filter(lambda r: r != '_', srl))
        if l:
            print(l)
        if srl[0] != '_':
            heads.append(tid)
        for i, e in enumerate(srl[1:]):
            if e != '_':
                dependents.append((i, e, int(tid)-1))
        ud_head = ud.split(':')[0]
        ud_label = ':'.join(ud.split(':')[1:])
        if ud_label == '':
            ud_head = '_'
            ud_label = '_'
        upos = upos.split('|')
        feats = '|'.join(upos[1:])
        upos = upos[0].split('=')[1]
        misc_list = []
        if dp != '_':
            misc_list.append('DP='+dp)
        if misc != '_':
            misc_list.append(misc)
        if ner != 'O':
            misc_list.append('NER='+ner)
        # if len(misc_list) == 0:
        #     misc_list.append('_')
        # f.write('\t'.join((tid, token, lemma, upos, xpos, feats, ud_head, ud_label, '_', '|'.join(misc_list))) + '\n')
        sent.append((tid, token, lemma, upos, xpos, feats, ud_head, ud_label, '_', misc_list))
