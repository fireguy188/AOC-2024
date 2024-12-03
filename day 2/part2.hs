import System.IO
import Data.Bool (Bool(True))

part2 :: String -> Int
part2 inp = sum [1 | line <- lines inp, is_safe line]
    where
        is_safe line = is_working ([(read x :: Int) | x <- words line]) (\x -> \y -> y - x) || is_working ([(read x :: Int) | x <- words line]) (\x -> \y -> x - y)

        is_working [] dif = True
        is_working [x] dif = True
        is_working [x, y] dif = True
        is_working (x:y:z:xs) dif
            | 1 <= dif x y && dif x y <= 3 = is_working' (x:y:z:xs) False dif -- first 2 items are fine, continue
            | 1 <= dif y z  && dif y z <= 3 = is_working' (y:z:xs) True dif -- removing first item
            | 1 <= dif x z && dif x z <= 3 = is_working' (x:z:xs) True dif -- removing second item
            | otherwise = False -- can't remove either item

        
        is_working' (x:y:[]) r dif
            | 1 <= dif x y && dif x y <= 3 = True
            | r = False
            | otherwise = True
        is_working' (w:x:y:[]) r dif
            | 1 <= dif x y && dif x y <= 3 = True
            | r = False
            | otherwise = True
        is_working' (w:x:y:z:xs) r dif -- we say y = whats at index i in python
            | 1 <= dif x y && dif x y <= 3 = is_working' (x:y:z:xs) r dif -- x and y are fine, continue
            | r = False -- we have to remove either x or y, but we have already removed something
            | (1 <= dif w y && dif w y <= 3) && (1 <= dif y z && dif y z <= 3) = is_working' (y:z:xs) True dif -- remove x
            | (1 <= dif x z && dif x z <= 3) = is_working' (x:z:xs) True dif -- remove y
            | otherwise = False -- can't remove either item


main :: IO ()
main = do
    inp <- readFile "input.txt"
    print (part2 inp)