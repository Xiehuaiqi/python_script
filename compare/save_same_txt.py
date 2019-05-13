from compare import makedir2 as mk2, makedir1 as mk1

anno = mk1.main()
jepg = mk2.main()
print len(anno)
print len(jepg)
txtlist = []
q =1
for i in anno:
    q += 1
    if i in jepg:
        txtlist.append(i)
        # print i
    if q % 5000 == 0:
        print len(txtlist)
        # print ('{}%'.format(len(txtlist)/len(anno)*100))
    # if q==(len(anno)/2):
    #     mk1.text_save(txtlist,'/home/zx/desktop/xiehuaiqi/datasets/CaltechPestrian/train.txt')
mk1.text_save(txtlist,'/home/zx/desktop/xiehuaiqi/datasets/CaltechPestrian/test.txt')
print len(txtlist)
print q
