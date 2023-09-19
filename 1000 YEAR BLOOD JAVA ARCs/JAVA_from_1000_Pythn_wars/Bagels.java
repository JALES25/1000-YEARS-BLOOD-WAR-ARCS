
/*
 * In Bagels, a deductive logic game, you must guess the secret tree-digit number based on clues. 
    The game offers one of the following hints in response to your guess:
    'Pico' when your guess has the correct digit in the wrong place, 
    'Fermi' when your guess has the correct digit in the correct place, and
    'Bagels' if your guess has no correct digits.
    YOU HAVE 10 TRIES TO GUESS THE CORRECT NUMBER.
 */

import java.util.Random;
import java.util.Scanner;


 public class Bagels {

   public static void prntln(String contnt) {
      System.out.println(contnt);
   }

   public static String methodA() {

      String roll_The_Intro = "Bagels, a deductive logic game. By TYLONs17" ;
      prntln(roll_The_Intro);

      System.out.println("Would you like to continue? : Type YES or NO \n");
      Scanner scan = new Scanner(System.in);
      String cont = scan.nextLine() ;
      
      return cont ;
      


   }
   
    

 }