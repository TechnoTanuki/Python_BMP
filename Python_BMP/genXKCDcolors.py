from os import path

def RGB2int(r: int,
            g: int,
            b: int) -> int:
    return b + (g << 8) + (r << 16)

def int2RGB(i: int):
        return  i >> 16, (i >> 8) & 0xff, i & 0xff

def load(filename, delimiter):
    m = []
    with open(filename) as f:
        for line in f:
            m.append(line.replace('\n', '').split(delimiter))
        f.close()
    return m

def main():
        code ="{\n"
        code1 ="{\n"
        rootdir = path.dirname(__file__)
        m = load(rootdir + "/XKCDrgb.txt",'\t')
        for n in m:
            o = int2RGB(int(n[1],16))
            code += "'%s': %s,\n" % (n[0], RGB2int(o[0], o[1], o[2]))
            code1 += "'%s': [%f, %f, %f],\n" % (n[0], o[0] / 255, o[1] / 255 , o[2] / 255)
        code +="}\n"
        code1 +="}\n"

        #print(code)
        print(code1)
if __name__ == "__main__":
        main()
