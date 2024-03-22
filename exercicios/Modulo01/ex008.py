m = float(input('Digite uma medida em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
#print (f'{m} metros corresponde a:\n{km}KM\n{hm}HM\n{dam}DAM\n{dm}dm\n{cm}CM e\n{mm}MM')
print ('{} metros corresponde a:\n\033[1m{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm e\n{:.0f}mm\033[m'.format(m, km, hm, dam, dm, cm, mm))