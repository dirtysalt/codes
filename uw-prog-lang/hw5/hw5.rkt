;; Programming Languages, Homework 5

#lang racket
(provide (all-defined-out)) ;; so we can put tests in a second file

;; definition of structures for MUPL programs - Do NOT change
(struct var  (string) #:transparent)  ;; a variable, e.g., (var "foo")
(struct int  (num)    #:transparent)  ;; a constant number, e.g., (int 17)
(struct add  (e1 e2)  #:transparent)  ;; add two expressions
(struct ifgreater (e1 e2 e3 e4)    #:transparent) ;; if e1 > e2 then e3 else e4
(struct fun  (nameopt formal body) #:transparent) ;; a recursive(?) 1-argument function
(struct call (funexp actual)       #:transparent) ;; function call
(struct mlet (var e body) #:transparent) ;; a local binding (let var = e in body)
(struct apair (e1 e2)     #:transparent) ;; make a new pair
(struct fst  (e)    #:transparent) ;; get first part of a pair
(struct snd  (e)    #:transparent) ;; get second part of a pair
(struct aunit ()    #:transparent) ;; unit value -- good for ending a list
(struct isaunit (e) #:transparent) ;; evaluate to 1 if e is unit else 0

;; a closure is not in "source" programs but /is/ a MUPL value; it is what functions evaluate to
(struct closure (env fun) #:transparent)

;; Problem 1R

;; CHANGE (put your solutions here)
(define (racketlist->mupllist xs)
  (cond [(null? xs) (aunit)]
        [#t (apair (car xs) (racketlist->mupllist (cdr xs)))]))

(define (mupllist->racketlist xs)
  (cond [(aunit? xs) null]
        [#t (cons (apair-e1 xs) (mupllist->racketlist (apair-e2 xs)))]))

;; (racketlist->mupllist '(1 2 3))
;; (mupllist->racketlist (racketlist->mupllist '(1 2 3)))

;; Problem 2

;; lookup a variable in an environment
;; Do NOT change this function
(define (envlookup env str)
  (cond [(null? env) (error "unbound variable during evaluation" str)]
        [(equal? (car (car env)) str) (cdr (car env))]
        [#t (envlookup (cdr env) str)]))

(define (extend-env name value env)
  (cons (cons name value) env))

;; Do NOT change the two cases given to you.
;; DO add more cases for other kinds of MUPL expressions.
;; We will test eval-under-env by calling it directly even though
;; "in real life" it would be a helper function of eval-exp.
(define (eval-under-env e env)
  ;; (display "env = ") (print env) (display ", e = ")(print e) (newline)
  (cond [(var? e)
         (envlookup env (var-string e))]
        [(add? e)
         (let ([v1 (eval-under-env (add-e1 e) env)]
               [v2 (eval-under-env (add-e2 e) env)])
           (if (and (int? v1)
                    (int? v2))
               (int (+ (int-num v1)
                       (int-num v2)))
               (error "MUPL addition applied to non-number")))]
        ;; CHANGE add more cases here
        [(int? e) e]

        [(fun? e) (closure env e)] ;; 这里仅仅创建closure对象

        [(ifgreater? e)
         (let ([v1 (eval-under-env (ifgreater-e1 e) env)]
               [v2 (eval-under-env (ifgreater-e2 e) env)])
           (if (and (int? v1) (int? v2))
               (if (> (int-num v1) (int-num v2))
                   (eval-under-env (ifgreater-e3 e) env)
                   (eval-under-env (ifgreater-e4 e) env))
               (error "MUPL if-greater applied to non-number")))]

        [(call? e)
         (let ([clj (eval-under-env (call-funexp e) env)])
           (if (closure? clj)
               (let* ([fn (closure-fun clj)]
                      [clj-env (closure-env clj)]
                      ;; 如果是有名称函数的话，在原有的env基础上增加name->clj的绑定
                      [ext-env (if (fun-nameopt fn) (extend-env (fun-nameopt fn) clj env) env)]
                      [ext-clj-env (if (fun-nameopt fn) (extend-env (fun-nameopt fn) clj clj-env) clj-env)]
                      [new-env (extend-env (fun-formal fn)
                                           ;; 在当前环境下面对实参求值，这个求值也可以使用当前函数
                                           (eval-under-env (call-actual e) ext-env)
                                           ;; 绑定到closure的环境上，对body内部求值
                                           ext-clj-env)])
                 ;                 (display "call ....") (newline)
                 ;                 (display "new-env = ") (print new-env) (newline)
                 ;                 (display "fun-formal = ") (print (fun-formal fn)) (newline)
                 ;                 (display "call-actual = ") (print (call-actual e)) (newline)
                 ;                 (display "fun-body = ") (print (fun-body fn)) (newline)
                 (eval-under-env (fun-body fn) new-env))
               (error "MULP call applied to non-closure")))]

        [(mlet? e)
         (eval-under-env (mlet-body e)
                         (extend-env (mlet-var e)
                                     (eval-under-env (mlet-e e) env)
                                     env))]

        [(apair? e)
         (apair (eval-under-env (apair-e1 e) env)
                (eval-under-env (apair-e2 e) env))]

        [(fst? e)
         (let ([v (eval-under-env (fst-e e) env)])
           (if (apair? v) (apair-e1 v)
               (error "MUPL fst on non-pair")))]

        [(snd? e)
         (let ([v (eval-under-env (snd-e e) env)])
           (if (apair? v) (apair-e2 v)
               (error "MUPL snd on non-pair")))]

        [(aunit? e) e]
        [(isaunit? e)
         (let ([v (eval-under-env (isaunit-e e) env)])
           (if (aunit? v) (int 1) (int 0)))]

        [(closure? e) e]
        [#t (error (format "bad MUPL expression: ~v" e))]))

;; Do NOT change
(define (eval-exp e)
  (eval-under-env e null))

;; Problem 3

(define (ifaunit e1 e2 e3)
  (ifgreater (isaunit e1) (int 0) e2 e3))

(define (mlet* lstlst e2)
  (if (null? lstlst) e2
      (mlet (caar lstlst) (cdar lstlst) (mlet* (cdr lstlst) e2))))


(define (ifeq e1 e2 e3 e4)
  (mlet "_x" e1
        (mlet "_y" e2
              (ifgreater (var "_x") (var "_y") e4
                         (ifgreater (var "_y") (var "_x") e4 e3)))))

;; Problem 4

;; 如果使用let是不行的，let只是简单的值绑定
;; 和我们这里设计的mlet很像
;; 但是我们这里(fun)返回一个closure对象，可以将变量和closure对象绑定
(define (my-map-let f)
  (letrec ([foo (lambda (xs)
                  (if (null? xs) null
                      (cons (f (car xs)) (foo (cdr xs)))))])
    foo))

(define (my-map f)
  (define (foo xs)
    (if (null? xs) null
        (cons (f (car xs)) (foo (cdr xs)))))
  foo)

;; ((my-map-let (lambda (x) (+ x 1))) '(1 2 3))

(define mupl-map
  (let ([xs (var "xs")]
        [fn (var "fn")]
        [loop (var "loop")])
    (fun #f "fn"
         (fun "loop" "xs"
              (ifaunit xs (aunit)
                       (apair (call fn (fst xs)) (call loop (snd xs))))))))

(define mupl-map-mlet
  (let ([xs (var "xs")]
        [fn (var "fn")]
        [loop (var "loop")])
    (fun #f "fn"
         (mlet "anything"
               (fun "loop" "xs"
                    (ifaunit xs (aunit)
                             (apair (call fn (fst xs)) (call loop (snd xs)))))
               (var "anything")))))


(define mupl-mapAddN
  (mlet "map" mupl-map
        (fun #f "i"
             (call (var "map") (fun #f "x" (add (var "x") (var "i")))))))

;; (eval-exp (call mupl-map (fun #f "x" (add (var "x") (int 7)))))
;; (print "====================")(newline)
;; (eval-exp (call mupl-map-mlet (fun #f "x" (add (var "x") (int 7)))))

;; (eval-exp (call (call mupl-map-mlet (fun #f "x" (add (var "x") (int 7)))) (apair (int 1) (aunit))))

;; Challenge Problem

(struct fun-challenge (nameopt formal body freevars) #:transparent) ;; a recursive(?) 1-argument function

;; We will test this function directly, so it must do
;; as described in the assignment
;; 检查每个表达式中使用了那些变量，并且返回
;; 在fun这个表达式中，排除掉形参，就是使用fun的freevars.
(define (compute-free-vars e)
  (define (C e)
    (cond [(var? e) (cons e (set-add (set) (var-string e)))]

          [(add? e)
           (let ([v1 (C (add-e1 e))]
                 [v2 (C (add-e2 e))])
             (cons (add (car v1) (car v2)) (set-union (cdr v1) (cdr v2))))]

          [(ifgreater? e)
           (let ([v1  (C (ifgreater-e1 e))]
                 [v2 (C (ifgreater-e2 e))]
                 [v3 (C (ifgreater-e3 e))]
                 [v4 (C (ifgreater-e4 e))])
             (cons (ifgreater (car v1) (car v2) (car v3) (car v4))
                   (set-union (cdr v1) (cdr v2) (cdr v3) (cdr v4))))]

          [(fun? e)
           (let* ([name (fun-nameopt e)]
                  [formal (fun-formal e)]
                  [v2 (C (fun-body e))]
                  ;; body里面可以使用name和formal. 所以排除
                  [vars (set-remove (set-remove (cdr v2) formal) name)])
             (cons (fun-challenge name formal (car v2) vars) vars))]

          [(call? e)
           (let ([v1 (C (call-funexp e))]
                 [v2 (C (call-actual e))])
             (cons (call (car v1) (car v2)) (set-union (cdr v1) (cdr v2))))]

          [(mlet? e)
           (let* ([v1 (C (mlet-e e))]
                  [v2 (C (mlet-body e))]
                  ;; e里面不能使用mlet-var，所以不排除
                  ;; 但是body里面可以使用mlet-var，所以排除
                  [vars (set-union (cdr v1) (set-remove (cdr v2) (mlet-var e)))])
             (cons (mlet (mlet-var e) (car v1) (car v2)) vars))]


          [(apair? e)
           (let ([v1 (C (apair-e1 e))]
                 [v2 (C (apair-e2 e))])
             (cons (apair (car v1) (car v2)) (set-union (cdr v1) (cdr v2))))]

          [(fst? e)
           (let ([v1 (C (fst-e e))])
             (cons (fst (car v1)) (cdr v1)))]

          [(snd? e)
           (let ([v1 (C (snd-e e))])
             (cons (snd (car v1)) (cdr v1)))]

          [(isaunit? e)
           (let ([v1 (C (isaunit-e e))])
             (cons (isaunit (car v1)) (cdr v1)))]

          [(closure? e)
           (let ([v (C (closure-fun e))])
             (cons (closure (closure-env e) (car v)) (cdr v)))]
          
          [#t (cons e (set))]))
  (let ([v (C e)])
    ;; (display "vars = ") (print (cdr v)) (newline)
    (car v)))

;; (compute-free-vars (call mupl-map (fun #f "x" (add (var "x") (int 7)))))
;; (compute-free-vars (mlet "x" (int 1) (add (int 5) (var "x"))))

;; Do NOT share code with eval-under-env because that will make
;; auto-grading and peer assessment more difficult, so
;; copy most of your interpreter here and make minor changes
(define (create-env-by-vars env vars)
  (if (set-empty? vars) null
      (let ([var (set-first vars)])
        (extend-env var (envlookup env var)
                    (create-env-by-vars env (set-rest vars))))))


(define (eval-under-env-c e env)
  ;; (display "env = ") (print env) (display ", e = ")(print e) (newline)
  (cond [(var? e)
         (envlookup env (var-string e))]
        [(add? e)
         (let ([v1 (eval-under-env-c (add-e1 e) env)]
               [v2 (eval-under-env-c (add-e2 e) env)])
           (if (and (int? v1)
                    (int? v2))
               (int (+ (int-num v1)
                       (int-num v2)))
               (error "MUPL addition applied to non-number")))]
        ;; CHANGE add more cases here
        [(int? e) e]

        [(fun-challenge? e)
         (let ([new-env (create-env-by-vars env (fun-challenge-freevars e))])
           (closure new-env e))] ;; 这里仅仅创建closure对象

        [(ifgreater? e)
         (let ([v1 (eval-under-env-c (ifgreater-e1 e) env)]
               [v2 (eval-under-env-c (ifgreater-e2 e) env)])
           (if (and (int? v1) (int? v2))
               (if (> (int-num v1) (int-num v2))
                   (eval-under-env-c (ifgreater-e3 e) env)
                   (eval-under-env-c (ifgreater-e4 e) env))
               (error "MUPL if-greater applied to non-number")))]

        [(call? e)
         (let ([clj (eval-under-env-c (call-funexp e) env)])
           (if (closure? clj)
               (let* ([fn (closure-fun clj)]
                      [clj-env (closure-env clj)]
                      ;; 如果是有名称函数的话,在原有的env基础上增加name->clj的绑定
                      [ext-env (if (fun-challenge-nameopt fn) (extend-env (fun-challenge-nameopt fn) clj env) env)]
                      [ext-clj-env (if (fun-challenge-nameopt fn) (extend-env (fun-challenge-nameopt fn) clj clj-env) clj-env)]
                      [new-env (extend-env (fun-challenge-formal fn)
                                           ;; 在当前环境下面对实参求值,这个求值也可以使用当前函数
                                           (eval-under-env-c (call-actual e) ext-env)
                                           ;; 绑定到closure的环境上,对body内部求值
                                           ext-clj-env)])
                 ;                 (display "call ....") (newline)
                 ;                 (display "new-env = ") (print new-env) (newline)
                 ;                 (display "fun-formal = ") (print (fun-formal fn)) (newline)
                 ;                 (display "call-actual = ") (print (call-actual e)) (newline)
                 ;                 (display "fun-body = ") (print (fun-body fn)) (newline)
                 (eval-under-env-c (fun-challenge-body fn) new-env))
               (error "MULP call applied to non-closure")))]

        [(mlet? e)
         (eval-under-env-c (mlet-body e)
                           (extend-env (mlet-var e)
                                       (eval-under-env-c (mlet-e e) env)
                                       env))]

        [(apair? e)
         (apair (eval-under-env-c (apair-e1 e) env)
                (eval-under-env-c (apair-e2 e) env))]

        [(fst? e)
         (let ([v (eval-under-env-c (fst-e e) env)])
           (if (apair? v) (apair-e1 v)
               (error "MUPL fst on non-pair")))]

        [(snd? e)
         (let ([v (eval-under-env-c (snd-e e) env)])
           (if (apair? v) (apair-e2 v)
               (error "MUPL snd on non-pair")))]

        [(aunit? e) e]
        [(isaunit? e)
         (let ([v (eval-under-env-c (isaunit-e e) env)])
           (if (aunit? v) (int 1) (int 0)))]

        [(closure? e) e]
        [#t (error (format "bad MUPL expression: ~v" e))]))

;; Do NOT change this
(define (eval-exp-c e)
  (eval-under-env-c (compute-free-vars e) null))

;; (eval-exp-c (call (call mupl-map (fun #f "x" (add (var "x") (int 7)))) (apair (int 1) (aunit))))
