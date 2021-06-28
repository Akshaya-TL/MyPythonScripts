{- 1> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these      multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.-}

-- Function for Approach 1 --
multiplesOfK :: Int -> [Int]
multiplesOfK k = [x | x <- [k, 2*k..999]]

-- Functions for Approach 2 --
greatestMultiplier :: Int -> Int
greatestMultiplier x = quot 999 x

sumMultiplesOfK ::  Int -> Int
sumMultiplesOfK k = ((n*(n+1)) `quot` 2) * k where n = greatestMultiplier k
   
main = do
    --Approach 1 --
    print ((sum (multiplesOfK 3)) + (sum (multiplesOfK 5)) - (sum (multiplesOfK 15)))
    
    --Approach 2--  
    print (sumMultiplesOfK 3 + sumMultiplesOfK 5 -  sumMultiplesOfK 15)
          
    
