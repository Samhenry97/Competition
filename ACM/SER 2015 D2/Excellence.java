import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Excellence {
	public  static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		int n = Integer.parseInt(line);
		int [] ranking = new int[n];
		for (int i = 0; i < n; i++) {
			ranking[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(ranking);
		int minval = 1000000000;
		for (int i = 0; i < n/2; i ++) {
			int v = ranking[i] + ranking[n - i - 1];
			if (v < minval) {
				minval = v;
			}
		}
		System.out.println(minval);
	}
}
