package lotto;

import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;
/**
 *
 * @author 1500264
 */
public class Lotto {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Random rn = new Random();
        int num1 = 0;
        int num2 = 0;
        int num3 = 0;
        int num4 = 0;
        int num5 = 0;
        Scanner keyboard = new Scanner(System.in);
        
        System.out.println("Choose your first number (1-10)");
        int holder = keyboard.nextInt();
        if(holder > 0 && holder < 11)
        {
            num1 = holder;
        }
        else
        {
            System.out.println("You failed to to follow simple instructions. Your number will be chosen for you.");
             num1 = rn.nextInt(10)+1;
             System.out.println(num1 + " was chosen.");
        }
        
        System.out.println("Choose your first number (11-20)");
        holder = keyboard.nextInt();
        if(holder > 10 && holder < 21)
        {
            num2 = holder;
        }
        else
        {
            System.out.println("You failed to to follow simple instructions. Your number will be chosen for you.");
            num2 = rn.nextInt(10)+11;
            System.out.println(num2 + " was chosen.");
        }
        
        System.out.println("Choose your first number (21-30)");
        holder = keyboard.nextInt();
        if(holder > 20 && holder < 31)
        {
            num3 = holder;
        }
        else
        {
            System.out.println("You failed to to follow simple instructions. Your number will be chosen for you.");
            num3 = rn.nextInt(10)+21;
            System.out.println(num3 + " was chosen.");
        }
        
        System.out.println("Choose your first number (31-40)");
        holder = keyboard.nextInt();
        if(holder > 30 && holder < 41)
        {
            num4 = holder;
        }
        else
        {
            System.out.println("You failed to to follow simple instructions. Your number will be chosen for you.");
            num4 = rn.nextInt(10)+31;
            System.out.println(num4 + " was chosen.");
        }
        
        System.out.println("Choose your first number (41-50)");
        holder = keyboard.nextInt();
        if(holder > 40 && holder < 51)
        {
            num5 = holder;
        }
        else
        {
            System.out.println("You failed to to follow simple instructions. Your number will be chosen for you.");
            num5 = rn.nextInt(10)+41;
            System.out.println(num5 + " was chosen.");
        }
        
        int[] usrArray = {num1, num2, num3, num4, num5};
        
        for(int count = 1;;count++){
            int r1 = rn.nextInt(10)+1;
            int r2 = rn.nextInt(10)+11;
            int r3 = rn.nextInt(10)+21;
            int r4 = rn.nextInt(10)+31;
            int r5 = rn.nextInt(10)+41;
            int[] rnArray = {r1, r2, r3, r4, r5};
            if(Arrays.equals(usrArray, rnArray)){
                System.out.println("You matched all 5 numbers! It only took " + count + " tries!");
                break;
            }
            
            
            
        }
    }
    
}
