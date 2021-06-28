{- The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 - Find the sum of all the primes below two million-}

isPrime :: Int -> Bool
isPrime x = (length (filter(\y -> (mod x y) == 0) [2..(quot x 2)])) == 0
primesBelow_n num = [x | x <- [2..num], isPrime x]

main = do
    print (sum (primesBelow_n 2000000))

