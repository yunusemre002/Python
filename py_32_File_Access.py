"""
"r"     Okuma
"w"     Yazma   (Eski içeriği siler)
"a"     Ekleme  (Eski içerik sonuna ekleme yapar )
"x"     Ekleme ama Olmayan bir dosya yaratıp ekler! Eğer aynı isimde dosya varsa hata verir!
        (w den farkı eğer bu isimde dosya varsa hata vermesi ekleme yapmaması)
"r+"     Okuma ve Yazma (it must be exist!)
"w+"     Okuma ve Yazma (Delete if there is something before)
"a+"     Okuma ve Yazma
"x+"     Okuma ve Yazma Ekleme ama Olmayan bir dosya yaratıp ekler Eğer aynı isimde dosya varsa hata verir

                  | r   r+   w   w+   a   a+
------------------|--------------------------
read              | +   +        +        +
write             |     +    +   +    +   +
write after seek  |     +    +   +
create            |          +   +    +   +
truncate          |          +   +
position at start | +   +    +   +
position at end   |                   +   +
"""

dosya = open("dene.txt", "a+")
dosya.write("Hello World\n")

dosya.seek(0)
print(dosya.read())

dosya.close()
"""
 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
"""


