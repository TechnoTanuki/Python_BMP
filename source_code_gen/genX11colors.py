from os import path

def RGB2int(r: int,
            g: int,
            b: int) -> int:
    return b + (g << 8) + (r << 16)

def int2RGB(i: int):
        return i >> 16, (i >> 8) & 0xff, i & 0xff

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
        m = load(rootdir + "/color.txt",'\t')
        for n in m:
            code += "'%s': %s,\n" % (n[0], RGB2int(int(n[1]),int(n[2]), int(n[3])))
            code1 += "'%s': [%f, %f, %f],\n" % (n[0], int(n[1]) / 255, int(n[2]) / 255 , int(n[3]) / 255)
        code +="}\n"
        code1 +="}\n"

        print(code)
        print(code1)
if __name__ == "__main__":
        main()
