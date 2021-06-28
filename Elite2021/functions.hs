-- function_name arg1 arg2 arg3 ... argn =   --
--     expression or statements 	     --

-- not a declarative style, it is imperative as we are telling how to do rather than what to do --
--in_range min max x = --
--    x >= min && x <= max --

-- :: == has type --
--in_range :: Int -> Int -> Int -> Bool --
{-
  direct expression
  ------------------
  in_range min max x = x >= min && x <= max
     
  using where 
  -----------
  in_range min max x = ilb && iub 
      where ilb = x >= min
            iub = x <= max 
  
  using let in
  ------------
  in_range min max x =
    let ilb = x>=min
        iub = x<=max
    in 
    ilb && iub

  using if then else
   -}
  in_range min max x = 
      if ilb then iub else False
      where ilb = x >= min
            iub = x <= max

c :: Int
c = 1
b :: Float
b = 2.3

main = do
    print (in_range 0 5 3)
    print (c+b)
