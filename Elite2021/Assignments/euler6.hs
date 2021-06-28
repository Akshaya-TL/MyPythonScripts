{- sum square difference. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. -}

sumOfSqrs limit = sum (map (^2) [1..limit])
sqrsOfSum limit = (sum [1..limit])^2
sumSqrDiff limit = abs ((sumOfSqrs limit) - (sqrsOfSum limit))

--sqrsOfSum limit = (quot (limit * (limit + 1))  2) ** 2--

main = do
    print (sumSqrDiff 100)
