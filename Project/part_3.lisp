;;;; Część I
;;;; Generowanie tablicy 100 losowych liczb, inkrementacja nieparzystych,
;;;; a następnie sortowanie przez zamianę malejąco.

;; Funkcja tworząca tablicę 100 losowych liczb z zakresu 1 do 100
(defun create-random-array ()
  (make-array '(100)
              :initial-contents (loop for i below 100 collect (1+ (random 100)))))

;; Funkcja podnosząca o jeden nieparzyste elementy tablicy
(defun increment-odd-array-elements (array)
  (map-into array (lambda (element)
                      (if (oddp element) (1+ element) element))
            array)
  array)

;; Funkcja sortowania przez zamianę (selekcyjne) malejąco
(defun selection-sort-descending (array)
  (let ((n (array-dimension array 0)))
    (loop for i from 0 below (1- n) do
          (let ((max-index i))
            (loop for j from (1+ i) below n do
                  (when (> (aref array j) (aref array max-index))
                    (setf max-index j)))
            (when (/= max-index i)
              (rotatef (aref array i) (aref array max-index)))))
    array))

;; Główna część programu dla Części I
(let ((number-array (create-random-array)))
  (format t "Tablica przed modyfikacją: ~a~%" (coerce number-array 'list))
  (let ((modified-array (increment-odd-array-elements (copy-seq number-array))))
    (format t "Tablica po inkrementacji nieparzystych: ~a~%" (coerce modified-array 'list))
    (let ((sorted-array (selection-sort-descending (copy-seq modified-array))))
      (format t "Tablica posortowana malejąco (selection sort): ~a~%" (coerce sorted-array 'list)))))

;;;; Część II
;;;; Implementacja sortowania przez wstawianie (insertion sort) malejąco
;;;; z użyciem rekurencji i zaawansowanych funkcji.

;; Algorytm: Sortowanie przez wstawianie (Insertion Sort)

;; Działanie (wersja rekurencyjna):
;; 1. Jeśli lista jest pusta, jest posortowana.
;; 2. Wyjmij pierwszy element z listy.
;; 3. Rekurencyjnie posortuj resztę listy (od największego do najmniejszego).
;; 4. Wstaw pierwszy element w odpowiednie miejsce w posortowanej reszcie,
;;    tak aby zachować porządek malejący.

(defun insert-element-descending (element sorted-list)
  (cond ((null sorted-list) (list element))
        ((>= element (first sorted-list)) (cons element sorted-list))
        (t (cons (first sorted-list)
                 (insert-element-descending element (rest sorted-list))))))

(defun insertion-sort-recursive-descending (list)
  (if (null list)
      nil
      (insert-element-descending (first list)
                                 (insertion-sort-recursive-descending (rest list)))))

;; Główna część programu dla Części II
(let ((number-list (coerce (create-random-array) 'list)))
  (let ((modified-list (increment-odd-array-elements (copy-seq (coerce number-list 'array)))))
    (format t "~%Lista przed sortowaniem przez wstawianie (po inkrementacji nieparzystych): ~a~%" (coerce modified-list 'list))
    (let ((sorted-list (insertion-sort-recursive-descending (copy-seq (coerce modified-list 'list)))))
      (format t "Lista posortowana malejąco (insertion sort recursive): ~a~%" sorted-list))))