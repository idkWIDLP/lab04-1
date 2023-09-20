from lib import count_common_elements


def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [5, 6, 7, 8, 9]
    
    print("Количество общих элементов:", count_common_elements(list1, list2, list3))



if __name__ == '__main__':
    main()