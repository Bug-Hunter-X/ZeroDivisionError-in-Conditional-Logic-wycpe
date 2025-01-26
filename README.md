# ZeroDivisionError in Conditional Logic
This example demonstrates a common error that can easily be missed, which is a ZeroDivisionError that occurs when there's an unexpected 0 in the denominator of division operation within a conditional statement.

The initial function appears to handle cases where either 'a' or 'b' is 0, returning the other value. However, the implicit assumption is that both 'a' and 'b' cannot be simultaneously 0.  If that happens, the last 'else' block will still execute, resulting in a ZeroDivisionError.

The solution involves improving the conditional logic to specifically check if the denominator is 0 before attempting division.