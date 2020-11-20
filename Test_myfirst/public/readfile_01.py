import xlrd
class exsj():

    def tz(self,lujin,name):
        a=xlrd.open_workbook(lujin)
        s=a.sheet_by_name(name)
        li=[]
        if s.nrows>0:
            for i in range(0,s.nrows):
                li.append(s.row_values(i))
        return li


if __name__ == '__main__':

    a=exsj()
    s=a.tz(r'D:\Users\Administrator\PycharmProjects\Test_myfirst\information\addlb.xlsx','name1')
    print(s)