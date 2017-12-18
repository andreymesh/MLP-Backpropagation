import xlrd
import pandas


def get_worksheet(file_path):
    raw_book = xlrd.open_workbook(file_path,
                                  formatting_info=True)
    return raw_book.sheet_by_index(0)


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


def get_dataset(file_path):
    worksheet = get_worksheet(file_path)
    dataset = []
    for row_index in range(1, worksheet.nrows):
        row = []
        for row_element in worksheet.row_values(row_index, 1):
            if row_element != '':
                if (row_element == 'мужской') | (row_element == 'да') | (row_element == 'очень высокий') | (
                        row_element == 'курит') | (row_element == '1,00') | (row_element == '1.00') | (
                        row_element == 1):
                    row.append(float(1))
                elif row_element == 'высокий':
                    row.append(float(0.75))
                elif (row_element == 'умеренный') | (row_element == 'возможный'):
                    row.append(float(0.5))
                elif row_element == 'низкий':
                    row.append(float(0.25))
                elif (row_element == 'женский') | (row_element == 'нет') | (row_element == 'очень низкий') | (
                        row_element == 'не курит') | (row_element == '0,00') | (row_element == '0.00') | (
                        row_element == 0):
                    row.append(float(0))
                else:
                    row.append(row_element)

                # print(row)

        dataset.append(row)

    # dataset.append([rowElement for if rowElement])

    return pandas.DataFrame(dataset)