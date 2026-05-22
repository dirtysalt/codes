use "hw1.sml";

val _ = assert((is_older ((1,2,3),(2,3,4)) = true), "test_is_older")
val _ = assert((is_older ((1,2,3),(1,2,3)) = false), "test_is_older")

val _ = assert((number_in_month([], 2) = 0), "test_number_in_month")
val _ = assert((number_in_month([(20, 2, 1), (20, 2, 2), (20, 3, 2)], 2) = 2), "test_number_in_month")
val _ = assert((number_in_months([(20, 2, 1), (20, 2, 2), (20, 3, 2)], [2,3]) = 3), "test_number_in_months")

val _ = assert((dates_in_month([(20, 2, 1), (20, 2, 2), (20, 3, 2)], 2) = [(20, 2, 1), (20, 2, 2)]), "test_dates_in_month")
val _ = assert((dates_in_months([(20, 2, 1), (20, 2, 2), (20, 3, 2)], [2,3]) = [(20, 2, 1), (20, 2, 2), (20, 3, 2)]), "test_dates_in_months")

val _ = assert((get_nth(["hello", "world"], 2) = "world"), "test_get_nth")
val _ = assert((get_nth(["hello", "world"], 1) = "hello"), "test_get_nth")

val _ = assert(((date_to_string (2019, 1, 20)) = "January 20, 2019"), "test_date_to_string")

val _ = assert((number_before_reaching_sum(10, [1, 2, 3, 4, 5]) = 3), "test_number_before_reaching_sum")

val _ = assert(what_month(30) = 1, "test_what_month")
val _ = assert(what_month(31) = 1, "test_what_month")
val _ = assert(what_month(32) = 2, "test_what_month")
val _ = assert(what_month(70) = 3, "test_what_month")

val _ = assert(month_range(31, 34) = [1,2,2,2], "test_month_range")

val _ = assert(oldest([(2012,2,28),(2011,3,31),(2011,4,28)]) = SOME (2011,3,31), "test_oldest")
val _ = assert(oldest([]) = NONE, "test_oldest")

val _  = assert(in_list(1, [1,2,3]), "test_in_list")
val _  = assert(in_list(4, [1,2,3]) = false, "test_in_list")
val _  = assert(remove_dup([1,2,3,4,1,2,3]) = [4,1,2,3], "test_remove_dup")

val _ = assert(reasonable_date((2000, 1, 1)), "test_reasonable_date")
val _ = assert(reasonable_date((2000, 2, 29)), "test_reasonable_date")
val _ = assert(reasonable_date((2001, 2, 29)) = false, "test_reasonable_date")
val _ = assert(reasonable_date((0, 2, 29)) = false, "test_reasonable_date")
val _ = assert(reasonable_date((2000, 13, 30)) = false, "test_reasonable_date")
val _ = assert(reasonable_date((2000, 5, 31)) = true, "test_reasonable_date")

val _ = OS.Process.exit(OS.Process.success)
