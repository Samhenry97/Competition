y = gets.strip.to_i

if y <= 1917 then
    if y % 4 == 0
        puts "12.09.#{y}"
    else
        puts "13.09.#{y}"
    end
elsif y == 1918 then
    puts "26.09.#{y}"
else
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
        puts "12.09.#{y}"
    else
        puts "13.09.#{y}"
    end
end
