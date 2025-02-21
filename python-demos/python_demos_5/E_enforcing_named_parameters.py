
def print_vat(*, gross=0, vatpc=17.5, message='Summary:'):
   net = gross/(1 + (vatpc/100))
   vat = gross - net
   print(message, 'Net: {0:5.2f} Vat: {1:5.2f}'.format(net, vat))


print_vat(vatpc=15, gross=9.55)
print_vat()

# attempt to call the function without naming the params
# print_vat(9.55, 20, 'Info:')
