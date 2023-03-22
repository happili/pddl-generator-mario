(define (problem problem_name)
    (:domain supermario_nes)
    (:objects


    )
    (:init


        (= (velocity-right) 0.0)
        (= (velocity-left) 0.0)
        ;(= (velocity-fall) 0.0)
        (= (velocity-height) 0.0)
        (= (y2) 2.0)
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
            (>= (x) 6.0)
            (< (y2) 2.1) 
            (= (velocity-right) 0.0)
            (= (velocity-left) 0.0)
            (= (velocity-height) 0.0)
        )
    )

)