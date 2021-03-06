#include "Adder.h"
#include <nlohmann/json.hpp>
#include <QApplication>
#include "CustomizedWidget.h"
#include <iostream>

int main (int argc, char* argv[]) {
    std::cout << "CMake Conan Test" << std::endl;
    std::cout << add(5, 7) << std::endl;

    nlohmann::json j;
    j["pi"] = 3.14;
    j["text"] = "hello world";

    std::cout << j.dump() << std::endl;

    QApplication app(argc, argv);
    CustomizedWidget widget;
    widget.print();
    widget.show();
    return app.exec();
}
