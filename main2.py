# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:17:03 2019

@author: Hengky Sanjaya
"""

# import sys
from graphviz import Digraph

from plyparser import parser

s2 = """
1 int b = 10;
2 int c = 15;

3 while(b == 5){
    3.1while(a < 10000){
        3.1.1if(a == 0){
            3.1.1.1if(b == c){
                3.1.1.1.1cout << "test";
            3.1.1.1}
        3.1.1}    
    3.1}

    3.2cout << "coba";
3}

"""

s2 = """
int b = 10;
int c = 15;

while(b == 5){
    while(a < 10000){
        if(a == 0){
            if(b == c){
                cout << "test";
                cout << "coba";
            }
        }    
    }
    
    cout << "aaaa";
}
            
cout << "bbbb";
cout << "cccc";
"""

#s2 = """
#
#if(a == b){
#        cout << "test";
#        if(a > 0){
#            cout << "wwwwwwwwwwww";
#        }
#        else if(b>0){
#            cout << "abcasdfasdf";
#        }
#}
#else if(a > 0){
#    cout << "abc";
#}
#else{
#    cout << "bbb";
#}
#"""

print("\n")
result = parser.parse(s2)
print("result ", result)

print("\n")





class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        self[key] = value


newres = my_dictionary()


print("result ",result,"\n")
# print(len(result[0]))
# print(result[0][0:])

final_res = []

# for i in result:
closing_code = []
def convert(p):
#    print("p",p,"\n")
    if (isinstance(p, tuple)):
        size = len(p)
        
        if (size == 3 or size == 4):
            # tuple doang ga ada array d dlmny
            final_res.append(p[0:])
        else:
            #klo misal ada array di dalam tuple
            final_res.append(p[0:3])
#            print("p[3]",p[3],"\n")
            
#            if(p[2] == "{"):
#                closing_code.append("}")
            for i in range(3, len(p)):
                print("p[i]",p[i])
                if(p[i] != '}'):
                    convert(p[i])
#            convert(p[3])
            
            if(p[2] == '{' or p[1] == '{'):
                print("wwwwwwww",p[1])
                final_res.append('}')
    
    elif(isinstance(p, list)):
        for a in p:
            convert(a)
    else:
        final_res.append(p)

convert(result)
print("final_res",final_res)



def set_label(data):
    res = ''
    for i in data:
        res += str(i) +"."
    return res

line = 1 # nentuin increment n linenya
scope = [0] # array utk simpan posisi nested
position = 0 # utk nentuin jangkauan di scope
new_indexing_result = []
for i in final_res:
    data = list(i)
    size = len(data)
    # pos = str(line) + "." + str(scope[position])

    scope[position] += 1
    # print("position", position)
    print("scope", scope)

    # print("data", data, size)

    if(data[-1] == '}'):
        scope[position] = 1
        position -= 1
      
    label = set_label(scope[0:position+1])
    
    if(data[-1] == '{'):
        scope.append(0)
        position += 1
          
    


    data.insert(0, label)

    new_indexing_result.append(data)

print("scope" , scope)

for i in new_indexing_result:
    print("#", i)


fc = Digraph(name="flowchart", strict=True,format='png')

# start = []
# condition = []
# stm = []
# start.append('start')
num = 0

scope2 = []
for i in new_indexing_result:
    scope2.append(i[0])

# print(scope2)
for i in new_indexing_result:
    # if num>0:
    #     fc.edge(str(num - 1), str(num))
    if i[1] in {'int', 'string', 'bool', 'char'}:
        # start.append(i[2])
        fc.attr('node', shape ='rectangle')
        fc.node(str(num), label=i[2])
        if num == 0:
            fc.attr('node', rankdir='LR')
            fc.node('start', shape='oval')
            fc.edge('start', str(num))
        if num > 0:
            fc.edge(str(num - 1), str(num))
        num += 1

    if i[1] in {'while', 'for', 'if', 'else if'}:
        # condition.append(i[2][1])
        # fc.attr('node', shape='diamond')
        fc.node(str(num), label=i[2][2], shape='diamond')
        if num > 0:
            fc.edge(str(num - 1), str(num))
        if num == 0:
            fc.attr('node', rankdir='LR')
            fc.node('start', shape='oval')
            fc.edge('start', str(num))

        num+=1

        for s in range(0, num):
            if scope2[num][0:-2] == scope2[num - s]:
                fc.edge(str(num), str(num-s), label='false')

        fc.edge(str(num - 1), str(num), label='true')


    if i[1] in {'cin', 'cout'}:
        # stm.append(i[3])
        # fc.attr('node', shape='parallelogram')
        fc.node(str(num), label="print "+i[3], shape='parallelogram')
        if num>0:
            fc.edge(str(num - 1), str(num))
        if num == 0:
            fc.attr('node', rankdir='LR')
            fc.node('start', shape='oval')
            fc.edge('start', str(num))
        num+=1


fc.node(str(num), label='end', shape='circle')
fc.edge(str(num - 1), str(num))





# print(start)
# print(condition)
# print(stm)



# fc.attr('node',shape ='rectangle')
# fc.node('var1', label='b = 5')
# fc.edge('start', 'var1')


# end = 'end' + str(1)
fc.view()
print(fc.source)


# newres = []
# id = 1
# def traverse(p):
#     global id
#
#     if (isinstance(p, list) or isinstance(p, tuple)):
#         for i in p:
#             traverse(i)
#     else:
#         id += 1
#         # print(id, "    ",p)
#         newres.add(id, p)
#         # id += 1
#
# traverse(result)
#
#
# # newres.items()
# print("newres ",newres)
# print("\n")
# # print(result[1][1])
#
#
#
# # convert into flowchart
#
# condition = my_dictionary()
# func = my_dictionary()
# var_dec = my_dictionary()
# for key,value in newres.items():
#     try:
#         if value == '(':
#             condition.add(key+1,newres[key+1])
#         if value in {'if', 'else if', 'while', 'for', '{', '}'}:
#             func.add(key,value)
#         if value in {'int', 'string', 'char', 'bool'}:
#             var_dec.add(key, value)
#     except:
#         continue
#
# print("condition : " + str(condition))
# print("function : " + str(func))
# print("var_dec : " + str(var_dec))