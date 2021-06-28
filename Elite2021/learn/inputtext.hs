main = do
    putStrLn "What's your name? "
    name <- getLine
    putStrLn ("hello " ++ name)
