/*
 * Starts the engine
 * Stopts the engine
 * speed up
 * change gear
 * stall
*/


public class motoc {
    String make;
    String color;
    boolean engine_state;

    void start_Engine() {
        if (engine_state == true) {
            System.out.println("The engine is already on.");
        } else {
            engine_state = true;
            System.out.println("The engine is now on.");
        }
    }

    void show_Atts() {
        System.out.println("This is a" + color + " " + make);
        if (engine_state == true) 
            System.out.println("The engine is on.");
        else System.out.println("The engine is off.");
    }


public static void Do_moto() {
    motoc m = new motoc();

    m.make = "Yamaha RZ350";
    m.color = "Yellow";

    System.out.println("Calling show_Atts...");
    m.show_Atts();
    System.out.println("-----------------");
    System.out.println("Starting engine...");
    m.start_Engine();
    System.out.println("-----------------");
    System.out.println("Calling show_Atts...");
    m.show_Atts();
    System.out.println("-----------------");
    System.out.println("Starting engine...");
    m.start_Engine();

}
}
