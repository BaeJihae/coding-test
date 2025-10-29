import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] p = new int[m];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < m; i++) {
			p[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] arr = new int[n + 1];
		for (int i=0; i<m-1; i++) {
			int l = Math.min(p[i] - 1, p[i+1] - 1);
			int r = Math.max(p[i] - 1, p[i+1] - 1);
			
			arr[l]++;
			arr[r]--;
		}
		
		for (int i = 1; i < n; i++) {
			arr[i] += arr[i-1];
		}
		
		long answer = 0;
		for (int i=0; i<n-1; i++) {
			int k = arr[i];
			if (k == 0) {
				br.readLine();
				continue;
			}
			st = new StringTokenizer(br.readLine());
			long A = Long.parseLong(st.nextToken());
			long B = Long.parseLong(st.nextToken());
			long C = Long.parseLong(st.nextToken());
			
			answer += Math.min(A*(long)k, B*(long)k + C);
		}
		
		System.out.println(answer);
	}
}
