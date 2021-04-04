# 1
musicians = ['Гітарист', 'Барабанщик', 'Піаніст', 'Вокаліст']
for musician in musicians:
    print (musician)

# 2
group_month_money = 100
group_year_money = group_month_money * 12
print (group_year_money)

# 3
group_name = 'Пайтон на гітарі'
hits = ['Пайтон і джунглі', 'Прінт та вивід на консоль моїх емоцій', 'Інпут свій настрій']
for hit in hits:
    print (hits.index(hit) + 1, hit)

# 4
like = 123
likes = 0
time = 6
i = 0
while i < time:
    print (i, 'Час', likes, 'лайков')
    likes += like
    i += 1