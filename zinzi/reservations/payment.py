from iamport import Iamport

iamport = Iamport(imp_key='6343293486082258',
                  imp_secret='JEAB6oXOMsc2oysgdu4tJzlfgQvn5sfP7Qqefn21Qe3fNwv11zuL9Q0qGvNMY2B6T1l8pn9fCdvpK0rL')
response = iamport.find(imp_uid='imp_131520085919')
print(response)
