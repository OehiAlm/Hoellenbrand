from time import time
from tomsTestRange import uplo

start = time()
for x in range(100):
    print("We have {0[0]} upper case letters, {0[1]} lower case letters".format(uplo("test_test_test")))
end = time()
print(f'It took {end - start} seconds to run this!')