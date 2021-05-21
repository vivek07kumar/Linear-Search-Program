def linear_search(user_list,user_search_element) :
    index = 0
    position_list = []
    for x in user_list :
        if x == user_search_element :
            position_list = position_list + [index]
        index = index + 1
    if len(position_list) == 0 :
        return None
    else :
        return position_list
def main() :
    user_input = list(eval(input('>> Please enter Numbers seperated by Comma : ')))
    print()
    user_input_2 = eval(input('>> Please a enter Number to find its position in list : '))
    result = linear_search(user_input,user_input_2)
    print()
    if result == None :
        print('>>  No Such Element Found In The List !  <<')
    else :
        print('>> ',user_input_2,'is present at following index position/s : ',result)
        print()
        print('>> Total Number of "',user_input_2,'" Found : ',len(result))
        print()
main()
