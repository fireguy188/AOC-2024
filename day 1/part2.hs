import System.IO

part2 :: String -> Int
part2 inp = sum [(read x :: Int) * count x right | x <- left]
    where
        count x [] = 0
        count x (y:ys) | x == y = 1 + count x ys
                       | otherwise = count x ys

        gen_lists [] = ([], [])
        gen_lists (xs:xss) = (head two_words:left, head (tail two_words):right)
            where
                (left, right) = gen_lists xss
                two_words = words xs
        
        (left, right) = gen_lists (lines inp)
        

main :: IO ()
main = do
    inp <- readFile "input.txt"
    print (part2 inp)