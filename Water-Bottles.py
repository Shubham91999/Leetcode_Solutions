class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        self.drank = numBottles

        def drink(num: int) -> int:

            if num // numExchange == 0:
                return self.drank

            self.drank += (num // numExchange)

            return drink((num % numExchange) + (num // numExchange))

        return drink(numBottles)
        
        """
        # Math
        return numBottles + (numBottles - 1) // (numExchange - 1)



            

        

