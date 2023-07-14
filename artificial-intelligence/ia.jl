# Salvador Donayre - Introd. CS.
# Artificial Intelligence - Formula of successions

# 1.570796326794897 -> 3.141592653589793 -> ... -> 9.42477796076938
pi(n) = (3.141592653589793 / 2) * n
# 5.14 -> 7.14 -> ... -> 33.14
catorce(n) = 5.14 + (n - 1) * 2
# 11 -> 19 -> ... -> 51
ocho(n) = 11 + (n - 1) * 8
# 1.3333333333333333 -> 2.6666666666666665 -> ... -> 8.0
tres(n) = n + (n/3)

function test(interval, func::Function)
    println("- $(func) -")
    for i in interval
        println("$func($i) = $(func(i))")
    end
    println("")
end

function test_all(p...)
    for pair in p
        interval, func = pair
        test(interval, func)
    end
end


println("")
test_all(
    (1:15, catorce),
    (1:6, ocho),
    (1:6, pi),
    (1:6, tres)
)