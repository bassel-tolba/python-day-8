test_h = int(input("height of wall:  ")) 
test_w = int(input("width of wall:  ")) 
coverage = 5

def paint_calc(height, width, cover):
    cans = (height * width) / cover
    cans_round = round(cans)
    if cans_round < cans:
        cans_round += 1
        
    print(f"you will need {cans_round} cans of paint.")


paint_calc(height = test_h, width = test_w, cover = coverage)