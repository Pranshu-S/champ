#include <iostream>
namespace stochlite {
    double tof_coor[6][3] = 
    {
        { 0.150,  0.000, -0.025},
        { 0.065,  0.047, -0.025},
        {-0.065,  0.047, -0.025},
        {-0.150,  0.000, -0.025},
        {-0.065, -0.047, -0.025},
        { 0.065, -0.047, -0.025}
    };

                        // {{ -0.065,  0.047, 0.025},  //tof1
                        //  { -0.150,      0, 0.025},  //tof2
                        //  { -0.065, -0.047, 0.025},  //tof3
                        //  {  0.065, -0.047, 0.025},  //tof4
                        //  {  0.150,      0, 0.025},  //tof5
                        //  {  0.065,  0.047, 0.025}}; //tof6
}