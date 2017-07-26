from ys_parser import ys

test = ys('https://www.google.fr')
#print test.data

test.setUrlsREG(0)
c_data = test.getUrlsREG()

test.saveData('test.txt',c_data)

print 'end'