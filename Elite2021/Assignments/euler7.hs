{- By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 - What is the 10 001st prime number?-}

isPrime :: Integer -> Bool
isPrime num = length ([x | x <- [2..round(fromIntegral (quot num 2) )], (mod num x) == 0]) == 0
nthPrime n = [x | x <- [2..], isPrime x] !! n

main = do
    print (nthPrime 10001)
