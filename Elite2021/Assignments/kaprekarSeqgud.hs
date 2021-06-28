import Data.List

smallest :: Int -> Int
smallest = read.sort.show

largest :: Int -> Int
largest = read.reverse.sort.show

nextKap :: Int -> Int
nextKap n = largest n - smallest n

kapSequence :: Int -> [Int]
kapSequence = iterate nextKap

takeUntilDup :: [Int] -> [Int]
takeUntilDup [] = []
takeUntilDup (x : xs) = if x == head xs then [x] else x : takeUntilDup(tail xs)

main = do
    print (takeUntilDup $ kapSequence 1786)
