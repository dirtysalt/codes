use "hw2.sml";

val _ = assert(card_color((Clubs, Num 2)) = Black, "card_color")
val _ = assert(card_value((Clubs, Num 2)) = 2, "card_value")
val _ = assert(card_value((Clubs, Ace)) = 11, "card_value")
val _ = assert(remove_card([(Clubs, Ace)], (Clubs, Ace), IllegalMove) = [], "remove_card")
val _ = assert(remove_card([(Clubs, Ace), (Clubs, Ace)], (Clubs, Ace), IllegalMove) = [(Clubs, Ace)], "remove_card")
val _ = assert((remove_card([(Clubs, Ace), (Clubs, Ace)], (Hearts, Ace), IllegalMove); false) handle IllegalMove => true, "remove_card")
val _ = assert((remove_card([], (Hearts, Jack), IllegalMove); false) handle IllegalMove => true, "remove_card")

val _ = assert(all_same_color [(Clubs,Ace),(Spades,Ace),(Diamonds,Ace)] = false, "all_same_color")
val _ = assert(all_same_color [(Hearts, Ace), (Hearts, Ace)] = true, "all_same_color")
val _ = assert(all_same_color [(Hearts, Ace), (Clubs, Ace)] = false, "all_same_color")
val _ = assert(all_same_color [(Hearts, Ace)] = true, "all_same_color")
val _ = assert(all_same_color [] = true, "all_same_color")
val _ = assert(sum_cards ([(Hearts, Num 2),(Clubs, Num 4)]) = 6, "sum_cards")
val _ = assert(score ([(Hearts, Num 2),(Clubs, Num 4)],10) = 4, "score")
val _ = assert(score ([(Hearts, Num 2),(Clubs, Num 4)],1) = 15, "score")
val _ = assert(score ([(Hearts, Num 2),(Diamonds, Num 4)],1) = 7, "score")
val _ = assert(officiate ([(Hearts, Num 2),(Clubs, Num 4)],[Draw], 15) = 6, "officiate")
val _ = assert(officiate ([(Hearts, Num 2)],[Draw, Draw, Draw], 2) = 0, "officiate")

val _ = assert(officiate ([(Clubs,Ace),(Spades,Ace),(Clubs,Ace),(Spades,Ace)],
                        [Draw,Draw,Draw,Draw,Draw],
                        42)
             = 3, "officiate")

val _ = assert(((officiate([(Clubs,Jack),(Spades,Num(8))],
                         [Draw,Discard(Hearts,Jack)],
                         42);
               false)
              handle IllegalMove => true), "officate")

val _ = assert(sum_cards_v2 ([(Hearts, Num 2),(Diamonds, Ace)]) = [3, 13], "sum_cards_v2")
val _ = assert(sum_cards_v2 ([(Hearts, Num 2),(Diamonds, Ace), (Diamonds, Ace)]) = [4,14,14,24], "sum_cards_v2")
val _ = assert(list_min([1,2,3,4,10]) = 1, "list_min")

val _ = assert(score_challenge ([(Hearts, Num 2),(Diamonds, Ace)],3) = 0, "score_challenge")
val _ = assert(score_challenge ([(Hearts, Num 2),(Diamonds, Ace)],13) = 0, "score_challenge")
val _ = assert(score_challenge ([(Hearts, Num 2),(Diamonds, Ace)],12) = 1, "score_challenge")


val _ = assert(officiate_challenge ([(Clubs,Ace),(Spades,Ace),(Clubs,Ace),(Spades,Ace)],
                        [Draw,Draw,Draw,Draw,Draw],
                        4)
               = 0, "officiate_challenge")

val _ = assert(officiate_challenge ([(Clubs,Ace),(Spades,Ace),(Clubs,Ace),(Spades,Jack)],
                        [Draw,Draw,Draw,Draw,Draw],
                        14)
               = 0, "officiate_challenge")


val _ = assert(ok_to_discard_and_draw([(Hearts, Num 2)], (Hearts, Ace), 11) = SOME (Hearts, Num 2), "ok_to_discard_and_draw")
val _ = assert(ok_to_discard_and_draw([(Hearts, Num 2)], (Hearts, Ace), 10) = NONE, "ok_to_discard_and_draw")

val _ = OS.Process.exit(OS.Process.success)
