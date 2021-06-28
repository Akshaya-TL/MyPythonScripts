import Data.List
import Data.Char

smallest :: Int -> [Char]
smallest n = sort . show $n

largest :: Int -> [Char]
largest n = reverse . smallest $n

toInt :: [Char] -> Int
toInt n = read n

nextKaprekar :: Int -> Int
nextKaprekar n = (toInt (largest n))  -  (toInt (smallest n)) 

kaprekarSeq :: Int -> [Int]
kaprekarSeq n = nextKaprekar n : (kaprekarSeq (nextKaprekar n))

takeUntilDup :: [Int] -> [Int]
takeUntilDup [] = []
takeUntilDup [n] = [n]
takeUntilDup (n : ns) = if (n == (head ns)) then [n] else n : takeUntilDup (ns)

main = do
    print ([1344] ++ takeUntilDup(kaprekarSeq 1344))
