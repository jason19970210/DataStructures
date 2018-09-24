import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        int i = 0;
        int num;
        int base;
  
    Scanner sc = new Scanner(System.in);
  
        num = sc.nextInt();
        base = sc.nextInt();
  
        convert(num, base);
    }
 
    static void convert(int num, int base) {
  
    if(num > 0) {
    
        int result = num / base;
        System.out.print(num % base);
        convert(result, base);

    } else if (num < 0){

        System.out.print("Error!\n")

    }


    return; 
    }

}