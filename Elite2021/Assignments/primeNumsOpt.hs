divides :: Int -> Int -> Bool
divides f n = rem n f == 0

iSqrt :: Int -> Int
iSqrt = floor . sqrt . fromIntegral

-- ldf n a returns the divisor of n (including n) >= a
ldf n a | divides a n = a
ldf n a | a * a > n   = n
ldf n a | otherwise   = ldf n (a + 1)

-- ld n returns the smallest divisor of n
ld ::Int -> Int
ld n = ldf n 2

isPrime :: Int -> Bool
isPrime 1 = False
isPrime n = ld n == n

primeNumbers :: Int -> [Int]
primeNumbers n = filter isPrime [1..n]

factorize :: Int -> [Int]
factorize n = factorize' n 2

factorize' :: Int -> Int -> [Int]
factorize' n f | f * f > n = [n]
factorize' n f | divides f n = f : factorize' (quot n f) f
factorize' n f | otherwise   = factorize' n (f + 1) 

main = do
    print $ factorize 13195
    print $ factorize 600851475143
