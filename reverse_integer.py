class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1  # 2,147,483,647
        MIN_INT = -2**31     # -2,147,483,648

        reversed_num = 0

        # Work with the absolute value of x and determine the sign
        sign = 1 if x >= 0 else -1
        num = abs(x)

        while num != 0:
            # Get the last digit
            digit = num % 10

            # --- This is the crucial overflow check ---
            # Check if reversed_num is about to exceed the max value boundary
            # MAX_INT // 10 is 214748364
            if reversed_num > MAX_INT // 10 or (reversed_num == MAX_INT // 10 and digit > 7):
                return 0 # Overflow would occur

            # Build the reversed number
            reversed_num = reversed_num * 10 + digit

            # Remove the last digit from the original number
            num //= 10

        return sign * reversed_num
# ...existing code...
