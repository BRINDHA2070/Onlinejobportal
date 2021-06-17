
import java.util.Scanner;
public class NewArray{
public static void main(String[] args){
int[] x=new int[5];
int[] y=new int[5];
Scanner Scan=new Scanner(System.in);
System.out.println("enter value = ");
for(int i=0;i<5;i++){
x[i]=Scan.nextInt();
}


for(int i=0;i<5;i++){
	int v=1;
	for(int j=0;j<5;j++){
		if(j!=i){
			v=v*x[j];

			}
		else{
			v=v;
			}
}	
		y[i]=v;		
	}
System.out.print("New Array Is =");
for(int i=0;i<5;i++){
System.out.print(" "+y[i]);





}
}
}









































































