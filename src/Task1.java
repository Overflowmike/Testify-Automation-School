public class Task1 {
    public static void main(String[] args) {

        System.out.println("Hello and welcome!. This is my Java Coding");

        // JavaDataTypes
//  byte from -128 to 127
//  short from -32, 768 to 32, 767
//  int from -2,147,483,648 to 2,147,483,64
//  long    -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
//  from 6 to 7 decimal digits
//  from 15 decimal digits
//  ingle letters = 'a' 'b'
//  boolean = true, false

        byte age = 127;

        short money = 32_76;

        long soMuchMoney = -2147483649l;

        float area = 12345678.90f;

        double biggerArea = 123456.67;


        System.out.println(biggerArea);

        char option = 'm';

        boolean isAround = false;

        // String And Concat

        String bird = "hummingbird";
        String adjective = " is beautiful.";
        String newString = bird + adjective;
        System.out.println(newString);

        // string and primitive concat
        String movieName = "matrix: ";
        int parts = 4;
        boolean isReleased = false;
        System.out.println(""+parts + isReleased);

        // .concat() method
        System.out.println(movieName.concat(parts+""));
    }
}



