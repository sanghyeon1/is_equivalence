# is_equivalence
이산 수학에서 동치 관계를 판별하는 프로그램입니다. 
반사적, 대칭적, 추이적(전이적) 관계인지를 boolean으로 반환합니다. 
단, 반대칭적인 관계는 판별하지 않습니다.
최종적으로 동치 관계인지 아닌지를 판별합니다.


- 변수 R
--> R은 numpy 행렬로써, n x n 형태의 정방행렬이 들어갑니다.
--> 사용자 직접입력이 아닌, 코드 상 미리 선언함으로써 할당됩니다.


함수(R)
- is_reflexive(R)
--> 행렬R이 반사적 관계인지 판별하여 boolean값을 반환합니다. 

- is_symmetric(R)
--> 행렬R이 대칭적 관계인지 판별하여 boolean값을 반환합니다.

- is_transitive(R)
--> 행렬R이 전이적 관계인지 판별하여 boolean값을 반환합니다.

- main()
--> ref, sym, trans 변수 : 각각 is_reflexive, is_symmetric, is_transitive의 반환값을 저장하는 변수입니다.
--> 동치 관계로 판별되면(ref, sym, trans 가 모두 True일 때) 
    "R is equivalence!"를 출력합니다.
--> 동치 관계가 아닌 것으로 판별되면(ref, sym, trans 중 어느 하나라도 False일 때)     
    "R is not equivalence."를 출력합니다.
