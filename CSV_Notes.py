import csv


def validate(num: str):
    num_length = len(num)
    if num_length == 16:
        return True
    else:
        print("* Not every number here is 16 digits long; therefore, I cannot handle this.")
        return False


def reverse_it(string):
    string_backwards = string[::-1]
    print(string_backwards)


reverse_it("Hello, world!")


# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print("* Writing...")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#             old_number = int(row[0])
#             new_number = old_number + 1
#             row[0] = new_number
#             writer.writerow(row)
#             print(int(old_number) + 1)
#             print(old_number)
# print("* Then, it is done.")

# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print("* Writing...")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#
#         for row in reader:
#             old_number = row[0]
#             first_num = int(old_number[0])
#             if first_num % 2 == 0:
#                 writer.writerow(row)
#             # print(int(old_number) + 1)
#             # print(old_number)
# print("* Then, it is done.")

with open("Book1.csv", 'r') as old_csv:
    with open("FourFile.csv", 'w', newline='') as new_csv:
        print("* Writing...")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)

        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
print("* Then, it is done.")