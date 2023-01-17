# 7.1

input_year = int(input('출생년도를 입력하세요: '))

year_lists = []
for year in range(1, 7):
    year_lists.append(year + input_year)
print(year_lists)

# 7.2
print(f'years_list의 세 번째 생일은 {year_lists[3]}년에 맞는다.')

# 7.3
print(f'years_list 중 가장 나이가 많을 때는 {year_lists[-1]}년이다.')