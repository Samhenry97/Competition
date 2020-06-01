import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;

public class Classy {
	public  static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		int n = Integer.parseInt(line);
		HashMap<String, String> map = new HashMap<>();
		String[] classes = new String[n];
		for (int i = 0; i < n; i++) {
			line = br.readLine();
			String[] parts = line.split(" ");
			String classy = "";
			for (int j = parts.length - 2; j > 0; j--) {
				String classi = parts[j];
				if (classi.equals("upper")) {
					classy += "0";
				} else if (classi.equals("middle")) {
					classy += "1";
				} else {
					classy += "2";
				}
			}
			for (int j = 0; j < 50 - parts.length; j ++) {
				classy += "1";
			}
			String name = parts[0];
			name = name.substring(0, name.length() - 1);
			map.put(classy + name, name);
			classes[i] = classy + name;
		}
		Arrays.sort(classes);
		for (String s: classes) {
			System.out.println(map.get(s));
		}
	}
}
