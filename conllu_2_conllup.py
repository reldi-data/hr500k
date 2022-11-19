COLUMNS = ['ID', 'FORM', 'LEMMA', 'UPOS', 'XPOS', 'FEATS', 'HEAD', 'DEPREL', 'DEPS', 'MISC',
           'RELDI:NE', 'RELDI:DP', 'RELDI:SRL', 'RELDI:MISC']

with open('hr500k.conllup', 'w') as fajl:
    fajl.write('# global.columns = {}\n'.format(' '.join(COLUMNS)))

    for line in open('hr500k.conllu'):
        if line.startswith('#'):
            fajl.write(line)

        elif line.strip() == '':
            fajl.write('\n')

        else:
            tid, form, lemma, upos, xpos, feats, head, deprel, deps, misc = line.strip().split('\t')
            ner = '*'
            dp = '*'
            srl = '*'
            rmisc = {}

            if misc != '_':
                misc = dict([f.split('=', 1) for f in misc.split('|')])

                ner = misc.pop('NER', '*')
                dp = misc.pop('DP', '*')
                srl = misc.pop('SRL', '*')

                if 'Normalized' in misc:
                    misc['CorrectForm'] = misc.pop('Normalized')

                if ner != '*':
                    misc['NamedEntity'] = 'Yes'

                if 'ToDo' in misc:
                    rmisc['ToDo'] = misc.pop('ToDo')

                misc = '|'.join(['='.join(f) for f in misc.items()]) or '_'

            rmisc = '|'.join(['='.join(f) for f in rmisc.items()]) or '_'

            fajl.write('\t'.join((tid, form, lemma, upos, xpos, feats, head, deprel, deps, misc, ner, dp, srl, rmisc)))
            fajl.write('\n')
