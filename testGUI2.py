import pathlib



def conversor(by,MBorGB):
    match(MBorGB):
        case MBorGB if MBorGB=="KB":
            totalF=by/1000
        case MBorGB if MBorGB=="MB":
            totalF=by/1000000
        case MBorGB if MBorGB=="GB":
            totalF=by/1000000000
    return totalF
p = pathlib.Path("C:/Users/chino/Downloads/SERVER_EVAL_x64FRE_es-es.iso")

MBs=conversor(p.stat().st_size,"GB")
print(MBs)
