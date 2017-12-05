import xlrd
import numpy


def get_worksheet(file_path):
  raw_book = xlrd.open_workbook(file_path,
                                formatting_info=True)
  return raw_book.sheet_by_index(0)


def get_dataset(file_path):
  worksheet = get_worksheet(file_path)
  dataset = []
  for row_index in range(1, worksheet.nrows):
    dataset.append([rowElement for rowElement in worksheet.row_values(row_index, 1) if rowElement])

  return dataset
