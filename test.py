# todo: file operation

if __name__ == "__main__":
    fp = open("d:\\lusichen\\123\\123.txt", "r+")
    s = fp.read()
    print(s)
    ss = '1' + s
    print(ss)
    fp.seek(0, 0)
    fp.write(ss)
    fp.close()

