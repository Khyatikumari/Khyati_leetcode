class Solution(object):
    def multiply(self, num1, num2):
        digit_map={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        n1=0
        for num in num1:
            n1=(n1*10)+digit_map[num]
        n2=0
        for i in num2:
            n2=(n2*10)+digit_map[i]
        return str(n1*n2)
        