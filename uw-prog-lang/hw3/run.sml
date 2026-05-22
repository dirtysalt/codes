use "hw3.sml";

val _ = assert(only_capitals(["Hello", "world", "Yes"]) = ["Hello", "Yes"], "only_captials")
val _ = assert(longest_string1(["hello", "world"]) = "hello", "longest_string1")
val _ = assert(longest_string1(["hello", "world", "hellworld"]) = "hellworld", "longest_string1")
val _ = assert(longest_string2(["hello", "world"]) = "world", "longest_string2")

val _ = assert(longest_string3(["hello", "world"]) = "hello", "longest_string3")
val _ = assert(longest_string3(["hello", "world", "hellworld"]) = "hellworld", "longest_string3")
val _ = assert(longest_string4(["hello", "world"]) = "world", "longest_string4")

val _ = assert(longest_capitalized(["Hello", "World", "aaaaaaaa"]) = "Hello", "longest_captialized")
val _ = assert(rev_string("hello") = "olleh", "rev_string")

val _ = assert((first_answer (fn (x) => if (x = 3) then SOME 10 else NONE) [1,2,3,4]) = 10, "first_answer")
val _ = assert(((first_answer (fn (x) => if (x = 10) then SOME 10 else NONE) [1,2,3,4]) = 10; false) handle NoAnswer => true, "first_answer")
val _ = assert((all_answers (fn (x) => if (x = 3) then NONE else SOME [10, 20]) [1,2,3,4]) = NONE, "all_answers")
val _ = assert((all_answers (fn (x) => if (x = 10) then NONE else SOME [10, 20]) [1,2,3,4]) = SOME [10, 20, 10, 20, 10, 20, 10, 20], "all_answers")

val _ = assert(count_wildcards(TupleP [Wildcard, Wildcard]) = 2, "count_wildcards")
val _ = assert(count_wild_and_variable_lengths(TupleP [Wildcard, Variable "hello"]) = 6, "count_wild_and_variable_lengths")
val _ = assert(count_some_var("world", TupleP([Wildcard, Variable "hello", Variable "world"])) = 1, "count_some_var")
val _ = assert(check_pat(TupleP([Wildcard, Variable "hello", Variable "world"])) = true, "check_pat")
val _ = assert(check_pat(TupleP([Wildcard, Variable "hello", Variable "hello"])) = false, "check_pat")

val _ = assert(match(Tuple([Const(10), Const(20), Constructor("world", Const(30))]),
                     TupleP([ConstP 10, ConstP 20, Variable "hello"])) =
               SOME [("hello", Constructor("world", Const(30)))], "match")

val _ = assert(make_list(10, 5) = [10,10,10,10,10], "make_list")
val _ = assert(lookup_def([("hello", "world", 10), ("name", "c", 20)], "name") =
               SOME ("c", 20), "lookup_def")
val _ = assert(lookup_def([("hello", "world", 10), ("name2", "c", 20)], "name") =
               NONE, "lookup_def")

val _ = assert((exp_all_ok (fn (x) => (if (x = 3) then NONE else SOME (x))) [1,2,3,4]) = NONE,
               "exp_all_ok")
val _ = assert((exp_all_ok (fn (x) => (if (x = 3) then NONE else SOME(x + 1))) [1,2,4]) = SOME [2,3,5],
               "exp_all_ok")

val _ = assert(typecheck_patterns(
                    [],
                    [TupleP[Variable("x"),Variable("y")], TupleP[Wildcard,Wildcard]]) =
               SOME (TupleT([Anything, Anything])), "typecheck_patterns")

val _ = assert(typecheck_patterns(
                    [("foo", "bar", IntT)],
                    [TupleP[Variable("x"),Variable("y")],
                     TupleP[Wildcard,ConstructorP("foo", ConstP(10))]]) =
               SOME (TupleT([Anything, Datatype "bar"])), "typecheck_patterns")

val _ = assert(typecheck_patterns(
                    [],
                    [TupleP [UnitP,UnitP,UnitP]]) =
               SOME (TupleT [UnitT, UnitT, UnitT]), "typecheck_patterns")

val _ = assert(typecheck_patterns(
                    [],
                    [Wildcard, ConstP 17,ConstP 4]) =
               SOME (IntT), "typecheck_patterns")

val _ = OS.Process.exit(OS.Process.success)
