#include <vector>
#include <iostream>
#include <map>

using namespace std;

vector<vector<double> > pixels;

double findAverage(int x, int y);
int width, height, blur;

int main() {
    cin >> width >> height >> blur;

    if(width == 0 || height == 0) {
        cout << 0;
        return 0;
    }

    for(int y = 0; y < height; y++) {
        vector<double> row;
        for(int x = 0; x < width; x++) {
            double pix;
            cin >> pix;
            row.push_back(pix);
        }
        pixels.push_back(row);
    }

    for(int i = 0; i < blur; i++) {
        vector<vector<double> > newPixels;
        for(int y = 0; y < height; y++) {
            vector<double> newRow;
            for(int x = 0; x < width; x++) {
                newRow.push_back(findAverage(x, y));
            }
            newPixels.push_back(newRow);
        }
        pixels = newPixels;
    }


    map<double, int> vals;
    for(int y = 0; y < height; y++) {
        for(int x = 0; x < width; x++) {
                vals[pixels[y][x]] += 1;
        }
    }

    cout << vals.size() << endl;

    return 0;
}

double findAverage(int x, int y) {
    int curX = -1;
    int curY = -1;
    int tempX = x;
    int tempY = y;
    double sum = 0;

    for(int i = 0; i < 9; i++) {
        tempX += curX;
        tempY += curY;
        if(tempY < 0) tempY = height - 1;
        else if(tempY >= height) tempY = 0;
        if(tempX < 0) tempX = width - 1;
        else if(tempX >= width) tempX = 0;

        sum += pixels[tempY][tempX];
        curX++;

        if(curX > 1) {
            curX = -1;
            curY += 1;
        }
        tempX = x;
        tempY = y;
    }
    return sum / 9.0;

}
