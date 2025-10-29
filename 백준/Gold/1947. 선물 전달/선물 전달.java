import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		long a = 0L;
		long b = 1L;
		
		for (int i=3; i<=n; i++) {
			long c = (i-1) * (a+b) % 1000000000;
			a = b;
			b = c;
		}
		
		if (n == 1) {
			System.out.println(a);
		}else {
			System.out.println(b);
		}
	}
}
