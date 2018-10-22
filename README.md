# DataStructures

## 重點
+ 迴圈 vs 遞迴
    + 迴圈執行效率較佳
    + 遞迴程式可讀性較高
    + 結束點 (迴圈與遞迴轉換)
+ 二進制轉換
    1. N/2
    2. N%2
    3. reverse print 餘數
    + HW : https://github.com/jason19970210/DataStructures/tree/master/HW/20180920
+ 費氏數列
+ Modular Exponention 模指數運算
    1. a<sup>b</sup> mod(%) N
    2. RSA Security 加解密
+ 大整數乘法
    1. 拆解 N<sub>1</sub> x 10<sup>n</sup> + N<sub>2</sub>
+ Closet Pair of Points
+ **Merge Sort 合併排序法**
    1. 遞迴切割與合併
    2. **必考**
+ Tower of Hanoi 河內塔
    1. N / N-1 
    2. 起始點 from、暫存點 temp、目標點 to (assign to char)
+ Algorithm Analysis
    1. Relative Growth Rate 相對成長率 RGR
        + RGR 方式：lim(N->infinity) T(N)/G(N)
            + The Results : `0`,`infinity`,`C 定值`,`dynamic 動態`
            + T(N) => 演算法的時間函數
            + G(N) => 另一個演算法的時間函數 / 自訂的數學函數
        + Ex.   T(N) = 3N<sup>2</sup>+ N + 1  
                T(10) 3x10<sup>2</sup> + 10 + 1  
                G(N) = 2N<sup>3</sup> + 1  
                lim(N->infinity) T(N)/G(N) = 0 (趨近於0)


    2. Bog O. Notation BigO表示法
        + Big Oh. 上限值
        + Big Omega 下限值
        + Big Theta 接近值
        + Little Oh. 小於

## Homework    
+ 20180920
    + 使用者輸入十進制: n
    + 輸入欲轉換進制: b
    + 輸出結果: N(10) ->  X(B)  
    + 遞迴 / 迴圈  
    + 執行時間 (加分)
    + 交 .java & .exe & .doc(.pdf) with code and 5 results  
+ 20181004
    + N = 3 ++ 5  
    + 次數 -> 全域變數(M = 0) 
    + 程序執行時間 (Tend - Tstart)
    + Source Code
        + h(N,'A','B','C')