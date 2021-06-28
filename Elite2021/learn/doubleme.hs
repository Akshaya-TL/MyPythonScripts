doubleMe :: [Int] -> [Int]
doubleMe [] = []
doubleMe (x : xs) = 2*x : doubleMe xs

main = do
    print (doubleMe [1,2,3,4])
