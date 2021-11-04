# hr500k

Training dataset for standard Croatian, content described in https://aclanthology.org/L16-1676/.

`conll_2_conllu.py` is used for transforming the old conll format into the conllu format. The conllu format should be the reference format.

Validating the conllu format can be done with UD tools like this:
```
python ../tools/validate.py --lang HR --level 1 hr500k.conllu
```
This test should be passed completely.

```
python ../tools/validate.py --lang HR --level 2 hr500k.conllu
```
This test should be passed except for the formatting and syntactic errors (good part of the dataset does not have UD annotations).

XPOS tags and their mapping to UPOS should be validated as well.
```
python ../hr500k/check_xpos_upos_feats.py ../hr500k/mte5-udv2.mapping hr500k.conllu hr500k.uposxpos.txt |sort|uniq -c
```

Currently the output of this command should be the number of UPOS and XPOS mismatches, something along the line of

```
  93 UPOS Rgc UposTag=DET|Degree=Cmp
 100 UPOS Rgp UposTag=DET|Degree=Pos
   7 UPOS Rgp UposTag=DET|Degree=Pos|PronType=Dem
 149 UPOS Rgp UposTag=DET|Degree=Pos|PronType=Ind
   7 UPOS Rgp UposTag=DET|Degree=Pos|PronType=Int,Rel
   6 UPOS Rgs UposTag=DET|Degree=Sup
 178 UPOS Y UposTag=ADJ|_
  93 UPOS Y UposTag=ADV|_
 821 UPOS Y UposTag=NOUN|_
 191 UPOS Y UposTag=PROPN|_
   3 UPOS Y UposTag=VERB|_
   5 XPOS Y UposTag=ADV|Degree=Pos
   4 XPOS Y UposTag=INTJ|_
 154 XPOS Y UposTag=PART|_
 214 XPOS Y UposTag=X|_
```
In the file `hr500k.uposxpos.txt` these mismatches can be analysed in context by searching for `UPOS!!!` or `XPOS!!!`.
