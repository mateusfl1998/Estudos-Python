def donuts(count):
    if count <= 10: 
        print(f'Number of donuts: {count}')
    elif count > 10:
        print(f'Number of donuts: many')
    return count

donuts(99)