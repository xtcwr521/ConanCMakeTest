#include "CustomizedWidget.h"
#include <iostream>

CustomizedWidget::CustomizedWidget(QWidget* parent) : QWidget(parent) {}

void CustomizedWidget::print() {
	std::cout << "hello from the widget!" << std::endl;
    Q_EMIT printSignal();	
}
