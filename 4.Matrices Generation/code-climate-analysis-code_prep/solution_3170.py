
import java.util.Scanner;
public class p10 {

 public static void main(String[] args) {
 Scanner cs=new Scanner(System.in);
  System.out.println("Enter the row and column size:");
 int row_size,out,in;
  row_size=cs.nextInt();
  for(out=row_size;out>=1;out--)
  {
  for(in=1;in<=row_size;in++)
   System.out.print(out);

     System.out.println();
  }
 cs.close();
 }
}