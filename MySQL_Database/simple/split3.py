#!/usr/bin/python
# -*- coding:utf-8 -*-
def main():
    # 先得到要分割的文件的起始和结束位置所在行数并放入列表x中
    count, total, j, l = 0, 0, 0, 0
    x = [0, ]
    fin = open('cdu.sql', 'r')
    for line in fin:
        total += 1
        if re.search('-- -----*', line):  # 以此判断表的数量
            count += 1
            if count % 10 == 0:  # 每到10张表时将分割的行数写入x列表中
                # print(count,total)
                x.append(total)

    x.append(len(open('cdu.sql').readlines()) + 1)  # 将最后一行也放入x中

    for i in x:
        print(i, end = ' ')

        print()

        cnt = 1
        # 读取x中的行数，起始和结束位置将文件内容复制到新文件中
        for i, j in enumerate(open('cdu.sql', 'r')):
            if i <= x[cnt]:
                with open('%dcdu.sql' % cnt, 'a+') as f:
                    f.write(j)
            else:
                cnt += 1
                print("wirte file" + str(cnt))
        print("ok")
    if __name__ == '__main__': main()