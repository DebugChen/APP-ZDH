import csv

# 设计函数专门读取 csv文件====>不变
# 函数 参数1： 读取文件的路径  参数2： 读取文件的行数
def get_csv_data(csv_file,line):
        ck_csv_file= open(csv_file, 'r', encoding='utf-8-sig')
        reader = csv.reader(ck_csv_file)
        # 参数2 :决定了下标位置的开始计数方式
        for index, row in enumerate(reader, 1):
            if index == line:
                print(row)
                return row

if __name__=="__main__":
    get_csv_data("./ckaccount.csv",1)