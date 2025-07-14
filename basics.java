import java.util.*;
public class basics{
    int arrr[] =  {3,34,34,34,34,3,34,34,34,34,34,34};

    public static void main(String[] args){
        int[] arr = new int[5];
        int a = 0;

        Scanner sc = new Scanner(System.in);
        System.out.print("enter the number for factoral series ");
        int sum=1;
        int number = sc.nextInt();
        System.out.println("enter "+number+"please enter it ");
       
        for(int i = 0 ; i <number;i++){
            arr[i] = sc.nextInt();
        }for(int i = 0 ; i <number;i++){
            if(a < arr[i]){
                a = arr[i];
            }
        }
        System.err.println(a);


    }
}