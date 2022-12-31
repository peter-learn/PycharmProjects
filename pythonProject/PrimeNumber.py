
# def Prime_number(a,b=0):
#     P = []
#     F = []
#     for i in range(a):
#         print('_________________1_O_______________')
#         print('i = ',i)
#         for j in range(i):
#             print('          _______2_O_______________')
#             print('j = ',j)
#             if j > 0:
#                 print(j>0)
#                 if a%(j+1) == 0:
#                     print('a%(j+1) = ',a%(j+1))
#                     F.append(j)
#                     print('F = ',F)
#         if len(F) == 2:
#             P.append(i)
#             print('P = ',P)
#     return P
def Prime_number(a,b=0):
    # P = []
    TF = ''
    F = []
    for i in range(a):

            if a%(i+1) == 0:
                F.append(i+1)
    if F[0] == 1 and F[1]==a:
        # P.append(a)
        TF = 'yes'
    else:
        TF = 'no'

    return TF

a = Prime_number(2147483647)
print(a)
