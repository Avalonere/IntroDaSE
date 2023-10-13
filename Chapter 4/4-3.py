# FlowChart by Mermaid
"""graph LR
st((开始))
e((结束))
op1(将第一个元素看作有序表，后面的元素看作无序表)
op2(取出无序表中第一个元素)
op3(从有序表尾部开始向前扫描)
cond1{无序表为空？}
cond2{有序表元素大于无序表元素？}
io1(将无序表元素插入到有序表合适位置)
io2(将有序表元素后移一位)

st-->op1-->op2-->cond1
cond1--是-->e
cond1--否-->op3-->cond2
cond2--是-->io2-->op3
cond2--否-->io1-->op2"""


def straight_insertion_sort(ls):
    n = len(ls)
    for i in range(1, n):
        current = ls[i]
        pre_index = i - 1
        while pre_index >= 0 and current < ls[pre_index]:
            ls[pre_index + 1] = ls[pre_index]
            pre_index -= 1
        ls[pre_index + 1] = current
    return ls
