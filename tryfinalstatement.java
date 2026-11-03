
public class FinallyDemo {

    static int display() {
        try {
            System.out.println("Inside try block");
            return 10;
        } finally {
            System.out.println("I am inevitable");
        }
    }

    public static void main(String[] args) {
        int result = display();
        System.out.println("Return value: " + result);
    }
}