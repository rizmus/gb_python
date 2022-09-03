def rle(data):
    data_encode = ""
    i = 0
    while i < len(data):
        count = 1

        while i + 1 < len(data) and data[i] == data[i + 1]:
            count = count + 1
            i = i + 1

        data_encode += str(count) + data[i]
        i = i + 1

    return data_encode

f_in = open('files/f_in.txt', 'r')
f_out = open('files/f_out.txt', 'w')
f_out.write(rle(f_in.read()))

f_in.close()
f_out.close()