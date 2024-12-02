import System.IO
import Data.List (sort)

part1 :: String -> Int
part1 inp = sum [abs ((read x :: Int) - (read y :: Int)) | (x, y) <- zip (sort left) (sort right)]
    where
        gen_lists [] = ([], [])
        gen_lists (xs:xss) = (head two_words:left, head (tail two_words):right)
            where
                (left, right) = gen_lists xss
                two_words = words xs
        
        (left, right) = gen_lists (lines inp)
        

main :: IO ()
main = do
    inp <- readFile "input.txt"
    print (part1 inp)