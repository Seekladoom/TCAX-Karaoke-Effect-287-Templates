'''
ext_fluf002
蜂窝数据附加效果 by我们的夏天
'''
from tcaxPy import *


def tcaxPy_Init():
    global _FD                              # frame duration, in millisecond
    global _Blur, _Bord
    global _FS
    _FD = 1000 / GetVal(val_FXFPS)
    _Blur = GetVal(val_Blur)
    _Bord = GetVal(val_Bord)
    _FS = GetVal(val_FontSize)


def tcaxPy_Fin():
    pass


time_gap = 1    # you can change this value to 0, or 2 or any other number
time_fac = 1    # you can change this value to 0, or 2 or any other number

def tcaxPy_Main(_i, _j, _n, _start, _end, _elapk, _k, _x, _y, _a, _txt):
    ASS_BUF  = []        # used for saving ASS FX lines
    TCAS_BUF = []        # used for saving TCAS FX raw data

    
    if True:
        if True:
            cell = 'm -6 -10 l 6 -10 l 12 0 l 6 10 l -6 10 l -12 0 l -6 -10 '
            clist = []
            able = []
            f = 10
            zoom1 = 45
            zoom2 = 52
            initx = int(GetVal(5) // 2 - _n / 2 * _FS - 55)
            lastx = int(GetVal(5) // 2 + _n / 2 * _FS + 55)
            inity = int(_y - _FS)
            for x in range(initx - f * 1 , lastx + _a + f * 2, f * 2):
                for y in range(inity - f * 0, _y + _FS + f * 1, f):
                    clist.append((x, y))
            for x in range(initx - f * 2 , lastx + _a + f * 1, f * 2):
                for y in range(inity - f // 2 - f * 0, _y + _FS - f // 2 + f * 1, f):
                    clist.append((x, y))
            for (px, py) in clist:
                if (px - _x) ** 2 + (py - _y) ** 2 <= 30 ** 2:
                    able.append((px, py))

            count = int(_k * 1.6)
            for i in range(count):
                pt = choice(able)
                px = pt[0]
                py = pt[1]
                st = randint(_start + _elapk - 10, _start + _elapk + _k)
                et = st + randint(55, 75)
                if st >= _start + _elapk + _k - 5:
                    et = st + randint(70, 100)
                dur = et - st - 10
                transp = 50
                ass_main(ASS_BUF, SubL(st, et, 0, Pix_Style),
                             pos(px, py) + color3('FFFFFF') + color1('FFFFFF') + alpha1(255) + alpha3(transp) + bord(0.8) + blur(0.2) + fad(100, dur * 10) + fsc(zoom1, zoom1), r'{\\p1}'+ cell +'{\\p0}')
                ass_main(ASS_BUF, SubL(st, et, 0, Pix_Style),
                             pos(px, py) + color3('FFFFFF') + color1('FFFFFF') + alpha1(100) + alpha3(transp) + bord(0.0) + blur(6.2) + fad(100, dur * 10) + fsc(zoom2, zoom2), r'{\\p1}'+ cell +'{\\p0}')
            


    return (ASS_BUF, TCAS_BUF)



