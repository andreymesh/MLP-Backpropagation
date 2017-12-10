# мужской - 1
# женский - 0
# да - 1
# нет - 0
# возможный - 0.5
# очень высокий - 1
# высокий - 0.75
# умеренный - 0.5
# низкий - 0.25
# очень низкий - 0
# курит - 1
# не курит - 0

def y_encoding(input_list):
    encoded_list = []
    for list_element in input_list:
        if list_element == 'да':
            encoded_list.append(1)
        else:
            encoded_list.append(0)

    return encoded_list


def x_encoding(input_list):
    encoded_list = []
    for row in input_list:
        encoded_row = []
        for row_element in row:
            if (row_element == 'мужской') | (row_element == 'да') | (row_element == 'очень высокий') | (
                    row_element == 'курит') | (row_element == '1,00'):
                encoded_row.append(1)
            elif row_element == 'высокий':
                encoded_row.append(0.75)
            elif (row_element == 'умеренный') | (row_element == 'возможный'):
                encoded_row.append(0.5)
            elif row_element == 'низкий':
                encoded_row.append(0.25)
            elif (row_element == 'женский') | (row_element == 'нет') | (row_element == 'очень низкий') | (
                    row_element == 'не курит') | (row_element == '0,00'):
                encoded_row.append(0)
            else:
                encoded_row.append(row_element)

        encoded_list.append(encoded_row)
    return encoded_list
