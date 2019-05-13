from compare import makedir1 as mk1

file = '/home/zx/desktop/xiehuaiqi/datasets/CaltechPestrian/test.txt'
f1 = open(file)
test = f1.readlines()
train = []
for line in test:
    pre = line.split('_')
    if pre[0] in ['set06','set07','set08','set09','set10']:
        line = line.strip('\n')
        train.append(line)
mk1.text_save(train,'/home/zx/desktop/xiehuaiqi/datasets/CaltechPestrian/test1.txt')