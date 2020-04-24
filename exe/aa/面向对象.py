# class Washer():
#     def wash(self):
#         print('洗')
#
# haier = Washer()
# print(haier)
#
# haier.wash()

class Washer():
    def wash(self):
        print('aaaa')


    def print_info(self):

        print(f'aaaa{self.w}')
        print(f'cccc{self.h}')

haier1 = Washer()

haier1.w = 200
haier1.h = 300

haier1.print_info()