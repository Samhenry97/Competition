import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MagicalThree {
	public  static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		long n = Long.parseLong(line);
		for (long i = 2; i < 1000000; i++) {
			if (n % i == 3) {
				System.out.println(i);
				return;
			}
		}
		if((n - 3) % 3 == 0) {
			System.out.println((n - 3) / 3);
			return;
		}
		if((n - 3) % 2 == 0) {
			System.out.println((n - 3) / 2);
			return;
		}
		if((n - 3) % 1 == 0) {
			System.out.println((n - 3));
			return;
		}
	}
}
