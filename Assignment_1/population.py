


population = 80000


men_percent = 52
literate_percent = 48
literate_men_percent = 35


men = (men_percent / 100) * population
women = population - men


literate_men = (literate_men_percent / 100) * population
total_literate = (literate_percent / 100) * population
literate_women = total_literate - literate_men


illiterate_men = men - literate_men
illiterate_women = women - literate_women

print(f"Illiterate Men: {int(illiterate_men)}")

print(f"Illiterate Women: {int(illiterate_women)}")

