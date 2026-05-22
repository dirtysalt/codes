
#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;; put your code below


;(define (sequence-cont low high step res)
;  (if (> low high) res
;      (sequence-cont (+ low step) high step (cons low res))))
;
;(define (sequence low high step)
;  (let ((res '()))
;    (reverse (sequence-cont low high step res))))


(define (sequence low high step)
  (if (> low high) '()
      (cons low (sequence (+ low step) high step))))

(define (string-append-map xs suffix)
  (map (lambda (x) (string-append x suffix)) xs))

(define (list-nth-mod xs n)
  (cond ((< n 0) (error "list-nth-mod: negative number"))
        ((eq? xs '()) (error "list-nth-mod: empty list"))
        ('t (car (list-tail xs (remainder n (length xs)))))))

;(list-nth-mod '(1 2 3) -1)
;(list-nth-mod '(1 2 3) 4)
;(list-nth-mod '() 10)

(define (sfst s) (car (s)))
(define (srst s) (cdr (s)))

(define (stream-for-n-steps stream n)
  (if (= n 0) '()
      (cons (sfst stream) (stream-for-n-steps (srst stream) (- n 1)))))

(define (funny-number-stream-from idx)
  (let ((v (if (= (modulo idx 5) 0) (- idx) idx)))
    (lambda () (cons v (funny-number-stream-from (+ idx 1))))))

(define funny-number-stream (funny-number-stream-from 1))

(stream-for-n-steps funny-number-stream 10)

(define dan-then-dog (lambda () (cons "dan.jpg" (lambda () (cons "dog.jpg" dan-then-dog)))))

(stream-for-n-steps dan-then-dog 3)

(define (stream-add-zero s) (lambda () (cons (cons 0 (sfst s)) (stream-add-zero (srst s)))))

(stream-for-n-steps (stream-add-zero funny-number-stream) 10)

;; list-to-stream with helper function.
;; don't know how to define local function.

(define (list-to-stream-2 xs xs2)
  (if (null? xs) (list-to-stream-2 xs2 xs2)
      (lambda () (cons (car xs) (list-to-stream-2 (cdr xs) xs2)))))

(define (list-to-stream xs)
  (list-to-stream-2 xs xs))

(define (cycle-lists-2 xs ys)
  (lambda ()
  (cons (cons (sfst xs) (sfst ys))
        (cycle-lists-2 (srst xs) (srst ys)))))

(define (cycle-lists xs ys)
  (cycle-lists-2 (list-to-stream xs) (list-to-stream ys)))

(stream-for-n-steps (list-to-stream '(1 2 3)) 10)

(stream-for-n-steps (cycle-lists-2 (list-to-stream '(1 2 3)) (list-to-stream '("a" "b"))) 10)

(stream-for-n-steps (cycle-lists '(1 2 3) '("a" "b")) 10)

(define (vector-assoc-from-idx v vec idx)
  (if (= idx (vector-length vec)) #f
      (let ((x (vector-ref vec idx)))
        (if (and (pair? x) (equal? (car x) v)) x
            (vector-assoc-from-idx v vec (+ idx 1))))))
(define (vector-assoc v vec) (vector-assoc-from-idx v vec 0))

(vector-assoc 10 (vector "hello" "world" (cons 20 20) (cons 10 10)))


(define (cached-assoc xs n)
  (let ((cache (make-vector n #f))
        (slot 0))
    (lambda (v)
      (let ((cv (vector-assoc v cache)))
        (if cv
            (begin
              (printf "found in cache~n")
              cv)
            (let ((cv2 (assoc v xs)))
              (if cv2
                  (begin
                    (printf "not found in cache. set to slot ~a~n" slot)
                    (vector-set! cache slot cv2)
                    (set! slot (modulo (+ slot 1) n)))
                    ;(set! slot (+ slot 1)))
                  #f)
              cv2))))))

(define cached-assoc-fn (cached-assoc '((1 . 2) (2 . 3) (3 . 4) (4 . 5)) 2))
(cached-assoc-fn 2)
(cached-assoc-fn 2)
(cached-assoc-fn 1)
(cached-assoc-fn 3)
(cached-assoc-fn 4)

(require compatibility/defmacro)

;; can not find good loop structure.
(define-macro (while-less e1 do e2)
  (let ((t1 (gensym)))
    `(letrec ((,t1 ,e1))
       (define (iter) (if (>= ,e2 ,t1) #t (iter)))
       (iter))))

(require macro-debugger/expand)
(define a 2)
(while-less 7 do (begin (set! a (+ a 1)) (printf "x, a = ~a~n" a) a))
(while-less 7 do (begin (set! a (+ a 1)) (printf "x, a = ~a~n" a) a))
