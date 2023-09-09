# split the input into day and month
x = input().split()
day = int(x[0])
month = x[1].lower()

januari = maret = mei = juli = agustus = oktober = desember = a = 31
februari = b = 28
april = juni = september = november = c = 30

n_day = 0
if month == 'januari':
    n_day = day
    print(f'{n_day} hari')
elif month == 'februari':
    n_day = januari + day
    print(f'{n_day} hari')
elif month == 'maret':
    n_day = januari + februari + day
    print(f'{n_day} hari')
elif month == 'april':
    n_day = januari + februari + maret + day
    print(f'{n_day} hari')
elif month == 'mei':
    n_day = januari+februari+maret+april+ day
    print(f'{n_day} hari')
elif month == 'juni':
    n_day = januari+februari+maret+april+mei+ day
    print(f'{n_day} hari')
elif month == 'juli':
    n_day = januari+februari+maret+april+mei+juni+ day
    print(f'{n_day} hari')
elif month == 'agustus':
    n_day = januari+februari+maret+april+mei+juni+juli+ day
    print(f'{n_day} hari')
elif month == 'september':
    n_day = januari+februari+maret+april+mei+juni+juli+agustus+ day
    print(f'{n_day} hari')
elif month == 'oktober':
    n_day = januari+februari+maret+april+mei+juni+juli+agustus+september+day
    print(f'{n_day} hari')
elif month == 'november':
    n_day = januari+februari+maret+april+mei+juni+juli+agustus+september+oktober+day
    print(f'{n_day} hari')
elif month == 'desember':
    n_day = januari+februari+maret+april+mei+juni+juli+agustus+september+oktober+november+day
    print(f'{n_day} hari')
else:
    print("Error")
    