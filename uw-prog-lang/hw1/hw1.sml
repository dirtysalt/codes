exception AssertError of string

fun assert(value: bool, comment: string) =
    if not value
    then raise AssertError(comment)
    else (print(comment ^ " ok\n"); true)

type mydate = int * int * int
fun get_month ((y, m, d): mydate) = m

fun is_older ((y0, m0, d0), (y1, m1, d1)) =
    if ((y0 < y1) orelse
        ((y0 = y1) andalso (m0 < m1)) orelse
        ((y0 = y1) andalso (m0 = m1) andalso (d0 < d1)))
    then true
    else false


fun number_in_month (xs: mydate list, month: int) =
    case xs of
        [] => 0
      | (y, m, d) :: xs2 => (if (m = month) then 1 else 0) +
                            number_in_month(xs2, month)


fun number_in_months (xs: mydate list, months: int list) =
    case months of
        [] => 0
      | m :: ms => number_in_month(xs, m) + number_in_months(xs, ms)


fun dates_in_month (xs: mydate list, month : int) =
    case xs of
        [] => []
      | x :: xs2  =>
        if (get_month(x) = month)
        then x :: dates_in_month(xs2, month)
        else dates_in_month(xs2, month)

fun dates_in_months (xs: mydate list, months : int list) =
    case months of
        [] => []
      | m :: ms => dates_in_month(xs, m) @ dates_in_months(xs, ms)

fun get_nth (xs : 'a list, n: int) =
    case n of
        1 => hd xs
      | _ => get_nth(tl xs, n - 1)

val months_in_string = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
fun month_to_string (m:int) =  get_nth(months_in_string, m)

fun date_to_string ((y, m, d): mydate) =
    month_to_string(m) ^ " " ^ Int.toString(d) ^ ", " ^ Int.toString(y)

fun number_before_reaching_sum (v : int, xs: int list)  =
    if (v <= 0) then ~1
    else 1 + number_before_reaching_sum(v - hd xs, tl xs)

val days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

fun what_month (day: int) = 1 + number_before_reaching_sum(day, days_in_month)


fun month_range (day1: int, day2: int) =
    if (day1 > day2) then []
    else what_month(day1) :: month_range(day1 + 1, day2)

fun oldest (xs : mydate list) =
    case xs of
        [] => NONE
      | x :: [] => SOME x
      | x :: (y :: xs2) =>
        if (is_older(x, y)) then oldest(x :: xs2)
        else oldest(y :: xs2)

fun in_list(x, xs) =
    case xs of
        [] => false
      | x2 :: xs2 => (x = x2) orelse in_list(x, xs2)

fun remove_dup(xs) =
    case xs of
        [] => []
      | x :: xs2 =>
        let val xs3 = remove_dup(xs2) in
            if in_list(x, xs3) then xs3
            else x :: xs3
        end

fun number_in_months_challenge (xs : mydate list, months: int list) =
    let val nodup_months = remove_dup(months) in
        number_in_months(xs, nodup_months)
    end

fun dates_in_months_challenge (xs : mydate list, months : int list) =
    let val nodup_months = remove_dup(months) in
        dates_in_months(xs, nodup_months)
    end

fun is_leap_year(y:int) =
    if ((y mod 400) = 0) then true
    else if ((y mod 4) = 0) andalso ((y mod 100) <> 0) then true
    else false

fun month_to_days (y:int, m:int) =
    if is_leap_year(y) andalso m = 2 then 29
    else get_nth(days_in_month, m)

fun reasonable_date ((y, m, d) : mydate) =
    if (y < 1) then false
    else if (m < 1) orelse (m > 12) then false
    else if (d < 1) orelse (d > month_to_days(y, m)) then false
    else true
