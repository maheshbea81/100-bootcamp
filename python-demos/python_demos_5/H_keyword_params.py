def print_vat(**kwargs):
   print(kwargs)
   net = kwargs['gross']/(1 + (kwargs['vatpc']/100))
   vat = kwargs['gross'] - net
   print(kwargs['message'], 'Net: {0:5.2f} Vat: {1:5.2f}'.format(net, vat))
   print("#" * 30)


# pass in named parameters that match the expected keywords within the function
print_vat(vatpc=15, gross=9.55, message='Summary')

# define a dictionary with keys that match the expected keywords within the function
argsdict = dict(vatpc=20, gross=15.99, message='Output')
print_vat(**argsdict)
