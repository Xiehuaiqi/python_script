#coding:utf-8
txt_read = open("MOT17-04_gt.txt","r")   #设置文件对象
txt_lines_count = len(open(r"MOT17-04_gt.txt",'rU').readlines())
print(txt_lines_count)

# 取得最大值
def count_len():
    a=0
    for i in range(txt_lines_count):
        line = txt_read.readline()
        kk=line.split(',')
        # print(kk[0])
        # 比较获得最大值
        if int(kk[0])>a:
            a=int(kk[0])
    return a

txt_max = count_len()+1

# 输出结果
for i in range(1,txt_max):
    txt_read = open("MOT17-04_gt.txt", "r")
    # 在文件夹中新建txt文档
    txt_file = "MOT17-04/"+'MOT17-04_'+str(i)+".txt"
    # 打开txt文件
    txt_open=open(txt_file,'w')

    for j in range(txt_lines_count):
       line1 = txt_read.readline()
       ss=line1.split(',')

       if ss[0]== str(i) :
         print(line1)
         txt_open.write(line1)

    txt_read.close()
    txt_open.close()

