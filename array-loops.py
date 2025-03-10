nums = [2, 3, 5, -12,]

#print("Toto jsou čísla:")
#print(nums)

#print(f"0:{nums[0]}")
#print(f"1:{nums[1]}")
#print(f"2:{nums[2]}")

def array_sum(items):
    sum_item = 0
    for item in items :
        sum_item += item
    return sum_item

sumNums = array_sum(nums)
print(f"sum: {sumNums}")




## Výpočet maxima

def array_max(items):
    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item


maxNums = array_max(nums)
print(f"Max: {maxNums}")


## Výpočet minima

def array_min (items):
    min_item = items[0]
    for item in items[1:]:
        if item < min_item:
            min_item = item
    return min_item

minNum = array_min(nums)
print(f"Min: {minNum}")

minNum2 = array_min([-4,9,5,3])
print(f"Min: {minNum2}")