{- The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ? -}

import primeNumsOpt


isPrime :: Int -> Bool
isPrime x = (length (filter(\y -> (mod x y) == 0) [1..(quot x 2)])) == 1
primeFactors num = filter (isPrime) (concat [x:[quot num x] | x <- [2..round(sqrt (fromIntegral num))],(mod num x) == 0])
largestPrime num = maximum (primeFactors num)

main = do
    print (largestPrime 600851475143)
     
