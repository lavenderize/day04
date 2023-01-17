# 7.1

input_year = int(input('출생년도를 입력하세요: '))

year_lists = []
for year in range(1, 7):
    year_lists.append(year + input_year)
print(year_lists)