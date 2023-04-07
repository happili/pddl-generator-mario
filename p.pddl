(define (problem problem_name)
    (:domain supermario_nes)
    (:objects
        a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15 - air
        b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 - blocks
    )
    (:init
       (= (block-x b1) 1.0)
       (= (block-y b1) 1.0)
       (= (block-x b2) 1.0)
       (= (block-y b2) 2.0)
       (= (block-x a1) 1.0)
       (= (block-y a1) 3.0)
       (= (block-x a2) 1.0)
       (= (block-y a2) 4.0)
       (= (block-x a3) 1.0)
       (= (block-y a3) 5.0)
       (= (block-x b3) 2.0)
       (= (block-y b3) 1.0)
       (= (block-x b4) 2.0)
       (= (block-y b4) 2.0)
       (= (block-x a4) 2.0)
       (= (block-y a4) 3.0)
       (= (block-x a5) 2.0)
       (= (block-y a5) 4.0)
       (= (block-x a6) 2.0)
       (= (block-y a6) 5.0)
       (= (block-x b5) 3.0)
       (= (block-y b5) 1.0)
       (= (block-x b6) 3.0)
       (= (block-y b6) 2.0)
       (= (block-x a7) 3.0)
       (= (block-y a7) 3.0)
       (= (block-x a8) 3.0)
       (= (block-y a8) 4.0)
       (= (block-x a9) 3.0)
       (= (block-y a9) 5.0)
       (= (block-x b7) 4.0)
       (= (block-y b7) 1.0)
       (= (block-x b8) 4.0)
       (= (block-y b8) 2.0)
       (= (block-x a10) 4.0)
       (= (block-y a10) 3.0)
       (= (block-x a11) 4.0)
       (= (block-y a11) 4.0)
       (= (block-x a12) 4.0)
       (= (block-y a12) 5.0)
       (= (block-x b9) 5.0)
       (= (block-y b9) 1.0)
       (= (block-x b10) 5.0)
       (= (block-y b10) 2.0)
       (= (block-x a13) 5.0)
       (= (block-y a13) 3.0)
       (= (block-x a14) 5.0)
       (= (block-y a14) 4.0)
       (= (block-x a15) 5.0)
       (= (block-y a15) 5.0)
        (= (velocity-right) 0.0)
        (= (velocity-left) 0.0)
        ;(= (velocity-fall) 0.0)
        (= (velocity-height) 0.0)
        (= (y2) 3.0)
        (= (x) 1.0)
      
        (= (d-jumped) 0.0)
        (not (pressing-right))
        (not (pressing-left))
        (not (pressing-a))
        (not (falling))
        (not (reached))
    )
    (:goal
        (and
            (> (x) 4)
            ;(< (y2) 2.1) 
            (= (velocity-right) 0.0)
            (= (velocity-left) 0.0)
            (= (velocity-height) 0.0)
        )
    )
)
