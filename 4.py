#  Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) % c


alpha = 5
beta = 10
gamma = 15
first_block = (alpha - beta) * gamma
second_block = alpha + beta
third_block = first_block / second_block
final_block = third_block % gamma
print(final_block)
