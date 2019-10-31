from random import random,seed
seed(0)
sr_docs={}
hr_docs={}
def transform(line):
  if not line.startswith('#') and not line.strip()=='':
    line=line.split('\t')
    #print line
    upos=line[8].split('|')
    feats='|'.join(upos[1:])
    #if feats=='':
    #  feats='_'
    upos=upos[0][8:]
    head=line[7].split(':')
    deprel=':'.join(head[1:])
    head=head[0]
    return line[0]+'\t'+line[1]+'\t'+line[2]+'\t'+upos+'\t'+line[4]+'\t'+feats+'\t'+head+'\t'+deprel+'\t_\t'+line[9]+'\n'
  else:
    return line

#read that shit
idx=0
newsent=None
for line in open('hr500k.conll'):
  idx+=1
  if line.startswith('# newdoc id = '):
    if line.startswith('# newdoc id = os-pecine-ri.skole.hr.1'):
      break
    newdoc=line[14:-1]
    if newdoc!='web.hr.1':
      hr_docs[newdoc]=''
      #print newdoc
  if newdoc=='web.hr.1':
    if line.startswith('# sent_id = '):
      newsent=line[12:-1]
      hr_docs[newsent]=''
  if not newdoc=='web.hr.1':
    hr_docs[newdoc]+=transform(line)
  else:
    if newsent!=None:
      hr_docs[newsent]+=transform(line)
  if idx%10000==0:
    print 'line',idx
for line in open('../../setsr/SETimes.SRPlus/set.sr.plus.conll'):
  if line.startswith('# newdoc id = '):
    newdoc=line[14:-1]
    sr_docs[line[14:-1]]=''
    #print newdoc
  sr_docs[newdoc]+=transform(line)
print len(hr_docs),len(sr_docs)

#split set
trainhr=open('hr_set-ud-train.conllu','w')
trainsr=open('sr_set-ud-train.conllu','w')
devhr=open('hr_set-ud-dev.conllu','w')
devsr=open('sr_set-ud-dev.conllu','w')
testhr=open('hr_set-ud-test.conllu','w')
testsr=open('sr_set-ud-test.conllu','w')

for idx in range(163):
  idx=str(idx+1)
  r=random()
  if r<=0.8:
    trainhr.write(hr_docs['set.hr.'+idx])
    trainsr.write(sr_docs['set.sr.'+idx])
  elif r<=0.9:
    devhr.write(hr_docs['set.hr.'+idx])
    devsr.write(sr_docs['set.sr.'+idx])
  else:
    testhr.write(hr_docs['set.hr.'+idx])
    testsr.write(sr_docs['set.sr.'+idx])
  del hr_docs['set.hr.'+idx]
  del sr_docs['set.sr.'+idx]

#put old test into test
testhr.write(hr_docs['set.hr.test'])
testhr.write(hr_docs['wiki.hr.test'])
del hr_docs['set.hr.test']
del hr_docs['wiki.hr.test']

#split serbian news
for idx in range(13):
  idx=str(idx+1)
  r=random()
  if r<=0.8:
    trainsr.write(sr_docs['news.sr.'+idx])
  elif r<=0.9:
    devsr.write(sr_docs['news.sr.'+idx])
  else:
    testsr.write(sr_docs['news.sr.'+idx])
  del sr_docs['news.sr.'+idx]

#split croatian news
for idx in range(85):
  idx=str(idx+1)
  r=random()
  if r<=0.8:
    trainhr.write(hr_docs['news.hr.'+idx])
  elif r<=0.9:
    devhr.write(hr_docs['news.hr.'+idx])
  else:
    testhr.write(hr_docs['news.hr.'+idx])
  del hr_docs['news.hr.'+idx]

#split croatian web sentences
for idx in range(2331):
  idx=str(idx+1)
  r=random()
  if r<=0.8:
    trainhr.write(hr_docs['web.hr-s'+idx])
  elif r<=0.9:
    devhr.write(hr_docs['web.hr-s'+idx])
  else:
    testhr.write(hr_docs['web.hr-s'+idx])
  del hr_docs['web.hr-s'+idx]

print hr_docs.keys()
print sr_docs.keys()
