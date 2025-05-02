#include<stdio.h>
#include<stdlib.h>
#include<math.h>

double distance(double x1, double x2, double y1, double y2) {
    return sqrt(((x2-x1) * (x2-x1)) + ((y2-y1) * (y2-y1)));
}

double norm(double x, double min, double max) {
    return (x-min)/(max-min);
}

int main(void)
{
    double x1 = 20;
    double y1 = 2000;

    double x2 = 40;
    double y2 = 9000;

    double d = distance(x1, x2, y1, y2);
    printf("d=%f (distancia nao normalizada)\n", d);
    
    double x1_min = 18;
    double x2_max = 60;
    double x = 40;

    double y1_min = 1000;
    double y2_max = 10000;

    double x1_norm = norm(x1, x1_min, x2_max);
    printf("x1 normal=%f\n", x1_norm);

    double x2_norm = norm(x2, x1_min, x2_max);
    printf("x2 normal: %f\n", x2_norm);

    double y1_norm = norm(y1, y1_min, y2_max);
    printf("y1 normal: %f\n", y1_norm);

    double y2_norm = norm(y2, y1_min, y2_max);
    printf("y2 normal: %f\n", y2_norm);

    double d2 = distance(x1_norm, x2_norm, y1_norm, y2_norm);
    printf("d=%f (distancia normalizada)\n", d2);


    return 0;
}