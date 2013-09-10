// Test giai phuong trinh bac 1
import static org.junit.*;
import static org.junit.Test.*;

public class TestGPTB1 
{
	private GPTB1 GPT = new GPTB1();
	
	public void test1() 
	{
		assertEquals("",-1, GPT.test(1, 1));
	}
	
	public void test2() 
	{
		assertEquals("",9, GPT.test(10, -90));
	}

}
