#NESTED LOOP
#catatan : penggunaan modulo pada kondisonal mengasumsikan nilai selain nol sebagai true(benar) dan nol sebagai false(salah)

x = 2
while (x < 10) :
    k = 2
    while(k<=(x/k)) :
        if not (x%k) : break
        k= k + x
    if (k > x/k) : print(x, "benar")
    x = x + 1
print ("selesai")