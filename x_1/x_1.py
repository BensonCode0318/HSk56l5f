class Phone(object):
    def __init__(self, price = 0, camera_count = 0, screen_size = 0):
        """
        :type price : int
        :type camera_count : int
        :type screen_size : int 
        """

        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size
    
    def special_freature(self):
        pass
        
class GooglePhone(Phone):
    def __init__(self, price = 10, camera_count = 3, screen_size = 5):
        super().__init__()
    def special_freature(self, num_list):
        """
        :type num_list : list[int]
        :rtype result : list[int]
        """
        result = [num for num in num_list if num > 10 and num % 2 == 0]
        result.sort(reverse = True)
        return result

"""
Testing
"""
APhone = GooglePhone()
print(APhone.special_freature([3, 43, 62, 15, 18, 22]))



from math import factorial

class TaiwanPhone(Phone):
    def __init__(self, price = 20, camera_count = 1, screen_size = 3):
        super().__init__()

    def fib(self, num):
        """
        :type num : int
        :rtype : int
        """
        if num < 2 :
            return num
        else:
            return self.fib(num-1) + self.fib(num-2)

    def special_freature(self, num):
        """
        :type num : int
        :rtype : int
        """

        x = self.fib(num) % 100 // 10
        y = self.fib(num) % 10
        
        if x < y :
            return 'Fibonacci數列計算結果，十位數 x 小於 個位數 y，無法從中進行排列組合'
        else:
            return factorial(x) // factorial(x-y)
    

"""
Testing
"""
BPhone = TaiwanPhone()
print(BPhone.special_freature(13))

        

