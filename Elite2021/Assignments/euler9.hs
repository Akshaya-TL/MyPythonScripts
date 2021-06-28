{- A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
   a2 + b2 = c2
   For example, 32 + 42 = 9 + 16 = 25 = 52.
   There exists exactly one Pythagorean triplet for which a + b + c = 1000.
   Find the product abc. -}

pythagoreanTriplet total =  [ x*y*z | z <- [3..(quot total 2)], y <- [2..z], x <- [1..y],  (x + y + z == total), (x^2 + y^2 == z^2)]

main = do
    print (head (pythagoreanTriplet 1000))


