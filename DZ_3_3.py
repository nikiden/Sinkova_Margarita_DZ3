def thesaurus(*args):
    names = {}
    for name in args:
        f_letter = name[0]
        names[f_letter] = names.get(f_letter, [])
        names[f_letter].append(name)
    return names


print(thesaurus("Иван", "Мария", "Петр", "Илья","Джонни", "Дарья", "Александр", "Ольга"))

