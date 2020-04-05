import pandas as pd
import math
#5개씩
kospiCSV22 = pd.read_csv('C:/stock/data/error/4/22/22UD.csv')
kospiCSV31 = pd.read_csv('C:/stock/data/error/4/31/31UD.csv')
#3개씩
kospiCSV33 = pd.read_csv('C:/stock/data/error/6/33/33UD.csv')
kospiCSV42 = pd.read_csv('C:/stock/data/error/6/42/42UD.csv')
#2개씩
kospiCSV44 = pd.read_csv('C:/stock/data/error/8/44/44UD.csv')
kospiCSV53 = pd.read_csv('C:/stock/data/error/8/53/53UD.csv')

for i in range(5):
    m = 0
    z = 0
    p = 0
    ga_gap_22 = 0
    nonga_gap_22 = 0
    ga22 = 0
    ga22_m = 0
    ga22_z = 0
    ga22_p = 0
    nonga22 = 0
    nonga22_m = 0
    nonga22_z = 0
    nonga22_p = 0
    # print(len(kospiCSV22['ga'+str(i)]))
    for j in range(1, len(kospiCSV22['ga'+str(i)])):
        if not math.isnan(kospiCSV22['ori' + str(i)][j]) :
            ga_gap_22 += abs(kospiCSV22['ori' + str(i)][j] - kospiCSV22['ga' + str(i)][j])
            nonga_gap_22 += abs(kospiCSV22['ori' + str(i)][j] - kospiCSV22['nonga' + str(i)][j])

        # print(str(i) + ' : ' + str(ga_gap_22))
        # print(nonga_gap_22)
        if kospiCSV22['ori' + str(i)][j] == -1:
            m += 1
        elif kospiCSV22['ori' + str(i)][j] == 0:
            z += 1
        elif kospiCSV22['ori' + str(i)][j] == 1:
            p += 1

        if kospiCSV22['ori'+str(i)][j] == kospiCSV22['ga'+str(i)][j]:
            ga22 += 1
            if kospiCSV22['ori'+str(i)][j] == -1:
                ga22_m += 1
            elif kospiCSV22['ori'+str(i)][j] == 0:
                ga22_z += 1
            elif kospiCSV22['ori' + str(i)][j] == 1:
                ga22_p += 1

        if kospiCSV22['ori'+str(i)][j] == kospiCSV22['nonga'+str(i)][j]:
            nonga22 += 1
            if kospiCSV22['ori'+str(i)][j] == -1:
                nonga22_m += 1
            elif kospiCSV22['ori'+str(i)][j] == 0:
                nonga22_z += 1
            elif kospiCSV22['ori' + str(i)][j] == 1:
                nonga22_p += 1

    # print(m+z+p)
    # print(str(i) + '_22 GA : ' + str(ga22))
    # print(str(i) + '_22 NonGA : ' + str(nonga22))
    # print('Origin - : ' + str(m), ", GA : " + str(ga22_m) + ', NonGA : ' + str(nonga22_m))
    # print('Origin 0 : ' + str(z), ", GA : " + str(ga22_z) + ', NonGA : ' + str(nonga22_z))
    # print('Origin + : ' + str(p), ", GA : " + str(ga22_p) + ', NonGA : ' + str(nonga22_p))
    print('ga_gap : ' + str(ga_gap_22) + ", nonga_gap : " + str(nonga_gap_22))

print('----------------------------------------------------------------------')
for i in range(5):
    m = 0
    z = 0
    p = 0
    ga31 = 0
    ga31_m = 0
    ga31_z = 0
    ga31_p = 0
    nonga31 = 0
    nonga31_m = 0
    nonga31_z = 0
    nonga31_p = 0
    ga_gap_31 = 0
    nonga_gap_31 = 0
    for j in range(1, len(kospiCSV31['ga' + str(i)])):
        if not math.isnan(kospiCSV31['ori' + str(i)][j]):
            ga_gap_31 += abs(kospiCSV31['ori' + str(i)][j] - kospiCSV31['ga' + str(i)][j])
            nonga_gap_31 += abs(kospiCSV31['ori' + str(i)][j] - kospiCSV31['nonga' + str(i)][j])
        if kospiCSV31['ori' + str(i)][j] == -1:
            m += 1
        elif kospiCSV31['ori' + str(i)][j] == 0:
            z += 1
        elif kospiCSV31['ori' + str(i)][j] == 1:
            p += 1

        if kospiCSV31['ori' + str(i)][j] == kospiCSV31['ga' + str(i)][j]:
            ga31 += 1
            if kospiCSV31['ori'+str(i)][j] == -1:
                ga31_m += 1
            elif kospiCSV31['ori'+str(i)][j] == 0:
                ga31_z += 1
            elif kospiCSV31['ori' + str(i)][j] == 1:
                ga31_p += 1

        if kospiCSV31['ori' + str(i)][j] == kospiCSV31['nonga' + str(i)][j]:
            nonga31 += 1
            if kospiCSV31['ori'+str(i)][j] == -1:
                nonga31_m += 1
            elif kospiCSV31['ori'+str(i)][j] == 0:
                nonga31_z += 1
            elif kospiCSV31['ori' + str(i)][j] == 1:
                nonga31_p += 1
        # ga_gap_31 += abs(kospiCSV31['ori' + str(i)][j] - kospiCSV31['ga' + str(i)][j])
        # nonga_gap_31 += abs(kospiCSV31['ori' + str(i)][j] - kospiCSV31['nonga' + str(i)][j])
    # print(m+z+p)
    # print(str(i) + '_31 GA : ' + str(ga31))
    # print(str(i) + '_31 NonGA : ' + str(nonga31))
    # print('Origin - : ' + str(m), ", GA : " + str(ga31_m) + ', NonGA : ' + str(nonga31_m))
    # print('Origin 0 : ' + str(z), ", GA : " + str(ga31_z) + ', NonGA : ' + str(nonga31_z))
    # print('Origin + : ' + str(p), ", GA : " + str(ga31_p) + ', NonGA : ' + str(nonga31_p))
    print('ga_gap : ' + str(ga_gap_31) + ", nonga_gap : " + str(nonga_gap_31))
################################################################################
print('----------------------------------------------------------------------')
for i in range(3):
    m = 0
    z = 0
    p = 0
    ga33 = 0
    ga33_m = 0
    ga33_z = 0
    ga33_p = 0
    nonga33 = 0
    nonga33_m = 0
    nonga33_z = 0
    nonga33_p = 0
    ga_gap_33 = 0
    nonga_gap_33 = 0
    for j in range(1, len(kospiCSV33['ga' + str(i)])):
        if not math.isnan(kospiCSV33['ori' + str(i)][j]) and not math.isnan(kospiCSV33['ga' + str(i)][j]) and not math.isnan(kospiCSV33['nonga' + str(i)][j]) :
            ga_gap_33 += abs(kospiCSV33['ori' + str(i)][j] - kospiCSV33['ga' + str(i)][j])
            nonga_gap_33 += abs(kospiCSV33['ori' + str(i)][j] - kospiCSV33['nonga' + str(i)][j])
        if kospiCSV33['ori' + str(i)][j] == -1:
            m += 1
        elif kospiCSV33['ori' + str(i)][j] == 0:
            z += 1
        elif kospiCSV33['ori' + str(i)][j] == 1:
            p += 1
        if kospiCSV33['ori' + str(i)][j] == kospiCSV33['ga' + str(i)][j]:
            ga33 += 1
            if kospiCSV33['ori'+str(i)][j] == -1:
                ga33_m += 1
            elif kospiCSV33['ori'+str(i)][j] == 0:
                ga33_z += 1
            elif kospiCSV33['ori' + str(i)][j] == 1:
                ga33_p += 1

        if kospiCSV33['ori' + str(i)][j] == kospiCSV33['nonga' + str(i)][j]:
            nonga33 += 1
            if kospiCSV33['ori'+str(i)][j] == -1:
                nonga33_m += 1
            elif kospiCSV33['ori'+str(i)][j] == 0:
                nonga33_z += 1
            elif kospiCSV33['ori' + str(i)][j] == 1:
                nonga33_p += 1
        # ga_gap_33 += abs(kospiCSV33['ori' + str(i)][j] - kospiCSV33['ga' + str(i)][j])
        # nonga_gap_33 += abs(kospiCSV33['ori' + str(i)][j] - kospiCSV33['nonga' + str(i)][j])
    # print(m+z+p)
    # print(str(i) + '_33 GA : ' + str(ga33))
    # print(str(i) + '_33 NonGA : ' + str(nonga33))
    # print('Origin - : ' + str(m), ", GA : " + str(ga33_m) + ', NonGA : ' + str(nonga33_m))
    # print('Origin 0 : ' + str(z), ", GA : " + str(ga33_z) + ', NonGA : ' + str(nonga33_z))
    # print('Origin + : ' + str(p), ", GA : " + str(ga33_p) + ', NonGA : ' + str(nonga33_p))
    print('ga_gap : ' + str(ga_gap_33) + ", nonga_gap : " + str(nonga_gap_33))
print('----------------------------------------------------------------------')
for i in range(3):
    m = 0
    z = 0
    p = 0
    ga42 = 0
    ga42_m = 0
    ga42_z = 0
    ga42_p = 0
    nonga42 = 0
    nonga42_m = 0
    nonga42_z = 0
    nonga42_p = 0
    ga_gap_42 = 0
    nonga_gap_42 = 0
    for j in range(1, len(kospiCSV42['ga' + str(i)])):
        if not math.isnan(kospiCSV42['ori' + str(i)][j]) and not math.isnan(kospiCSV42['ga' + str(i)][j]) and not math.isnan(kospiCSV42['nonga' + str(i)][j]) :
            ga_gap_42 += abs(kospiCSV42['ori' + str(i)][j] - kospiCSV42['ga' + str(i)][j])
            nonga_gap_42 += abs(kospiCSV42['ori' + str(i)][j] - kospiCSV42['nonga' + str(i)][j])
        if kospiCSV42['ori' + str(i)][j] == -1:
            m += 1
        elif kospiCSV42['ori' + str(i)][j] == 0:
            z += 1
        elif kospiCSV42['ori' + str(i)][j] == 1:
            p += 1
        if kospiCSV42['ori' + str(i)][j] == kospiCSV42['ga' + str(i)][j]:
            ga42 += 1
            if kospiCSV42['ori'+str(i)][j] == -1:
                ga42_m += 1
            elif kospiCSV42['ori'+str(i)][j] == 0:
                ga42_z += 1
            elif kospiCSV42['ori' + str(i)][j] == 1:
                ga42_p += 1

        if kospiCSV42['ori' + str(i)][j] == kospiCSV42['nonga' + str(i)][j]:
            nonga42 += 1
            if kospiCSV42['ori'+str(i)][j] == -1:
                nonga42_m += 1
            elif kospiCSV42['ori'+str(i)][j] == 0:
                nonga42_z += 1
            elif kospiCSV42['ori' + str(i)][j] == 1:
                nonga42_p += 1

        # ga_gap_42 += abs(kospiCSV42['ori' + str(i)][j] - kospiCSV42['ga' + str(i)][j])
        # nonga_gap_42 += abs(kospiCSV42['ori' + str(i)][j] - kospiCSV42['nonga' + str(i)][j])

    # print(m+z+p)
    # print(str(i) + '_42 GA : ' + str(ga42))
    # print(str(i) + '_42 NonGA : ' + str(nonga42))
    # print('Origin - : ' + str(m), ", GA : " + str(ga42_m) + ', NonGA : ' + str(nonga42_m))
    # print('Origin 0 : ' + str(z), ", GA : " + str(ga42_z) + ', NonGA : ' + str(nonga42_z))
    # print('Origin + : ' + str(p), ", GA : " + str(ga42_p) + ', NonGA : ' + str(nonga42_p))
    print('ga_gap : ' + str(ga_gap_42) + ", nonga_gap : " + str(nonga_gap_42))
##############################################################################
print('----------------------------------------------------------------------')
for i in range(2):
    m = 0
    z = 0
    p = 0
    ga44 = 0
    ga44_m = 0
    ga44_z = 0
    ga44_p = 0
    nonga44 = 0
    nonga44_m = 0
    nonga44_z = 0
    nonga44_p = 0
    ga_gap_44 = 0
    nonga_gap_44 = 0
    for j in range(1, len(kospiCSV44['ga' + str(i)])):
        if not math.isnan(kospiCSV44['ori' + str(i)][j]) and not math.isnan(kospiCSV44['ga' + str(i)][j]) and not math.isnan(kospiCSV44['nonga' + str(i)][j]) :
            ga_gap_44 += abs(kospiCSV44['ori' + str(i)][j] - kospiCSV44['ga' + str(i)][j])
            nonga_gap_44 += abs(kospiCSV44['ori' + str(i)][j] - kospiCSV44['nonga' + str(i)][j])

        if kospiCSV44['ori' + str(i)][j] == -1:
            m += 1
        elif kospiCSV44['ori' + str(i)][j] == 0:
            z += 1
        elif kospiCSV44['ori' + str(i)][j] == 1:
            p += 1

        if kospiCSV44['ori' + str(i)][j] == kospiCSV44['ga' + str(i)][j]:
            ga44 += 1
            if kospiCSV44['ori'+str(i)][j] == -1:
                ga44_m += 1
            elif kospiCSV44['ori'+str(i)][j] == 0:
                ga44_z += 1
            elif kospiCSV44['ori' + str(i)][j] == 1:
                ga44_p += 1

        if kospiCSV44['ori' + str(i)][j] == kospiCSV44['nonga' + str(i)][j]:
            nonga44 += 1
            if kospiCSV44['ori'+str(i)][j] == -1:
                nonga44_m += 1
            elif kospiCSV44['ori'+str(i)][j] == 0:
                nonga44_z += 1
            elif kospiCSV44['ori' + str(i)][j] == 1:
                nonga44_p += 1
        # ga_gap_44 += abs(kospiCSV44['ori' + str(i)][j] - kospiCSV44['ga' + str(i)][j])
        # nonga_gap_44 += abs(kospiCSV44['ori' + str(i)][j] - kospiCSV44['nonga' + str(i)][j])
    # print(m+z+p)
    # print(str(i) + '_44 GA : ' + str(ga44))
    # print(str(i) + '_44 NonGA : ' + str(nonga44))
    # print('Origin - : ' + str(m), ", GA : " + str(ga44_m) + ', NonGA : ' + str(nonga44_m))
    # print('Origin 0 : ' + str(z), ", GA : " + str(ga44_z) + ', NonGA : ' + str(nonga44_z))
    # print('Origin + : ' + str(p), ", GA : " + str(ga44_p) + ', NonGA : ' + str(nonga44_p))
    print('ga_gap : ' + str(ga_gap_44) + ", nonga_gap : " + str(nonga_gap_44))
print('----------------------------------------------------------------------')
for i in range(2):
    m = 0
    z = 0
    p = 0
    ga53 = 0
    ga53_m = 0
    ga53_z = 0
    ga53_p = 0
    nonga53 = 0
    nonga53_m = 0
    nonga53_z = 0
    nonga53_p = 0
    ga_gap_53 = 0
    nonga_gap_53 = 0
    for j in range(1, len(kospiCSV53['ga' + str(i)])):
        if not math.isnan(kospiCSV53['ori' + str(i)][j]) and not math.isnan(kospiCSV53['ga' + str(i)][j]) and not math.isnan(kospiCSV53['nonga' + str(i)][j]) :
            ga_gap_53 += abs(kospiCSV53['ori' + str(i)][j] - kospiCSV53['ga' + str(i)][j])
            nonga_gap_53 += abs(kospiCSV53['ori' + str(i)][j] - kospiCSV53['nonga' + str(i)][j])
        if kospiCSV53['ori' + str(i)][j] == -1:
            m += 1
        elif kospiCSV53['ori' + str(i)][j] == 0:
            z += 1
        elif kospiCSV53['ori' + str(i)][j] == 1:
            p += 1

        if kospiCSV53['ori' + str(i)][j] == kospiCSV53['ga' + str(i)][j]:
            ga53 += 1
            if kospiCSV53['ori'+str(i)][j] == -1:
                ga53_m += 1
            elif kospiCSV53['ori'+str(i)][j] == 0:
                ga53_z += 1
            elif kospiCSV53['ori' + str(i)][j] == 1:
                ga53_p += 1
        if kospiCSV53['ori' + str(i)][j] == kospiCSV53['nonga' + str(i)][j]:
            nonga53 += 1
            if kospiCSV53['ori'+str(i)][j] == -1:
                nonga53_m += 1
            elif kospiCSV53['ori'+str(i)][j] == 0:
                nonga53_z += 1
            elif kospiCSV53['ori' + str(i)][j] == 1:
                nonga53_p += 1
        # ga_gap_53 += abs(kospiCSV53['ori' + str(i)][j] - kospiCSV53['ga' + str(i)][j])
        # nonga_gap_53 += abs(kospiCSV53['ori' + str(i)][j] - kospiCSV53['nonga' + str(i)][j])

    # print(m+z+p)
    # print(str(i) + '_53 GA : ' + str(ga53))
    # print(str(i) + '_53 NonGA : ' + str(nonga53))
    # print('Origin - : ' + str(m), ", GA : " + str(ga53_m) + ', NonGA : ' + str(nonga53_m))
    # print('Origin 0 : ' + str(z), ", GA : " + str(ga53_z) + ', NonGA : ' + str(nonga53_z))
    # print('Origin + : ' + str(p), ", GA : " + str(ga53_p) + ', NonGA : ' + str(nonga53_p))
    print('ga_gap : ' + str(ga_gap_53) + ", nonga_gap : " + str(nonga_gap_53))

