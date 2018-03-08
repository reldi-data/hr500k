import re


class MSDMapper:
    def __init__(self):
        self.msd_upos = {}
        self.msd_mtefeat = {}
        self.msd_udfeat = {}
        with open('mte5-udv2.mapping', 'r', encoding='utf-8') as mapfile:
            for line in mapfile:
                parts = line.strip().split('\t')
                self.msd_upos[parts[0]] = parts[1]
                self.msd_mtefeat[parts[0]] = parts[2]
                self.msd_udfeat[parts[0]] = parts[3]

    def map_word(self, surface_form, lemma, msd):
        mtefeat = self.msd_mtefeat[msd]
        upos = self.msd_upos[msd]
        udfeat = self.msd_udfeat[msd]

        # Pronouns and determiners
        if msd.startswith('Pi') and lemma in ('čiji', 'nečiji', 'ničiji', 'svačiji', 'ičiji'):
            udfeat = udfeat[0:udfeat.rfind('|')] + '|Poss=Yes|PronType=Int,Rel'
        if msd.startswith('Ps'):
            if lemma in ('naš', 'vaš', 'njihov'):
                udfeat = udfeat[0:udfeat.find('Person')] + 'Number[psor]=Plur|' + udfeat[udfeat.find('Person'):]
            elif lemma in ('moj', 'tvoj'):
                udfeat = udfeat[0:udfeat.find('Person')] + 'Number[psor]=Sing|' + udfeat[udfeat.find('Person'):]
            elif lemma == 'njegov':
                udfeat = udfeat[0:udfeat.find('Number')] + 'Gender[psor]=Masc,Neut|' + udfeat[udfeat.find('Number'):udfeat.find('Person')] + 'Number[psor]=Sing|' + udfeat[udfeat.find('Person'):]
            elif lemma in ('njen', 'njezin'):
                udfeat = udfeat[0:udfeat.find('Number')] + 'Gender[psor]=Fem|' + udfeat[udfeat.find('Number'):udfeat.find('Person')] + 'Number[psor]=Sing|' + udfeat[udfeat.find('Person'):]
        if msd.startswith('P'):
            if lemma in ('svako', 'svatko', 'niko', 'nitko', 'neko', 'netko', 'iko', 'itko', 'svašta', 'ništa', 'išta', 'nešto'):
                upos = 'PRON'
            if lemma in ('sav', 'svaki', 'svakakav', 'svačiji', 'nikakav', 'ničiji', 'neki', 'nekolik', 'nekakav', 'nečiji', 'ikoji', 'ičiji', 'ikakav'):
                upos = 'DET'
            if lemma in ('sav', 'sve', 'svako', 'svatko', 'svaki', 'svašta', 'svakakav', 'svačiji'):
                if 'PronType' in udfeat:
                    udfeat = udfeat[0:udfeat.find('PronType')] + 'PronType=Tot'
                else:
                    udfeat += 'PronType=Tot'
            elif lemma in ('niko', 'nitko', 'ništa', 'nikakav', 'ničiji'):
                if 'PronType' in udfeat:
                    udfeat = udfeat[0:udfeat.find('PronType')] + 'PronType=Neg'
                else:
                    udfeat += 'PronType=Neg'
            elif lemma in ('neko', 'netko', 'nešto', 'neki', 'nekolik', 'nekakav', 'nečiji', 'iko', 'itko', 'išta', 'ikoji', 'ičiji', 'ikakav', 'pokoji', 'štošta'):
                if 'PronType' in udfeat:
                    udfeat = udfeat[0:udfeat.find('PronType')] + 'PronType=Ind'
                else:
                    udfeat += '|PronType=Ind'

        # Adverbs
        if msd == 'Rr':
            if surface_form.endswith('ći'):
                udfeat = 'Tense=Pres|VerbForm=Conv'
            elif surface_form.endswith('ši'):
                udfeat = 'Tense=Past|VerbForm=Conv'
        elif msd.startswith('Rg'):
            if lemma in ('sad', 'sada', 'onda', 'tad', 'tada', 'onda', 'ovde', 'ovdje', 'onde', 'ondje', 'ovamo', 'tamo', 'onamo', 'ovuda', 'tuda', 'onuda', 'ovako', 'tako', 'onako', 'tu', 'stoga', 'zato', 'ovoliko', 'toliko', 'onoliko'):
                udfeat += '|PronType=Dem'
            elif lemma in ('gde', 'gdje', 'kud', 'kuda', 'kako', 'kad', 'kada', 'koliko', 'zašto', 'odakle', 'otkada'):
                udfeat += '|PronType=Int,Rel'
            elif lemma in ('nekad', 'nekada', 'ponekad', 'nekako', 'negde', 'negdje', 'nekud', 'nekuda', 'odnekud', 'nekoliko', 'ikad', 'ikada', 'ikako', 'ikoliko'):
                udfeat += '|PronType=Ind'
            elif lemma in ('uvek', 'uvijek', 'svakako', 'svuda', 'posvuda', 'svugde', 'svugdje', 'svakako'):
                udfeat += '|PronType=Tot'
            elif lemma in ('nikad', 'nikada', 'nigde', 'nigdje', 'nikud', 'nikuda', 'nikad', 'nikada', 'nikako', 'nikoliko'):
                udfeat += '|PronType=Neg'

        # Numbers
        if msd.startswith('Mlc') and msd != 'Mlc':
            if 'Number' not in udfeat:
                if lemma == 'jedan':
                    numstr = 'Sing'
                else:
                    numstr = 'Plur'
                udfeat = udfeat[0:udfeat.find('NumType')] + 'Number=' + numstr + '|NumType=Card'
        elif msd.startswith('Mlo'):
            udfeat = udfeat[0:udfeat.find('Gender')] + 'Degree=Pos|' + udfeat[udfeat.find('Gender'):]

        # Verbs
        if msd.startswith('Va'):
            if surface_form in ('nisam', 'nisi', 'nije', 'nismo', 'niste', 'nisu',
                         'neću', 'nećeš', 'neće', 'nećemo', 'nećete', 'neće',
                         'nemam', 'nemaš', 'nema', 'nemamo', 'nemate', 'nemaju',
                         'nemoj', 'nemojmo', 'nemojte'):
                udfeat = udfeat[0:udfeat.find('Tense')] + 'Polarity=Neg|' + udfeat[udfeat.find('Tense'):]

        # Other
        if '%' in surface_form or '$' in surface_form:
            upos = 'SYM'
            if re.search('[0-9]+', surface_form):
                udfeat = 'NumType=Mult'
            else:
                udfeat = '_'

        return mtefeat, upos, udfeat

    def map_file(self, infilename, outfilename):
        with open(infilename, 'r', encoding='utf-8') as infile:
            with open(outfilename, 'w', encoding='utf-8') as outfile:
                for line in infile:
                    if '\t' in line:
                        parts = line.split('\t')
                        mtefeat, upos, udfeat = self.map_word(parts[1], parts[2], parts[4])
                        outfile.write(parts[0] + '\t' + parts[1] + '\t' + parts[4] + '\t' + mtefeat + '\t' + upos + '\t' + udfeat + '\n')
                    else:
                        outfile.write(line)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Mapper from UDv1 CoNLL to UDv2 CoNLL format')
    parser.add_argument('input', help='Path to the input UDv1 file')
    parser.add_argument('output', help='Path to the output UDv2 file')
    args = parser.parse_args()
    mapper = MSDMapper()
    mapper.map_file(args.input, args.output)
