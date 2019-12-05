from multiprocessing import Process
def cube(my_numbers):
   for x in my_numbers:
      print('%s cube  is  %s' % (x, x**3))
if __name__ == '__main__':
   my_numbers2 = [3, 4, 5, 6, 7, 8]
   p = Process(target=cube, args=(my_numbers2,))
   p.start()
   p.join
   print ("Done")