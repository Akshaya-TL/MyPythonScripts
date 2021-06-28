fib = 0 : 1 : zipWith (+) fib (tail fib)

main = do
     print (take 10 fib)
     print (take 20 fib)
