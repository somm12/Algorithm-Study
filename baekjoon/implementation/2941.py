arr = ['c=' ,'c-', 'dz=', 'd-', 'lj', 'nj',	's=','z=']
string = input()
result = 0
con = 0
finish = True
while finish:
    for i in range(len(arr)):
        if arr[i] not in string:
            con += 1
       
        if con== 8:
            finish = False
    con =0
    if arr[0] in string:
        result  += 1
        string = string.replace(arr[0],'0')
    if arr[1] in string:
        result  += 1
        string = string.replace(arr[1],'0')
    if arr[2] in string:
        result  += 1
        string = string.replace(arr[2],'0')
    if arr[3] in string:
        result  += 1
        string = string.replace(arr[3],'0')
    if arr[4] in string:
        
        result  += 1
        string =  string.replace(arr[4],'0')
        
    if arr[5] in string:
        
        result  += 1
        string = string.replace(arr[5],'0')
        
    if arr[6] in string:
        
        result  += 1
        string = string.replace(arr[6],'0')
        
    if arr[7] in string:
        result  += 1
        string = string.replace(arr[7],'0')


count = 0
for i in range(len(string)):
    if(string[i]=='0'):
        count += 1
if count != result:
    result += (count-result)

string = string.replace('0','')  
result += len(string)
print(result)