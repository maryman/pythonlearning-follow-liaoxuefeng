# -*- coding: utf-8 -*-
def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
    else:
        #移动n-1个盘从A通过C到B
        move(n-1,a,c,b)
        #移动A最下面的盘到C
        move(1,a,b,c)
        #移动n-1个盘从B通过A到C
        move(n-1,b,a,c)
move(3,'A','B','C')