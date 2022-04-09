#pragma once
#include <QWidget>

class CustomizedWidget : public QWidget {
    Q_OBJECT
public:
    explicit CustomizedWidget(QWidget* parent = nullptr);
    void print();

signals:
    void printSignal();
};
