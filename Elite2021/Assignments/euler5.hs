{- 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? -}

-- Approach 1 --
gcd_ x y = if y == 0 then x else gcd y (mod x y)
lcm_ x y = quot (x * y) (gcd_ x y)

-- foldl, foldr works same as reduce --
-- Realised lcm is an inbuilt function --

main = do
    -- Approach 1 --
    print (foldl (lcm_) 1 [1..20])
    -- Approach 2 --
    print (foldl lcm 1 [1..20])
