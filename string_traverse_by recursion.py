def my_fun(s):
    if s=='':
        return ''
    print(s[0])
    return my_fun(s[1:]) + s[0]
st='hello python'
out=my_fun(st)
print(out)
