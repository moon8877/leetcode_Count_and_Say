class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        init = 0
        def convert(number):
            string = ""
            temp_count = 1       #how many contiguous same number
            temp_number = 0      #the first number or next different number
            for j in range(len(number)):
                if(j == 0):
                    temp_number = number[j]
                else:
                    if(number[j] != temp_number):
                        string = string + str(temp_count) +str(temp_number)
                        temp_count = 1
                        temp_number = number[j]
                    else:
                        temp_count = temp_count + 1
            string = string + str(temp_count) +str(number[j])   
            return string
        for i in range(n):
            if(i == 0):
                init = "1"
            elif(i == 1):
                init = "11"
            else:
                init = convert(init)
        return str(init)
        