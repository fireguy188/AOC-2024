import System.IO

part1 :: String -> Int
part1 inp = sum [1 | line <- lines inp, is_safe line]
    where
        is_safe line = is_increasing ([(read x :: Int) | x <- words line]) || is_decreasing ([(read x :: Int) | x <- words line])

        is_increasing [] = True
        is_increasing [x] = True
        is_increasing (x:y:xs) = 1 <= (y-x) && (y-x) <= 3 && is_increasing (y:xs)

        is_decreasing [] = True
        is_decreasing [x] = True
        is_decreasing (x:y:xs) = 1 <= (x-y) && (x-y) <= 3 && is_decreasing (y:xs)

main :: IO ()
main = do
    inp <- readFile "input.txt"
    print (part1 inp)