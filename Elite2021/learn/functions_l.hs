{- addMe :: Int -> Int -> Int -}

addMe x y = x + y

-- | are called guards --
isOdd n
    | n `mod` 2 == 0 = False
    | otherwise = True

whatGrade marks
    | marks < 20 = "Fail"
    | marks < 40 = "Pass"
    | marks < 60 = "A+"
    | marks < 80 = "O"
    | otherwise = "Keep Going"

bat_avg hits atbats

    | avg < 20 = "Fail"
    | avg < 40 = "Pass"
    | avg < 60 = "A+"
    | avg < 80 = "O"
    | otherwise = "Keep Working"
    where avg = hits/atbats

getListItems :: [Int] -> String

getListItems [] = "Your list is empty"
getListItems (x:[]) = "Your list starts with " ++ show x
getListItems (x : y : []) = "Your list contains " ++ show x ++ " " ++ show y
getListItems (x : xs) = "Your list starts with " ++ show x ++ " followed by " ++ show xs

-- Recursion --
areStringsEq :: [Char] -> [Char] -> Bool

areStringsEq [] [] = True
areStringsEq (x : xs) (y : ys) = x == y && areStringsEq xs ys
areStringsEq _ _ = False


main = do
    print (addMe 2 3) 
