""" 
@author: lileilei
@file: ddd.py 
@time: 2018/1/19 11:43 
"""
import xlrd
def huoqu_test(filepath,index):
    try:
        file = xlrd.open_workbook(filepath)
        me = file.sheets()[index]
        nrows = me.nrows
        listdata = []
        for i in range(1, nrows):
            dict_canshu = {}
            dict_canshu['id']=me.cell(i,0).value
            dict_canshu.update(eval(me.cell(i,2).value))
            dict_canshu.update(eval(me.cell(i,3).value))
            listdata.append(dict_canshu)
        return listdata
    except Exception as e:
        print(e)