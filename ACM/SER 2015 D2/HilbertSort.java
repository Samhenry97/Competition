import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;

public class HilbertSort {
	private static HilbertSort hs = new HilbertSort();
	private static int s;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		String[] parts = line.split(" ");
		int n = Integer.parseInt(parts[0]);
		s = Integer.parseInt(parts[1]);
		Point[] points = new Point[n];
		for (int i = 0; i < n; i++) {
			line = br.readLine();
			parts = line.split(" ");
			int x = Integer.parseInt(parts[0]);
			int y = Integer.parseInt(parts[1]);
			points[i] = hs.new Point(x, y);
		}
		Arrays.sort(points, hs.new c());
		for (Point p: points) {
			System.out.println(p.x + " " + p.y);
		}
	}
	private class Point {
		public int x;
		public int y;
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	private  class  c implements Comparator<Point>{
		public int compare(Point a, Point b) {
			Point corner = hs.new Point(0,0);
			String direction = "1234";
			for (double i = s; i > 1; i = i/2 - 0.5) {
				int quad = quadrant(a, i, corner);
				int diff = quad - quadrant(b, i, corner);
				if (diff != 0) {
					return diff;
				} else {
					switch(quad) {
					case 1: corner = hs.new Point(corner.x, corner.y); direction = direction.charAt(1) + direction.charAt(4) + direction.charAt(3) + direction.charAt(2) + "" ; break;
					case 2: corner = hs.new Point(corner.x, (int) (corner.y + (i/2 + 0.5))); break;
					case 3: corner = hs.new Point((int) (corner.x + (i/2 + 0.5)), (int) (corner.y + (i/2 + 0.5))); break;
					case 4: corner = hs.new Point((int) (corner.x + (i/2 + 0.5)), corner.y); break;
					}
				}
			}
			return 0;
		}
		private int quadrant (Point p, double s, Point corner) {
			int x = p.x - corner.x;
			int y = p.y - corner.y;
			if (x >= s/2.0) {
				if (y >= s/2.0) {
					return 3;
				}else {
					return 2;
				}
			} else {
				if (y >= s/2.0) {
					return 4;
				}else {
					return 1;
				}
			}
		}
	}	
}