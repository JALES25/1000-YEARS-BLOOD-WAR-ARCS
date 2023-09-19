import java.util.Date;

import javax.swing.text.DocumentFilter.FilterBypass;

public class Create_Dates{
    public static void main(String[] args) {
        Date d1, d2, d3;

        /*  public Date getD1() {
              return d1;
          }
      
          public void setD1(Date d1) {
              this.d1 = d1;
          }
      
          public Date getD2() {
              return d2;
          }
      
          public void setD2(Date d2) {
              this.d2 = d2;
          }
      
          public Date getD3() {
              return d3;
          }
      
          public void setD3(Date d3) {
              this.d3 = d3;
          } */
          
          d1 = new Date();
          System.out.println("Date 1: " + d1);
      
          d2 = new Date(71, 7, 1, 7, 30);
          System.out.println("Date 2: " + d2);
          
          d3 = new Date("April 3 1993 3:24 PM");
          System.out.println("Date 3: " + d3);
        
    }
}