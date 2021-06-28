revNum :: Int -> Int
--revNum n = read $ reverse $ show n--
--revNum = read <$> reverse <$> show--
revNum = read . reverse . show -- . = function application read(reverse(show)))--
{-freq' ch = length . filter (==ch) 
. operator called as composition function-}

{-euler 10 , kaprekar-}
