data={
"st1": {
    "name":"anandhu",
    "email":"abc@gmail.com",
    "marks": {
        "sem1":100,
        "sem2":200,
        "sem3":300
}},
"st2": {
    "name":"zeon",
    "email":"xyz@gmail.com",
    "marks": {
        "sem1":123,
        "sem2":159,
        "sem3":234
}}}
total=0
for x, y in data.items():
    #print(x,y)
    for k,v in y.items():
        print(k, "-",v)        
        if x =="marks":
            for n,m in y.items():
                total=total+m
print(total)
    
            
