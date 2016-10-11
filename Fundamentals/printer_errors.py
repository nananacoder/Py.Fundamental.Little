'''
In a factory a printer prints labels for boxes.
For one kind of boxes the printer has to use colors which,
for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string.
For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a,
four times color b, then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced
e.g. aaaxbbbbyyhwawiwjjjwwm.

You have to write a function printer_error
which given a string will output the error rate of the printer as a string representing a rational whose numerator is the number of errors
and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

Examples:

s="aaabbbbhaijjjm"
error_printer(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"

Test.describe("printer_error")
Test.it("Basic tests")
s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
Test.assert_equals(printer_error(s), "3/56")

'''

def printer_error(s):
    sum1 = str(len(s))
    n = list(s)
    m = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    num = sum([1 for i in n if i not in m])
    result = str(num) + '/' + sum1
    return result

def printer_error_3(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

from re import sub
def printer_error_2(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

def printer_error_5(s):
    import re
    return str(len(re.findall('[n-z]', s))) + "/" + str(len(s))

def printer_error_4(s):
    return "%s/%s" % (len(s.translate(None, "abcdefghijklm")), len(s))

s="aaaxbbbbyyhwawiwjjjwwm"
print printer_error(s)

