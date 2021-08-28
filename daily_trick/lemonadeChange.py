

class Solution(object):

    def lemonadeChange(self, bills):

        """

        贪心算法


        """

        five = 0  # 五元面值
        ten = 0  # 十元面值

        for bill in bills:

            if bill == 5:
                five += 1

            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif bill == 20:

                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five > 3:
                    five -= 3
                else:
                    return False
        return True