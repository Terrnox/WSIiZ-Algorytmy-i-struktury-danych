def odw_tab(tab, ind_p, ind_k):
    if ind_p > ind_k:
        return tab
    tmp = tab[ind_k]
    tab[ind_k] = tab[ind_p]
    tab[ind_p] = tmp
    return odw_tab(tab, ind_p + 1, ind_k - 1)


tab = [1, 2, 3, 4, 5]
dl = len(tab) - 1
print(odw_tab(tab, 0, dl))