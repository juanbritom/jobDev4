
def main():
    sp = 67836.43
    rj = 36678.66
    mg = 29229.88
    es = 27165.48
    ot = 19849.53

    fat = sp+rj+mg+es+ot
    print("Em relação ao faturamento total, SP obteve {:.2%}, enquanto RJ, MG e ES obtiveram {:.2%}, {:.2%} e {:.2%} respectivamente, seguidos de outros estados com {:.2%}".format((sp/fat), (rj/fat), (mg/fat), (es/fat), (ot/fat)))


if __name__ == "__main__":
    main()