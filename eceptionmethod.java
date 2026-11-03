public class TryCatchExample3 {
    public static void main(String[] args) {
        try
        {
            int data = 50 / 0; // may throw exception
            // If exception occurs, the remaining statement will not execute
            System.out.println("rest of the code");
        }
        // handling the exception
        catch (ArithmeticException e)
        {
            System.out.println(e);
        }
    }
}