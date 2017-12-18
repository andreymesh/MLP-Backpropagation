import xlrd
import pandas


def get_worksheet(file_path):
  raw_book = xlrd.open_workbook(file_path)
  return raw_book.sheet_by_index(0)


# black - 0
# blue - 1
# brown - 2
# gold - 3
# green - 4
# orange - 5
# red - 6
# white - 7

def get_dataset(file_path):
  worksheet = get_worksheet(file_path)
  dataset = []
  for row_index in range(1, worksheet.nrows):
    row = []
    for row_element in worksheet.row_values(row_index, 1):
      if row_element != '':
        if (row_element == 'black'):
          row.append(float(0))
        elif row_element == 'blue':
          row.append(float(1))
        elif (row_element == 'brown'):
          row.append(float(2))
        elif row_element == 'gold':
          row.append(float(3))
        elif (row_element == 'green'):
          row.append(float(4))
        elif (row_element== 'orange'):
          row.append(float(5))
        elif (row_element == 'red'):
          row.append(float(6))
        elif (row_element == 'white'):
          row.append(float(7))
        else:
          row.append(row_element)

        # print(row)

    dataset.append(row)

  # dataset.append([rowElement for if rowElement])

  return pandas.DataFrame(dataset)