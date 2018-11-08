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

+ Search Method
    + BST (Binary Search Tree / Binary Search Algrithm)

+ List ADT (Abstract Data Type) 抽象資料型態
    + 資料儲存結構 List Implementation
        + Linked List
        + Array
    + 資料操作 (新增、刪除、修改、查詢、列印)
    + Linked List
        + 其儲存方式：
            + Node (節點、車廂)：(資料 | 下一個節點的位置)
            + At the last node, the position area will be "**null**"
        + 其操作方法：
            + 新增：
                + List : [(A<sub>100</sub> | 50) (B<sub>50</sub> | 36) (D<sub>36</sub> | null)]

                + 新增於 List 首 
                    + 先新增一 node (Z<sub>data</sub> | null)
                    + 將 null 值 = 100
                    + New List : [(Z<sub>data</sub> | **100**) (A<sub>100</sub> | 50) (B<sub>50</sub> | 36) (D<sub>36</sub> | null)]

                + 新增於 List 中
                    + 先新增一 node (F<sub>400</sub> | null)
                    + 將 F 的 next position 修改為 下一資料塊的 position
                    + 再將 A 的 next position 修改為 F 的 position
                        + 主控權 位於 A
                    + New List : [(Z<sub>data</sub> | 100) (A<sub>100</sub> | ~~50~~ **400**) (F<sub>400</sub> | **50**) (B<sub>50</sub> | 36) (D<sub>36</sub> | null)]
                + 新增於 List 末
                    + 先新增一 node (K<sub>450</sub> | null)
                    + 將 D 的 next position = 450
                    + New List : [(Z<sub>data</sub> | 100) (A<sub>100</sub> | 400) (F<sub>400</sub> | 50) (B<sub>50</sub> | 36) (D<sub>36</sub> | **450**) (K<sub>450</sub> | null)]
            + 刪除 : 
                + List : [(A<sub>100</sub> | 50) (B<sub>50</sub> | 36) (D<sub>36</sub> | null)]
                + 假定刪除 Node B
                    + 主控權位於 A (需在需更動的前一個 Node)
                    + 將 A 的 next position 修改為 B 的 next position
                        + [(A<sub>100</sub> | 50) (B<sub>50</sub> | 36) (D<sub>36</sub> | null)]
                        + [(A<sub>100</sub> | 36) ~~(B<sub>50</sub> | 36)~~ (D<sub>36</sub> | null)]
                + 假定刪除 Node D
                    + 主控權位於 B
                    + 將 B 的 next position 修改為 null
                        + [(A<sub>100</sub> | 50) (B<sub>50</sub> | 36) (D<sub>36</sub> | null)]
                        + [(A<sub>100</sub> | 50) (B<sub>50</sub> | ~~36~~ **null**) ~~(D<sub>36</sub> | null)~~]

                + 資源佔用問題：刪除 List 但 資料依舊儲存於記憶體位置 (Recycle Linked List)
                        + 資源回收：保留閒置記憶體
                        + Release：將閒置記憶體釋放掉 將資源轉移回 CPU
        + 火車概念 Linked List With Header： H<sub>0</sub> > A > B > C (H<sub>0</sub> >> Header)
            + 優點：當沒有資料時，Header 依舊存在
            + 缺點：浪費 Header 空間
        + 捷運概念 Linked List Without Header： A > B > C > D
            + 優點：沒有浪費 Header 空間
            + 缺點：當沒有資料時，List 不存在

    + Type Declaration for Linked List Node
        ```java
        class ListNode{
            //Verb.
            // Constructors
                // 
            ListNode(Object theElement){
                this (theElement), null;
                // (theElement | next) as a node
            }
            LinkNode( Object theElement , ListNode n){  // ListNode > 遞迴定義
                element = theElement;
                next = n;
            }

            // Nouns
            // Friendly Data
            Object element;
            ListNode next; // next : next position(下一個記憶體位置)
        }
        ```
    + Inerator Class for Linked List
        ```java
        package DataStructures;

        public class LinkedListItr{
            LinkedListItr(ListNode theNode){
                current = theNode;
            }
            public boolean isPasdtEnd(){
                return current == null;
            }
            public Object retrieve(){
                return isPasdtEnd() ? null : current.element;
            }
            public void advance(){
                if(!isPasdtEnd()){
                    current = current.next;
                }
            }
            ListNode current; //Current position
        }
        

        ```

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