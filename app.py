# Function to convert number to words
def number_to_words(num):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", 
                 "Septillion", "Octillion", "Nonillion", "Decillion"]

    def helper(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif 10 < n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + " " + ones[n % 10]
        else:
            return ones[n // 100] + " Hundred " + helper(n % 100)

    if num == 0:
        return "Zero"
    
    result = ""
    i = 0
    while num > 0:
        if num % 1000 != 0:
            result = helper(num % 1000) + " " + thousands[i] + " " + result
        num //= 1000
        i += 1

    return result.strip()

# Example usage
num = int(input("Enter a number: "))
print(number_to_words(num))
