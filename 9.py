ans1 = input('Собака короткошерстной породы? ')
if ans1 == 'да':
    ans2 = input('Рост собаки менее 50см? ')
    if ans2 == 'да':
        ans3 = input('У собаки короткий хвост? ')
        if ans3 == 'да':
            print('английский бульдог')
        elif ans3 == 'нет':
            ans4 = input('У собаки длинные уши? ')
            if ans4 == 'да':
                print('гончая')
            elif ans4 == 'нет':
                ans5 = input('У собаки короткое тело? ')
                if ans5 == 'да':
                    print('мопс')
                else: print('чихуахуа')

    elif ans2 == 'нет':
        ans3 = input('Собака весит более 50кг? ')
        if ans3 == 'да':
            print('датский дог')
        else: print('фоксхаунд')

elif ans1 == 'нет':
    ans2 = input('Рост собаки менее 50см? ')
    if ans2 == 'да':
        ans3 = input('У собаки доброжелательный характер? ')
        if ans3 == 'да':
            print('кокер-спаниель')
        else: print('цвергшнауцер')

    elif ans2 == 'нет':
        ans3 = input('У собаки рост менее 70см? ')
        if ans3 == 'да':
            ans4 = input('У собаки длинные уши? ')
            if ans4 == 'да':
                print('большой вандейский грифон')
            else: print('колли')

        elif ans3 == 'нет':
            ans4 = input('Окрас собаки с белыми отметинами? ')
            if ans4 == 'да':
                print('сенбернар')
            elif ans4 == 'нет':
                ans5 = input('Белоснежный окрас? ')
                if ans5 == 'да':
                    print('ирландский волкодав')
                else:
                    print('ньюфаундленд')
