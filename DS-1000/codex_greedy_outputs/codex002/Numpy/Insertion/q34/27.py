
def check_degree_or_radian(number):
    degree_value = np.sin(number)
    radian_value = np.sin(np.radians(number))
    
    if degree_value > radian_value:
        return 0
    else:
        return 1

number = np.random.randint(0, 360)
print(check_degree_or_radian(number))
