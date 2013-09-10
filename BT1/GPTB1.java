//Giai phuong trinh bac 1
public class GPTB1 
{
	public static int test(int a, int b) 
	{
		if((a==0)&&(b==0))
		{
			System.out.println("X vo han");
		}
		else
		{
			if((a==0)&&(b!=0))
			{
				System.out.println("Khong co x");
			}
			System.out.println(-b/a);
		}
		return 0;
	}	
}
