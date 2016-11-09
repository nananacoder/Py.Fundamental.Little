#!/usr/bin/env python
# -*-coding:utf-8-*-

f = open('mail.bcp.1473400424', 'r')

line = f.readline()
# for line in f.readlines():
#     if not line.strip():
#         continue
#         r = line.split('\t')
#     if len(r)<3:continue
#       print r
#       try:
#          records.setdefault(int(r[1]), {})
#          records[int(r[1])].setdefault(int(r[0]), {})
#          records[int(r[1])][int(r[0])] = float(r[2])
#       except ValueErro:
#         continue
ls = line.split()

# # print ls[1].find(":")
#
for i in range(len(ls)):
    # print ls[i].find(":")
    # if not ls[i].find(":") < 0:
    #     ls[i-1] = ls[i-1] + ' ' + ls[i]
    #     del ls[i]
    #     # print ls
    #     break
    if not ls[i].find("@") < 0:
        ls[i+1] = ls[i] + ls[i+1]
        print ls[i+1]

        break



#         ls[i-1] = ls[i-1] + " " + ls[i]
#         del ls[i]
#     elif ls[i].find("<") > 0:
#         ls[i-1] = ls[i-1] + " " + ls[i]
#     else:
#         pass
# # print ls

