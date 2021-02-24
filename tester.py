# [None, None], [None, True], [True, None] Will be successful
# [True, True] Will be unsuccessful
result = [True, True]

# Just another safeguard to insure a problem hasn't occured in unit placement 
# Reason for not 'if result[0] == result[1]:' is because they could both be None, which is fine.
if None not in result:
    raise Exception("Error has occured during draw: Red unit and blue unit coexist on one tile")
else:
    print(result)