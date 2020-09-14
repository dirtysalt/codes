(* Dan Grossman, Coursera PL, HW2 Provided Code *)

exception AssertError of string

fun assert(value: bool, comment: string) =
    if not value
    then (print("!!!! " ^ comment ^ " FAILED\n"); false)
    else (print(comment ^ " ok\n"); true)


(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)

fun all_except_option (s: string, xs: string list) =
    case xs of
        [] => NONE
      | x :: xs2 => if same_string(x, s) then SOME xs2 else
                    let val y = all_except_option(s, xs2) in
                        case y of
                            NONE => NONE
                         |  SOME z => SOME (x :: z)
                    end

fun get_substitutions1 (xs : string list list, s: string) =
    case xs of
        [] => []
     |  ys :: xs2 =>
        let val y = all_except_option(s, ys) in
            case y of
                NONE => get_substitutions1(xs2, s)
              | SOME z =>  z @ get_substitutions1(xs2, s)
        end

fun get_substitutions2 (xs :string list list, s: string) =
    let fun foo (xs, s, res) =
            case xs of
                [] => res
              | ys :: xs2 =>
                let val y = all_except_option(s, ys) in
                    case y of
                        NONE => foo(xs2, s, res)
                      | SOME z =>  foo(xs2, s, z @ res)
                end
    in
        foo(xs, s, [])
    end


fun similar_names ( xs: string list list, {first=f:string, middle=m, last=l}) =
    let val subs = get_substitutions1(xs, f)
        fun foo (fs: string list) =
            case fs of
                [] => []
             |  x :: fs2 => {first=x, middle=m, last=l} :: foo(fs2)
    in
        foo(f::subs)
    end


val _ = assert(all_except_option ("string", ["string"]) = SOME [], "all_except_option")
val _ = assert(all_except_option ("string", ["hello", "world"]) = NONE, "all_except_option")

val test1 = get_substitutions1([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]],"Fred")

val _ = assert(get_substitutions1([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]],"Fred") = ["Fredrick","Freddie","F"], "get_substitutions1")
val _ = assert(get_substitutions1([["Fred","Fredrick"],["Jeff","Jeffrey"],["Geoff","Jeff","Jeffrey"]],"Jeff") = ["Jeffrey","Geoff","Jeffrey"], "get_substitutions1")
val _ = assert(get_substitutions2([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]],"Fred") = ["Freddie","F","Fredrick"], "get_substitutions2")
val _ = assert(get_substitutions2([["Fred","Fredrick"],["Jeff","Jeffrey"],["Geoff","Jeff","Jeffrey"]],"Jeff") = ["Geoff","Jeffrey","Jeffrey"], "get_substitutions2")

val _ = assert(similar_names([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]], {first="Fred", middle="W", last="Smith"}) =
               [{first="Fred", last="Smith", middle="W"},
                {first="Fredrick", last="Smith", middle="W"},
                {first="Freddie", last="Smith", middle="W"},
                {first="F", last="Smith", middle="W"}], "similar_names")

val test2 = similar_names([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]], {first="Fred", middle="W", last="Smith"})


(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw

exception IllegalMove

(* put your solutions for problem 2 here *)

fun card_to_string((suit, rank) : card) =
    let val ss = case suit of
                    Clubs => "Clubs"
                  | Diamonds => "Diamonds"
                  | Hearts =>  "Hearts"
                  | Spades => "Spades"
        val rs = case rank of
                     Ace => "Ace"
                   | Queen => "Queen"
                   | King => "King"
                   | Jack => "Jack"
                   | Num x => "Num " ^ Int.toString(x)
    in
        ss ^ " " ^ rs
    end

fun move_to_string(m : move) =
    case m of
        Discard c => "Discard " ^ card_to_string(c)
      | Draw =>  "Draw"


fun card_color ((suit, _): card) =
    case suit of
        Clubs => Black
     |  Spades => Black
     | Diamonds => Red
     | Hearts => Red

fun card_value ((_, rank): card) =
    case rank of
        Ace => 11
      | Jack => 10
      | Queen => 10
      | King => 10
      | Num x => x

fun remove_card(cs : card list, c : card, ex: exn) =
    case cs of
        [] => raise ex
      | c2 :: cs2 => if (c = c2) then cs2 else c2 :: remove_card(cs2, c, ex)

fun all_same_color(cs : card list) =
    case cs of
        [] => true
      | _ :: [] => true
      | x :: (y :: xs2) =>
        if (card_color(x) = card_color(y)) then all_same_color(y :: xs2)
        else false

fun sum_cards(cs: card list) =
    let fun foo (cs: card list, res: int) =
            case cs of
                [] => res
              | c :: cs2 => foo(cs2, card_value(c) + res)
    in
        foo(cs, 0)
    end

fun score(cs : card list, goal : int) =
    let val res = sum_cards(cs)
        val pscore = if (res > goal) then 3 * (res - goal) else (goal - res)
        val res2 = if all_same_color(cs) then pscore div 2 else pscore in
        res2
    end

fun officiate (cs : card list, ms : move list, goal : int) =
    let fun play(cs: card list, ms: move list, held: card list) =
            if (sum_cards(held) > goal) then score(held, goal) else
            case ms of
                [] => score(held, goal)
             | mv :: ms2 =>
               (
                 (* print ((move_to_string(mv) ^ "\n")); *)
                 case mv of
                     Discard c => play(cs, ms2, remove_card(held, c, IllegalMove))
                   | Draw =>
                     case cs of
                         [] => score(held, goal)
                      | c :: cs2 => play(cs2, ms2, c :: held)
            )
    in
        play(cs, ms, [])
    end


(* ============================================================ *)
fun sum_cards_v2(cs : card list) : int list =
    case cs of
        [] => [0]
      | c :: cs2 =>
        let val rest = sum_cards_v2(cs2) in
            case c of
                (_, Ace) => (List.map (fn (x) => (1 + x)) rest) @ (List.map (fn (x) => (x + 11)) rest)
              | _ => List.map (fn (x) => (x + card_value(c))) rest
        end

fun list_min (xs) =
    case xs of
        [] => 0
      | x :: xs2 => foldl (fn (x, acc) => Int.min(x, acc)) x xs2

fun min_sum_cards(cs : card list) = list_min(sum_cards_v2(cs))

fun score_challenge(cs : card list, goal : int) =
    let val vs = sum_cards_v2(cs)
        val same_color = all_same_color(cs)
        fun make_score(res) = if (res > goal) then 3 * (res - goal) else (goal - res)
        val scores = List.map make_score vs
        val min_score = list_min scores
        val res = if same_color then (min_score div 2) else min_score
    in
        res
    end


fun officiate_challenge (cs : card list, ms : move list, goal : int) =
    let fun play(cs: card list, ms: move list, held: card list) =
            if min_sum_cards(held) > goal then score_challenge(held, goal) else
            case ms of
                [] => score_challenge(held, goal)
             | mv :: ms2 =>
               (
                 (* print ((move_to_string(mv) ^ "\n")); *)
                 case mv of
                     Discard c => play(cs, ms2, remove_card(held, c, IllegalMove))
                   | Draw =>
                     case cs of
                         [] => score_challenge(held, goal)
                      | c :: cs2 => play(cs2, ms2, c :: held)
               )
    in
        play(cs, ms, [])
    end


fun print_cards(xs : card list) =
    let fun fx(xs : card list) =
        case xs of
            [] => true
          | x :: xs2 => (print("(" ^ card_to_string(x) ^ ") "); fx(xs2); true)
    in
        (print("["); fx(xs); print("]"))
    end

fun ok_to_discard_and_draw(held : card list, x : card, goal: int) =
    let fun test(xs: card list, tries: card list) =
            case tries of
                [] => NONE
              | t :: ts2  =>
                let val removed = remove_card(xs, t, IllegalMove)
                    val removed_score = score(removed, goal) in
                    (
                      print("try remove " ^ card_to_string(t) ^ ". score = " ^ Int.toString(removed_score) ^ "\n");
                      print("removed = ");
                      print_cards(removed);
                      print("\n");
                      if (removed_score = 0) then SOME t
                      else test(xs, ts2)
                    )
                end
    in
        test(x :: held, held)
    end


fun careful_player(cs : card list, goal : int) =
    let fun play(cs: card list, held : card list, ms: move list) =
            let val cur_value = sum_cards(held)
                val cur_score = score(held, goal) in

                if (cur_score = 0) then ms else
                case cs of
                    [] => ms
                 | c :: cs2 =>
                   if (goal - cur_value) > 10 then play(cs2, c :: held, ms @ [Draw]) else
                   (* try discard and draw strategy *)
                   let val discard_card = ok_to_discard_and_draw(held, c, goal) in
                       case discard_card of
                           NONE => if ((card_value(c) + cur_value) > goal) then ms else
                                   play(cs2, c :: held, ms @ [Draw])
                         | SOME v => ms @ [(Discard v),  Draw]
                   end
            end
    in
        play(cs, [], [])
    end
