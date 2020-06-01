import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Persistance {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		int persistance = line.length();
		int count = 0;
		while (persistance > 1) {
			long product = 1;
			for (char c: line.toCharArray()) {
				long n = Integer.parseInt("" + c);
				product *= n;
			}
		    persistance = ("" + product).length();
		    line = "" + product;
			count ++;
		}
		System.out.println(count);
	}
}
