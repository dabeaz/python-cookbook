# Different styles of raising chained exceptions

# Example 1:   Explicit chaining.  Use this whenever your
# intent is to raise a new exception in response to another

def example1():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e

# Example 2:  Implicit chaining.  This occurs if there's an
# unexpected exception in the except block.

def example2():
    try:
        int('N/A')
    except ValueError as e:
        print('It failed. Reason:', e)   # Intentional error

# Example 3: Discarding the previous exception
def example3():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from None

if __name__ == '__main__':
    import traceback
    print('****** EXPLICIT EXCEPTION CHAINING ******')
    try:
        example1()
    except Exception:
        traceback.print_exc()

    print()
    print('****** IMPLICIT EXCEPTION CHAINING ******')
    try:
        example2()
    except Exception:
        traceback.print_exc()

    print()
    print('****** DISCARDED CHAINING *******')
    try:
        example3()
    except Exception:
        traceback.print_exc()


