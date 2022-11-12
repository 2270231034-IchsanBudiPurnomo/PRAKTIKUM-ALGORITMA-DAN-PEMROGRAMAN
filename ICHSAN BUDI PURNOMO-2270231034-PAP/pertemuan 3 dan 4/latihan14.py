data ="ini adalah string"
print (data)
print (type(data))

#1. cara membuat string

'''
    1. dengan menggunakan single qoute '...'
    2. dengan menggunakan double qoute "..."
'''
data = 'menggunakan single qoute'
print(data)

data2 = "menggunakan double qoute"
print(data2)

print('''hello, apa kabar?''')
print('''hello, apa kabar?''')
print("ini adlah hari jum'at")

#2. menggunakan tanda (\)
    #membuat tanda 'menjadi string
print("mari shalat jum\\'at'")
print("g\'day,isn\'t it?")

#backslash
print("c:\\user\\ucup")

#tab
print("ucup\t\t\totong,semakin jauhan")

#backspace
print("ucup\botong, jadi deketan")

#newline
print("baris pertama.\nbaris kedua.")   #LF -> line feed -> unix,macos,linux
print("baris pertama.\rbaris kedua")    #CR -> carriage return -> commodore,acorn,lisp
print("baris pertama.\r\nbaris kedua")  #CRLF -> line feed carriage return -> windows

#3. string literal atau raw
    #hati hati
print("c:\new folder") #akan salah pathnya
    #menggunakan raw string
print(r'c:\new folder')

#multiline literal string
print('''
nama : ucup
kelas : 3 SD
''')

#mltiline literal string dan raw
print(r"""
nama : ucup
kelas : 3 sd\new normal
website : www.ucup.com/newid
""")


