-- digits :: Int -> [Int] --
digits 0 = []
digits n = digits (quot n 10) ++ [(rem n 10)]

powers :: [Int] -> Int -> [Int]
powers d n = map (^n) d

isArmstrong :: Int -> Bool
isArmstrong n = n == sum (powers d (length d)) where d = digits n)

genArmstrong :: Int -> Int -> [Int]
genArmstrong n n' = filter isArmstrong [n..n']

main = do 
    print $ genArmstrong 100 1000
    print $ genArmstrong 1000 10000
