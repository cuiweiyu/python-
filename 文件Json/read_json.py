import json


def par_json_2(path):
    with open(path, 'r') as load_f:
        cwy_dict = json.load(load_f)
        spec = cwy_dict['data']['2DFFT']['Spectrum2D']
        time = cwy_dict['data']['timestamp']
        tstep = cwy_dict['data']['2DFFT']['tstep']
        tend = cwy_dict['data']['2DFFT']['tend']
        fstep = cwy_dict['data']['2DFFT']['fstep']
        fend = cwy_dict['data']['2DFFT']['fend']
        print('tstep', tstep)
        # print('tstart', cwy_dict['data']['2DFFT']['tstart'])
        print('tend', tend)
        print("int(tend / tstep)：", int(tend / tstep))
        print("时间点数：", len(spec[0]))
        print('fstep', fstep)
        # print('fstart', cwy_dict['data']['2DFFT']['fstart'])
        print('fend', fend)
        print("int(fend / fstep)：", int(fend / fstep))
        print("频率点数：", len(spec))
    return spec, time


print("==========================================")
s1, t1 = par_json_2("WF0092_WF0092WTG0076_20191111_res.json")
print("=================")
s2, t2 = par_json_2("lyz.json")
print("==========================================")
print("类型对比")
print(type(s1))
print(type(s2))
print("数据长度对比")
print("---长---")
print(len(s1))
print(len(s2))
print("---高---")
print(len(s1[0]))
print(len(s2[0]))
print("时间对比")
print(t1)
print(t2)
