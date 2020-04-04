                                  #DJANGO

Masaüstünde klasör yarat : blog <br>
Open cmd in there (Klasör adres çubuğuna gel ve cmd yaz orada açar cmd yi)<br>
`C:\Users\Demir\Desktop\blog>pip install virtualenv`<br>
`C:\Users\Demir\Desktop\blog> virtualenv venv`		//venv isimli bir klasör yarattı<br>
`C:\Users\Demir\Desktop\blog> venv\Scripts\activate`	// aktif ettik sanal zımbırtıyı<br>
`(venv) C:\Users\Demir\Desktop\blog>` 			//En başta env görüyorsan olmuştur.<br>
`(venv) C:\Users\Demir\Desktop\blog>deactivate`	// yazarak kapatıyoruz sanal zımbırtıyı. <br>
Sanal python ortamını kurmamdaki amaç ana python dosyamdan ayırmam projemi. Bir izalasyon yaratmam.<br>
`C:\Users\Demir\Desktop\blog> venv\Scripts\activate`	// aktif ettik sanal zımbırtıyı<br>
`(venv) C:\Users\Demir\Desktop\blog>pip install django`<br>
`(venv) C:\Users\Demir\Desktop\blog> django-admin startproject blog .`		// proje yaratıldı.<br>
     ..*Şimdi pycharmda blog adlı projemizi açalım ve settings en altta dil te zaman Europe/Istanbul yapalım<br>
     ..*dJango bize sunucu desteğide sağlıyor.<br>
`(venv) C:\Users\Demir\Desktop\blog> dir`	// baktık manage dosyası burada mı diye.<br>
      ..*04/04/2020  22:25    <DIR>          .idea<br>
      ..*04/04/2020  22:25    <DIR>          blog<br>
      ..*04/04/2020  22:08               645 manage.py<br>
`(venv) C:\Users\Demir\Desktop\blog>python manage.py runserver`  //	Serverı çalıştırdık<br>
`…`
`Django version 3.0.5, using settings 'blog.settings`<br>
`Starting development server at http://127.0.0.1:8000/`<br>
`…`
..*http://127.0.0.1:8000/ ADRESİNİ TARAYICINA GİR VE MUHTEŞEM SONUCU GÖR 😊<br>
Komut satırından Ctrl+c  ile  server sonlandırılabilir.<br>
`(venv) C:\Users\Demir\Desktop\blog>python manage.py runserver 8080`  //8080 Por numarasından erişilebilir yapabilirsin.<br>
	`…`
	..*Starting development server at http://127.0.0.1:8080/`<br>
	`…`
