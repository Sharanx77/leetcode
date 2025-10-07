class Solution:
    def myAtoi(self, s):
        """
        Converts a string to a 32-bit signed integer.
        """
        # Define 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)
        sign = 1
        result = 0

        # 1. Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check for sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Read digits and convert, checking for overflow
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Check for overflow BEFORE updating the result
            # If result > INT_MAX // 10, then result * 10 will surely overflow.
            # If result == INT_MAX // 10, it overflows if the new digit > 7.
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
            
        # 4. Apply the sign and return
        return sign * result 
