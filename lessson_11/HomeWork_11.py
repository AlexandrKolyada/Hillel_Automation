def sum_numbers_in_list(my_list):

    for line in my_list:
        sub_list = line.split(',')
        container = 0

        try:
            for item in sub_list:
                container += int(item)
            print(container)
        except ValueError:
            print("Не можу це зробити")

sum_numbers_in_list(["1,2,3,4", "1,2,3,4,50",  "qwerty1,2,3"])