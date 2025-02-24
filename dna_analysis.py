# 姓名：...
# Python程序设计
# Teamwork1: DNA分析

#这个程序读取DNA测序器的输出并计算统计数据，比如GC的含量。
#从如下命令行运行：python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# sys模块支持读取文件、命令行参数等。
import sys


###########################################################################
### 将核苷酸读入一个名为seq的变量中
###

# 需要指定文件名
if len(sys.argv) < 2:
    print( "运行此程序时，必须提供一个文件名作为参数。")
    sys.exit(2)
# 在命令行上指定的文件名，作为字符串。
filename = sys.argv[1]
# 可以从中读取数据的文件对象。
inputfile = open(filename)

# 输入文件中迄今为止已读取的所有核苷酸。
seq = ""
# 当前行号（=到目前为止读取的行数）。
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # 如果我们在2，6，10行
    if linenum % 4 == 2:
        # 从行尾删除换行符
        line = line.rstrip()
        seq = seq + line
length_seq=len(seq)


###########################################################################
### 计算统计
###

# 迄今为止发现的总核苷酸。
total_count = 0
# G和C核苷酸的数量。
ga_count = 0
gt_count = 0
gc_count = 0
gg_count = 0
extra_count=0
# 对于字符串中的每个碱基（bp），
for bp in seq:
    # 增加我们看到的碱基总数
    total_count = total_count + 1

    # 接下来，如果bp是G或C，
    if bp == 'A' :
        # 增加bp的计数
        ga_count = ga_count + 1
    elif bp=='T' :
        gt_count += 1
    elif bp=='C' :
        gc_count += 1
    elif bp=='G':
        gg_count += 1
    else :
        extra_count +=1
    sum_count=ga_count+gc_count+gt_count+gg_count








# 用GC碱基总计数gc_count 除以总计数total_count
gcg_content = float(gc_count+gg_count) / total_count
gat_content =float(ga_count+gt_count) / total_count

# 打印答案
print ('AT-content:', gat_content)
print ('CG-content:', gcg_content)
print('A count:',ga_count)
print('T count:',gt_count)
print('C count:',gc_count)
print('G count:',gg_count)
print('total_count:',total_count)
print('sum_count:',sum_count)
print('length_seq:',length_seq)

