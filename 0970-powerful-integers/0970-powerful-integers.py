class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ## brute force for all of x while it is less than bound add value into hashtable 
        ## repeat for y, double for loop to pair them 

        x_map = {}
        x_curr, x_power = x ** 0, 0

        while x_curr <= bound:
            if x == 1:
                x_map[x_power] = x_curr
                break
            x_map[x_power] = x_curr
            x_power += 1
            x_curr = x ** x_power
        
        y_map = {}
        y_curr, y_power = y ** 0, 0

        while y_curr <= bound:
            if y == 1:
                y_map[y_power] = y_curr
                break
            y_map[y_power] = y_curr
            y_power += 1
            y_curr = y ** y_power
        
        output = set()
        for x_value in x_map.values():
            for y_value in y_map.values():
                if x_value + y_value <= bound:
                    output.add(x_value + y_value) 

        return list(output)

