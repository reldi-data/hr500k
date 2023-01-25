# Results of testing the .conllup file format using the ud-tools validator

## Level 1
```
*** PASSED ***
```

## Level 2
```
[Line 226946 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 226946 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'

The following 37 relations are currently permitted in language [ud]:
acl, advcl, advmod, amod, appos, aux, case, cc, ccomp, clf, compound, conj, cop, csubj, dep, det, discourse, dislocated, expl, fixed, flat, goeswith, iobj, list, mark, nmod, nsubj, nummod, obj, obl, orphan, parataxis, punct, reparandum, root, vocative, xcomp
If a language needs a relation subtype that is not documented in the universal guidelines, the relation
must have a language-specific documentation page in a prescribed format.
See https://universaldependencies.org/contributing_language_specific.html for further guidelines.
Documented dependency relations can be specifically turned on/off for each language in which they are used.
See https://quest.ms.mff.cuni.cz/udvalidator/cgi-bin/unidep/langspec/specify_deprel.pl for details.

[Line 226947 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 226947 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 226948 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 226948 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 226949 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 226949 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 226950 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 226950 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 226951 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 226951 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 226952 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 226952 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 226953 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 226953 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 226954 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 226954 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 226955 Sent os-pecine-ri.skole.hr-s1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
...suppressing further errors regarding Syntax
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 226969 Sent os-pecine-ri.skole.hr-s1]: [L2 Format invalid-head] Invalid HEAD: '_'.
...suppressing further errors regarding Format
Format errors: 315979
Syntax errors: 900678
*** FAILED *** with 1216657 errors
```

# Results of testing the UPOS-XPOS correspondence using reldi-data validator (aggregated results)

```
     93 UPOS Rgc UposTag=DET|Degree=Cmp
    100 UPOS Rgp UposTag=DET|Degree=Pos
      7 UPOS Rgp UposTag=DET|Degree=Pos|PronType=Dem
    149 UPOS Rgp UposTag=DET|Degree=Pos|PronType=Ind
      7 UPOS Rgp UposTag=DET|Degree=Pos|PronType=Int,Rel
      6 UPOS Rgs UposTag=DET|Degree=Sup
    178 UPOS Y UposTag=ADJ|_
     93 UPOS Y UposTag=ADV|_
      5 UPOS Y UposTag=ADV|Degree=Pos
      4 UPOS Y UposTag=INTJ|_
    821 UPOS Y UposTag=NOUN|_
    154 UPOS Y UposTag=PART|_
    191 UPOS Y UposTag=PROPN|_
      3 UPOS Y UposTag=VERB|_
    214 UPOS Y UposTag=X|_
```
