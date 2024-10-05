with  open("../ESP32/corbeau") as f:
    i=0
    for line in f:
        i+=1
        print(i,".",line)
    f.seek(0)
    print(f.readline(5))