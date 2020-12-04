# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:17:03 2019

@author: Hengky Sanjaya
"""

# import sys

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





# print("final_res indexing",new_indexing_result)

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