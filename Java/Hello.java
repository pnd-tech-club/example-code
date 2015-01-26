import java.util.Scanner;

public class Hello 
{
  public static void main(String[] args)
  {
	  String username;
	  Scanner keyboard = new Scanner(System.in);
	  int a, b, c;

	  System.out.print("What's your name?: ");
	  username = keyboard.next();
	  System.out.printf("Hello, %s!\n", username);

	  a = 2;
	  b = 2;
	  c = a + b;
	  System.out.printf("2 plus 2 is: %d!\n", c);
  }
}

