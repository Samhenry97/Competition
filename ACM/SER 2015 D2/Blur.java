import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Blur {
	private int blurCount;
	private int[][] pixels;
	private int width;
	private int height;
	
	public Blur(int blurCount, int[][] pixels) {
		this.blurCount = blurCount;
		this.pixels = pixels;
		width = pixels[0].length;
		height = pixels.length;
		
		for(int y = 0; y < pixels.length; y++) {
			for(int x = 0; x < pixels.length; x++) {
				findAverage(y, x);
			}
		}
	}
	
	public void findAverage(int y, int x) {
		int curX = -1;
		int curY = -1;
		int tempX = x;
		int tempY = y;
		int sum = 0;
		
		for(int i = 0; i < 9; i++) {
			tempX += curX;
			tempY += curY;
			if(tempX < 0) tempX = width - 1;
			if(tempY < 0) tempY = height - 1;
			if(tempX >= width) tempX = 0;
			if(tempY >= height) tempY = 0;
			sum += pixels[tempY][tempX];
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] pixels;
		String line = br.readLine();
		String[] data = line.split(" ");
		int width = Integer.parseInt(data[0]);
		int height = Integer.parseInt(data[1]);
		int blurCount = Integer.parseInt(data[2]);
		pixels = new int[height][width];
		
		for(int y = 0; y < height; y++) {
			line = br.readLine();
			data = line.split(" ");
			for(int x = 0; x < data.length; x++) {
				pixels[y][x] = Integer.parseInt(data[x]);
			}
		}			
			
		new Blur(blurCount, pixels);
	}
	
}
