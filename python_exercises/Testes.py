def remove_adjacent(nums):
    resultado = []
    if len(nums) > 1:
        resultado = [nums[0]]
    for num in nums:
        if num != resultado[-1]:
            resultado.append(num)
    
    print()
    print(resultado)
            

remove_adjacent([])