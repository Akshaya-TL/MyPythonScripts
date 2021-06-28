next :: Int -> Int
-- next n = if even n then (quot n 2) else (3 * n + 1) --
next n | even n   = quot n 2    -- even n is pattern--
next n | otherwise = 3 * n + 1

{- next n |
 -    even n = quot n 2
 -    otherwise 3*n+1
 -    -}
 
collatz :: Int -> [Int]
collatz 4 = [4, 2, 1]  --pattern matching--
collatz n = n : collatz (next n)

-- collatz n = if n == 4 then [4,2,1] else (n : collatz (next n))--
--
main = do
    print $ collatz 7
    print $ collatz 1
    -- $ indicates (all the elements from $ to the end of line )
