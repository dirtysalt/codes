(* Coursera Programming Languages, Homework 3, Provided Code *)

exception AssertError of string

fun assert(value: bool, comment: string) =
    if not value
    then raise AssertError(comment)
    else (print("[OK] " ^ comment ^ "\n"); true)

exception NoAnswer

datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
    let
	val r = g f1 f2
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x
	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
	  | ConstructorP(_,p) => r p
	  | _                 => 0
    end

(**** for the challenge problem only ****)

datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string

(**** you can put all your code here ****)

val only_capitals = List.filter (fn x => Char.isUpper(String.sub(x, 0)))

val longest_string1 = foldl (fn (x, acc) => if (String.size(x) > String.size(acc)) then x else acc) ""

val longest_string2 = foldl (fn (x, acc) => if (String.size(x) >= String.size(acc)) then x else acc) ""

fun longest_string_helper (f : int * int -> bool)  =
    foldl (fn (x, acc) => if (f(String.size(x), String.size(acc))) then x else acc) ""

val longest_string3 = longest_string_helper (fn (x, y) => x > y)
val longest_string4 = longest_string_helper (fn (x, y) => x >= y)

val longest_capitalized = longest_string1 o only_capitals

val rev_string = String.implode o List.rev o String.explode


fun first_answer (f : 'a -> 'b option) (xs : 'a list) : 'b =
    if (null xs) then raise NoAnswer else
    case f(hd xs) of
        NONE => first_answer f (tl xs)
     |  SOME v => v

fun all_answers (f : 'a -> 'b list option) (xs : 'a list) : 'b list option =
    if (null xs) then SOME [] else
    case f(hd xs) of
        NONE => NONE
      | SOME vs =>
        case all_answers f (tl xs) of
            NONE => NONE
         | SOME rest =>  SOME (vs @ rest)

(* fun g f1 f2 p = *)
(*     let *)
(* 	val r = g f1 f2 *)
(*     in *)
(* 	case p of *)
(* 	    Wildcard          => f1 () *)
(* 	  | Variable x        => f2 x *)
(* 	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps *)
(* 	  | ConstructorP(_,p) => r p *)
(* 	  | _                 => 0 *)
(*     end *)

fun count_wildcards p =
    let val count = ref 0
    in
        (g (fn (x) => (count := !count + 1; 0)) (fn (x) => 0) p;
         !count)
    end


fun count_wild_and_variable_lengths p =
    let val count = ref 0
    in
        (g (fn (x) => (count := !count + 1; 0))
           (fn (x) => (count := !count + String.size(x); 0)) p;
         !count)
    end

fun count_some_var (s, p) =
    let val count = ref 0
    in
        (g (fn (x) => 0) (fn (x) => if (x = s) then(count := !count + 1; 0) else 0) p;
         !count)
    end

fun check_pat p =
    let fun collect(p) =
            case p of
                Variable x => [x]
              | TupleP ps => List.foldl (fn (p, acc) => collect(p) @ acc) [] ps
              | ConstructorP(_, p) => collect(p)
              | _ => []
        fun check_rep (names) =
            case names of
                [] => false
              | x :: xs => if (List.exists (fn (y) => (x = y)) xs) then true else check_rep(xs)
    in
        not(check_rep(collect(p)))
    end

fun match (v : valu, p : pattern) : (string * valu) list option =
    let fun foo (v: valu, p: pattern) =
            case (p, v) of
                (Wildcard, _) => SOME []
              | (Variable name, _) => SOME [(name, v)]
              | (UnitP, Unit) => SOME []
              | (ConstP x, Const y) => if (x = y) then SOME [] else NONE
              | (TupleP ps, Tuple vs) =>
                if (length(ps) = length(vs)) then all_answers foo (ListPair.zip (vs,ps)) else NONE
              | (ConstructorP (x, p1), Constructor (y, v1)) => if (x = y) then foo(v1, p1) else NONE
              | _ => NONE
    in
        foo(v, p)
    end

fun first_match (v: valu) (ps : pattern list) : (string * valu) list option =
    SOME (first_answer (fn (x) => match(v, x)) ps)
    handle NoAnswer => NONE


fun exp_all_ok (f : 'a -> 'b option) (xs : 'a  list) : 'b list option =
    let fun foo (xs) =
            case xs of
                [] => SOME []
              | x :: xs2 =>
                case f(x) of
                    NONE => NONE
                  | SOME v =>
                    case foo(xs2) of
                        NONE => NONE
                     | SOME vs2 => SOME (v :: vs2)
    in
        foo(xs)
    end

fun make_list(v, n) = if n = 0 then [] else v :: make_list(v, n - 1)

fun lookup_def (defs, name) =
    case defs of
        [] => NONE
      | (x, dt_name, typ)::rest =>
        if (x = name) then SOME (dt_name, typ) else lookup_def(rest, name)

fun typecheck_patterns (defs : (string * string * typ) list,
                        ps : pattern list) : typ option =
    let fun mm(t : typ, p : pattern) : typ option =
            case (p, t) of
                (Wildcard, _) => SOME t
             |  (Variable _, _) =>
                if (t = UnitT) then NONE else SOME t

             | (UnitP, UnitT) => SOME t
             | (UnitP, Anything) => SOME UnitT
             | (ConstP _, IntT) => SOME t
             | (ConstP _, Anything) =>SOME IntT

             (* for tuple to match tuple of types
                1. length matches
                2. all elements match

                for tuple to match Anything
                1. match [Anything .. Anything] of same length
              *)

             | (TupleP ps, TupleT types) =>
               (if (length(ps) <> length(types)) then NONE else
                   case exp_all_ok mm (ListPair.zip (types, ps)) of
                       NONE => NONE
                     | SOME ts => SOME (TupleT ts))
             | (TupleP ps, Anything) =>
               (case exp_all_ok mm (ListPair.zip (make_list(Anything, length(ps)), ps)) of
                   NONE => NONE
                 | SOME ts => SOME (TupleT ts))

             (* for constructor to match Anything
                1. lookup cs in defs, (cs, dt_name, ty)
                2. try match (ty, cp) if failed return NONE
                3. return Datatype of dt_name

                for constructor to match datatype of dt_name
                1. lookup cs in defs, (cs, dt_name2, ty)
                2. if dt_name2 != dt_name return NONE
                3. return datatype of dt_name.
              *)
             | (ConstructorP (cs, cp), Anything) =>
               (case lookup_def(defs, cs) of
                   NONE => NONE
                 | SOME (dt_name, ty) =>
                   if (mm (ty, cp) = NONE) then NONE else SOME (Datatype dt_name))
             | (ConstructorP (cs, cp), Datatype dt_name2) =>
               (case lookup_def(defs, cs) of
                    NONE => NONE
                  | SOME (dt_name, _)  =>
                    if (dt_name = dt_name2) then SOME (Datatype dt_name) else NONE)
             | _ => NONE

        fun iter (t: typ, ps: pattern list) : typ option =
            case ps of
                [] => SOME (t)
              | p :: ps2 =>
                case mm(t, p) of
                    NONE => NONE
                  | SOME t2 => iter(t2, ps2)
    in
        iter(Anything, ps)
    end
