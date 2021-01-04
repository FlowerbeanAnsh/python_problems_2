def show_info(dct):
    if dct.get('course') not in dct:
        dct.update({'course':'Btech'})
    else:
        pass
    it=dct.items()
    for i in it:
        print(*i)
dc={'name':'harry'}
out=show_info(dc)
